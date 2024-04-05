from happytransformer import HappyTextToText, TTSettings

class AIGrammarCorrector:
    def __init__(self, model_name="T5", model_version="vennify/t5-base-grammar-correction"):
        """
        Initializes the AI model for grammar correction.
        :param model_name: Name of the model to use.
        :param model_version: Version of the model.
        """
        self.model = HappyTextToText(model_name, model_version)
        self.settings = TTSettings(num_beams=5, min_length=1)
        self.text_to_correct = ""

    def feed(self, text):
        """
        Feeds text to the model for grammar correction.
        :param text: The text to be corrected.
        """
        self.text_to_correct = f"grammar: {text}"

    def execute(self):
        """
        Executes grammar correction on the provided text.
        :return: Corrected text.
        """
        if not self.text_to_correct:
            return "No text provided for correction."
        result = self.model.generate_text(self.text_to_correct, args=self.settings)
        return result.text

# Example usage
if __name__ == "__main__":
    corrector = AIGrammarCorrector()
    corrector.feed("This sentences has has bads grammar.")
    corrected_text = corrector.execute()
    print(corrected_text)
