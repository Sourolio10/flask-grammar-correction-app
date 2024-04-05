import unittest
import json
from app import app
from flask_jwt_extended import create_access_token
from unittest.mock import Mock ,patch
class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()
        token = create_access_token("test@test.com")
        self.headers = {"Authorization": "Bearer "+ token}

    # Test health check route
    def test_health_check(self):
        response = self.client.get('/',headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Web App with python flask is running')

    @patch('app.user_db_handler.getUser')
    # Test login route
    def test_login(self, mockHandler):
        mockHandler.return_value = {'useremail': 'test@test.com'}
        login_data = {
            'username': 'test_user',
            'password': 'password123',
            'useremail':"test@test.com"
        }
        response = self.client.post('/login', json=login_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in json.loads(response.data.decode()))

    # Test signup route
    @patch('app.user_db_handler.insertUser')
    def test_signup(self, mockHandler):
        signup_data = {
            'username': 'new_user',
            'password': 'new_password',
            'useremail': 'new_user@example.com'
        }
        response = self.client.post('/signup', json=signup_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in json.loads(response.data.decode()))

    # Test deleteUser route
    def test_delete_user(self):
        delete_data = {
            'username': 'test_user'
        }
        response = self.client.delete('/deleteUser', json=delete_data,headers=self.headers)
        self.assertEqual(response.status_code, 200)

    # Test updateUser route
    def test_update_user(self):
        update_data = {
            'username': 'test_user',
            'password': 'new_password'
        }
        response = self.client.patch('/updateUser', json=update_data,headers=self.headers)
        self.assertEqual(response.status_code, 200)

    # Test grammar check route
    @patch('app.user_db_handler.getUserByEmail')
    @patch('app.grammarChecker.run_inference')
    def test_grammar_check(self,mock_inference,mock_handler):
        mock_handler.return_value = ['lol']
        mock_inference.return_value = {
            "correctedText":"lmao"
        }
        grammar_data = {
            'text': 'The quick brown foxs jump over the lazy dog.'
        }
        response = self.client.post('/grammar', json=grammar_data,headers=self.headers)
        self.assertEqual(response.status_code, 200)
        print(response)
        self.assertTrue('correctedText' in response.get_json(force=True))

