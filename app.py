from flask import Flask, request, jsonify, make_response
#from models.user import User
from middleware.authentication import login_required
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from aiservice.api import GrammarCorrectionAI
from config.ai_config import API_TOKEN ,API_URL
from config.db_config import engine
from models.user import UserDBHandler
from config.logging import logger
app = Flask(__name__)
grammarChecker = GrammarCorrectionAI(api_url=API_URL , token= API_TOKEN)
user_db_handler = UserDBHandler(table_name='user', engine=engine)

app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to your preferred secret key
jwt = JWTManager(app)

@app.route('/')
@login_required
def healthCheck():
    return 'Web App with python flask is running'


@app.route('/login',methods = ["POST"])
def login():
    data = request.get_json()
    user_data = user_db_handler.getUser(data)
    print(user_data)
    access_token = create_access_token(identity=user_data['useremail'])
    user_data['token'] = access_token
    logger.info(f"user logged in {user_data['useremail']}")
    return make_response(jsonify(user_data),200)

@app.route('/signup',methods = ["POST"])
def signUp():
    data = request.get_json()
    try:
        user_db_handler.insertUser(data)
    except Exception as e:
        logger.info("user already exists" , data)
        return make_response(jsonify({"error":"user already exists"}),400)
    access_token = create_access_token(identity=data['useremail'])
    data['token'] = access_token
    logger.info(f"new user created {data['useremail']}")
    return make_response(jsonify(data),200)

@app.route('/deleteUser',methods = ["DELETE"],endpoint = 'deleteuser')
@jwt_required()
def deleteUser():
    #added
    current_user = get_jwt_identity()
    print(current_user)
    data = request.get_json()
    user_db_handler.deleteUser(current_user)
    return make_response(jsonify(data),200)
    
@app.route('/updateUser',methods = ["PATCH"], endpoint='updateUser')
@jwt_required()
def updateUser():
    #added
    current_user = get_jwt_identity()
    data = request.get_json()
    
    user_db_handler.updateUser(current_user, data['password'])
    return make_response(jsonify(data),200)

@app.route('/grammar',methods = ["POST"],endpoint='grammerChecker')
@jwt_required()
def checkGrammar():
    #added
    current_user = get_jwt_identity()
    user_data = user_db_handler.getUserByEmail(current_user)
    if len(user_data)==0:
        return jsonify({"error": "Invalid user"}), 401
    data = request.json
    print(data)
    if not data:
        return jsonify({"error": "No text provided"}), 400
    
    correctedText = grammarChecker.run_inference(data)
    return make_response(jsonify({"correctedText": correctedText}),200)
    

