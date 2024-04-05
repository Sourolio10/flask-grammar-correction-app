import requests

class GrammarCorrectionAI:
    def __init__(self, api_url, token):
        """
        Initialize the instance with the API url and the authorization token.
        """
        self.api_url = api_url
        self.headers = {"Authorization": "Bearer {auth_token}".format(auth_token=token)}

    def run_inference(self, text):
        """
        Run inference using the AI model to correct grammar in the input text.

        :param text: A string containing the text to be corrected.
        :return: The corrected text as a string.
        """
        response = requests.post(self.api_url, headers=self.headers, json=text)
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            try:
                # Assuming the API returns a list of corrections, and we're interested in the first one.
                corrected_text = result[0]['generated_text']
                return corrected_text
            except (KeyError, IndexError, TypeError):
                return "Error processing the response. The structure might have changed."
        else:
            return f"Error: Received response code {response.status_code}"

    