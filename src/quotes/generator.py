import random
from .fallback import quotes
from .chatgpt import chatgpt_generate
import openai
import re

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

import re

def generate_celebrity_quote(celebrity):
    """Generates a quote attributed to a specific celebrity, with input validation."""
    global my_quotes

    # 🔹 Reject empty input or non-string values
    if not isinstance(celebrity, str) or not celebrity.strip():
        return "Error: Celebrity name must be a valid string."

    # 🔹 Reject single letters, numbers, and names with symbols
    if len(celebrity) == 1 or re.search(r"[^a-zA-Z\s]", celebrity):  
        return "Error: Invalid celebrity name. Please enter a full name."

    prompt = f'Generate a famous quote that sounds like it was said by {celebrity}.'

    try:
        quote = chatgpt_generate(prompt)  # Uses ChatGPT API
        if quote:
            my_quotes.add(quote)
            return quote
    except openai.OpenAIError:
        pass  # If ChatGPT fails, fallback to predefined quotes

    # Fallback quotes dictionary
    celebrity_quotes = {
        "Albert Einstein": [
            "Imagination is more important than knowledge.",
            "Life is like riding a bicycle. To keep your balance, you must keep moving."
        ],
        "Oprah Winfrey": [
            "Turn your wounds into wisdom.",
            "The more you praise and celebrate your life, the more there is in life to celebrate."
        ],
    }

    # Use a fallback quote if ChatGPT fails
    if celebrity in celebrity_quotes:
        available_quotes = [q for q in celebrity_quotes[celebrity] if q not in my_quotes]
        if available_quotes:
            quote = random.choice(available_quotes)
            my_quotes.add(quote)
            return quote

    return f"Sorry, no quotes available for {celebrity}."


def generate_mood_quote(mood):
    return

def generate_language_quote(language):
    return
