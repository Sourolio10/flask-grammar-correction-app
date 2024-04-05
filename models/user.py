import pandas as pd
from sqlalchemy import text
from config.db_config import engine
from config.logging import logger
class UserDBHandler():
    def __init__(self,table_name,engine):
        self.table_name = table_name
        self.engine = engine
    def insertUser(self,user_dict):
        user_data = {
            'username':[user_dict['username']],
            'useremail':[user_dict['useremail']],
            'password':[user_dict['password']]
        }
        data = pd.DataFrame.from_dict(user_data,orient='columns')
        data.to_sql(con=self.engine,name = 'user', if_exists='append')



    def getUser(self, data):
        user_email = data['useremail']
        password = data['password']
        SQL = "SELECT username , useremail, password FROM user WHERE useremail='{given_user}' and password='{given_password}'".format(given_user = user_email, given_password = password)
        data = pd.read_sql(con=self.engine , sql= SQL)
        return data.to_dict(orient='records')
    
    def deleteUser(self, useremail):
        SQL = "DELETE from user where useremail='{useremail}';".format(useremail = useremail)
        with engine.connect() as eng:
            eng.execute(text(SQL))
            eng.commit()
            
    def updateUser(self, useremail, new_password):
        SQL = "UPDATE user SET password = '{new_password}' where useremail = '{useremail}'".format(new_password = new_password, useremail = useremail)
        with engine.connect() as eng:
            eng.execute(text(SQL))
            eng.commit()
    
    def getUserByEmail(self, useremail):
        SQL = "SELECT useremail FROM user WHERE useremail='{useremail}'".format(useremail = useremail)
        data = pd.read_sql(con=self.engine , sql= SQL)
        return data.to_dict(orient='records')



                
