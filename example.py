"""Example program demonstrating all functions in the Quotes package."""
import sys 
import os 

sys.path.insert(0, os.path.abspath("src"))


from quotes.generator import generate_quote, generate_celebrity_quote, generate_language_quote, generate_mood_quote


def demonstrate_quotes():
    print("\n--- Quotes Package Demonstration ---")

    print("\nRandom Quote:")
    print(generate_quote())

    celebrity = "Albert Einstein"
    print(f"\nQuote from {celebrity}:")
    print(generate_celebrity_quote(celebrity))

    language = "French"
    print(f"\nQuote in {language}:")
    print(generate_language_quote(language))

    mood = "happy"
    print(f"\n{mood.capitalize()} Quote:")
    print(generate_mood_quote(mood))

if __name__ == "__main__":
    demonstrate_quotes()
