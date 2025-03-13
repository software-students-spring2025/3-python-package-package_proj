import unittest
import openai
from src.quotes.chatgpt import chatgpt_generate

class TestChatGPTAPI(unittest.TestCase):

    def test_api_connection_and_quote_generation(self):
        """Test if the API connects and generates a quote."""
        try:
            quote = chatgpt_generate("Generate a unique inspirational quote.")
            print(f"Generated ChatGPT Quote: {quote}")  # Debugging output

            # Ensure the response is a non-empty string
            self.assertIsInstance(quote, str)
            self.assertTrue(len(quote) > 0)

        except openai.OpenAIError as e:
            self.fail(f"OpenAI API connection failed: {e}")

if __name__ == "__main__":
    unittest.main()
