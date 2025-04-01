"""This module fetches and stores random quotes."""

import random
import requests

def get_quote_from_api() -> str:
    """Fetches a random quote from the API and appends it to a file."""
    response = requests.get("https://zenquotes.io/api/random", timeout=5).json()
    quote = f"\"{response[0]['q']} - {response[0]['a']}\""

    with open("quotes.txt", mode="a", encoding="utf-8") as file:
        file.write(quote + "\n")

    return quote

def get_quote_from_file() -> str:
    """Retrieves a random quote from a file."""
    with open("quotes.txt", mode="r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]
        return random.choice(lines)
