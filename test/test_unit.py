import unittest
from unittest.mock import Mock, patch
from aiservice.api import GrammarCorrectionAI
class Test(unittest.TestCase):
    
    @patch("aiservice.api.requests")
    def test_runinferencewhensuccess(self,mock_requests):
        #given
        given_api_url = "http//:abc.com"
        given_token = 'haduahfu'
        given_text = "lol"
        expected_result = "lol"
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{
            "generated_text" : "lol"
        }]
        mock_requests.post.return_value = mock_response

        #when
        checker = GrammarCorrectionAI(api_url=given_api_url , token = given_token)
        result = checker.run_inference(given_text)

        #Then
        self.assertEqual(expected_result, result)

    @patch("aiservice.api.requests")
    def test_run_inference_when_response_struct_change(self,mock_requests):
        #given
        given_api_url = "http//:abc.com"
        given_token = 'haduahfu'
        given_text = "lol"
        expected_result = "Error processing the response. The structure might have changed."
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{
            "generated_texts" : "lol"
        }]
        mock_requests.post.return_value = mock_response

        #when
        checker = GrammarCorrectionAI(api_url=given_api_url , token = given_token)
        result = checker.run_inference(given_text)

        #Then
        self.assertEqual(expected_result, result)

    @patch("aiservice.api.requests")
    def test_run_inference_when_failed(self,mock_requests):
        #given
        given_api_url = "http//:abc.com"
        given_token = 'haduahfu'
        given_text = "lol"
        expected_result = "Error: Received response code 400"
        mock_response = Mock()
        mock_response.status_code = 400
        mock_requests.post.return_value = mock_response

        #when
        checker = GrammarCorrectionAI(api_url=given_api_url , token = given_token)
        result = checker.run_inference(given_text)

        #Then
        self.assertEqual(expected_result, result)
