import pytest
import openai
from quotes.generator import generate_language_quote


def test_generate_language_quote_valid():
    """Test that a language-based quote is generated correctly."""
    quote = generate_language_quote("french")
    assert isinstance(quote, str), "Output should be a string"
    assert len(quote) > 0, "Generated quote should not be empty"


def test_generate_language_quote_invalid_number():
    """Test that a number as language returns an error message."""
    quote = generate_language_quote(123)
    assert quote == "Error: Language must be a valid string."


def test_generate_language_quote_invalid_empty():
    """Test that an empty string returns an error message."""
    quote = generate_language_quote("")
    assert quote == "Error: Language must be a valid string."


def test_generate_language_quote_invalid_string():
    """Test behavior when an unsupported language is requested."""
    quote = generate_language_quote("qwerty")
    assert isinstance(quote, str)
    assert len(quote) > 0
