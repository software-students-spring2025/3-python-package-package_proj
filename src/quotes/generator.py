import random
from .fallback import quotes
from .chatgpt import chatgpt_generate
import openai

# Set to store used quotes during runtime (resets when the program restarts)
my_quotes = set()

def generate_quote():
    """Tries ChatGPT first. If it fails, falls back to predefined quotes."""
    global my_quotes

    try:
        quote = chatgpt_generate("Generate a unique inspirational quote.")
        if quote:  # make sure the response is not empty
            my_quotes.add(quote)
            return quote
    except openai.OpenAIError:
        pass

    available_quotes = [q for q in quotes if q not in my_quotes]

    if not available_quotes:
        return "No new fallback quotes left! Try again later."

    quote = random.choice(available_quotes)
    my_quotes.add(quote)
    return quote

def generate_celebrity_quote(celebrity):
    return

def generate_mood_quote(mood):
    return

def generate_language_quote(language):
    return
