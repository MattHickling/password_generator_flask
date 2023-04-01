import random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)

def generate_password(min_length="10", has_numbers=True, has_specials=True):
    min_length = int(min_length) # Convert the min_length parameter to an integer
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if has_numbers:
        characters += digits
    if has_specials:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if has_numbers:
            meets_criteria = has_number
        if has_specials:
            meets_criteria = meets_criteria and has_special

    return pwd
