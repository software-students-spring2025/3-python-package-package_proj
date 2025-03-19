"""Example program that uses all functions of the quotes package and demonstrates its complete functionality."""

from dotenv import load_dotenv
import quotes

# load env variables
load_dotenv()


def main():
    """Demonstrate features of the package"""
    print("Daily Quote Generator Demonstration")

    # interactive way with user input?
    while True:
        print("\nMenu:")
        print("1. Generate a random quote")
        print("2. Generate a celebrity quote")
        print("3. Generate a quote in another language")
        print("4. Generate a quote matching a mood")
        print("5. Exit")

        userChoice = input("\nEnter your choice: ")

        # get random quote
        if userChoice == "1":
            print("\nRandom Quote:")
            print(quotes.generate_quote())

        # get quote from a celebrity
        elif userChoice == "2":
            name = input("Enter a celebrity's full name: ")
            print(f"\nQuote from {name}:")
            print(quotes.generate_celebrity_quote(name))

        # get a quote in another language
        elif userChoice == "3":
            language = input("Enter a language: ")
            print(f"\nQuote in {language}:")
            print(quotes.generate_language_quote(language))

        # get a quote in a certain mood
        elif userChoice == "4":
            mood = input("Enter a mood: ")
            print(f"\n{mood} Quote:")
            print(quotes.generate_mood_quote(mood))

        elif userChoice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Enter a number 1 to 5.")


if __name__ == "__main__":
    main()
