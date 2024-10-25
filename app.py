import random
import string
import streamlit as st


# Function to generate password
def generate_password(length, use_uppercase, use_lowercase, use_symbols, use_numbers):
    characters = ''

    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == '':
        return "Please select at least one character set!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Streamlit UI
st.title("Random Password Generator")

# Input controls
length = st.slider("Select password length", min_value=8, max_value=32, value=12)
use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
use_lowercase = st.checkbox("Include Lowercase Letters", value=True)
use_symbols = st.checkbox("Include Symbols", value=True)
use_numbers = st.checkbox("Include Numbers", value=True)

# Generate password button
if st.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_lowercase, use_symbols, use_numbers)
    st.success(f"Generated Password: {password}")

# Optional: Info about the password
st.write("Use the controls to customize your password with different character types.")
