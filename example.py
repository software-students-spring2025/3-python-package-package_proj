"""Example program that uses all functions of the quotes package and demonstrates its complete functionality."""

from dotenv import load_dotenv
import quotes

# load env variables
load_dotenv()


def main():
    """Demonstrate features of the package"""
    print("Daily Quote Generator Demonstration\n")

    # get a random quote
    print("Random Quote:")
    print(quotes.generate_quote())
    print()

    # get celebrity quote

    # get language quote

    # get mood quote
