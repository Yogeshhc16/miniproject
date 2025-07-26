# chatbot.py
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import datetime
import random
# Download NLTK data (only needed once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
# Print chatbot greeting
print("🤖 NLTK Chatbot — Type 'exit' to quit\n")
# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()
# Sample jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why was the math book sad? Because it had too many problems.",
    "Why did the computer go to the doctor? Because it had a virus!",
]
# Define intent keywords
intents = {
    "greeting": ["hello", "hi", "hey"],
    "how_are_you": ["how", "are", "you"],
    "name": ["name"],
    "bye": ["bye", "exit", "quit"],
    "help": ["help", "commands"],
    "time": ["time", "clock"],
    "date": ["date", "day"],
    "joke": ["joke", "funny"],
    "weather": ["weather"],
    "thanks": ["thank", "thanks"],
}
# Define responses
responses = {
    "greeting": "Hello there! 😊",
    "how_are_you": "I'm doing great! How about you?",
    "name": "I'm a Python-powered chatbot using NLTK!",
    "bye": "Goodbye! 👋 Have a great day!",
    "help": "You can say hi, ask the time or date, request a joke, or say bye!",
    "time": lambda: f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}.",
    "date": lambda: f"Today is {datetime.datetime.now().strftime('%A, %B %d, %Y')}.",
    "joke": lambda: random.choice(jokes),
    "weather": "I'm not connected to the internet, but I hope it's nice outside! ☀",
    "thanks": "You're welcome! 😊",
}
# Preprocess user input
def preprocess_input(text):
    tokens = word_tokenize(text.lower())
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized
# Detect intent
def detect_intent(tokens):
    for intent, keywords in intents.items():
        if any(word in tokens for word in keywords):
            return intent
    return "unknown"
# Generate chatbot response
def chatbot_response(user_input):
    tokens = preprocess_input(user_input)
    intent = detect_intent(tokens)
    if intent in responses:
        response = responses[intent]
        return response() if callable(response) else response
    else:
        return "I'm not sure how to respond to that. Try asking something else!"
# Chat loop
while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ["exit", "quit", "bye"]:
        print("Chatbot:", responses["bye"])
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)