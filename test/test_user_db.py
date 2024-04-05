import unittest
from unittest.mock import Mock, MagicMock,patch
from models.user import UserDBHandler
import pandas
class TestUserDbhandler(unittest.TestCase):
    @patch('models.user.engine')
    def test_delete_user_when_success(self,mock_engine):
        #Given
        given_useremail = "habibi@dubai.com"
        mockctx = Mock()
        mock_engine.connect.return_value.__enter__.return_value = mockctx
        given_table_name = 'users'
        #When
        user_db_handler = UserDBHandler(table_name=given_table_name,engine= mock_engine)
        user_db_handler.deleteUser(given_useremail)

        #Then
        mockctx.execute.assert_called_once()

    @patch('models.user.engine')
    def test_update_user_when_success(self,mock_engine):
        #Given
        given_useremail = "habibi@dubai.com"
        given_password = "password1234"
        mockctx = Mock()
        mock_engine.connect.return_value.__enter__.return_value = mockctx
        given_table_name = 'users'
        #When
        user_db_handler = UserDBHandler(table_name=given_table_name,engine= mock_engine)
        user_db_handler.updateUser(given_useremail, given_password)

        #Then
        mockctx.execute.assert_called_once()