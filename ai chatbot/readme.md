Chatbot using Python & NLTK

This is a simple terminal-based chatbot built using Python and NLTK (Natural Language Toolkit). It responds to basic user inputs like greetings, time, date, jokes, and more. It uses tokenization and lemmatization to understand intent.


Features

Greets the user and responds to simple inputs

Tells current date and time

Tells random jokes

Gives basic weather-like replies

Uses lemmatization and tokenization with NLTK

Runs entirely in the command line (terminal)



Technologies Used

Python 3

nltk (for NLP processing)

datetime (for date/time)

random (for joke selection)



 How to Run the Project

1. Install dependencies:

 pip install nltk


2. Run the chatbot:

python chatbot.py


3. The chatbot will prompt you for input. Type something like:

hello

tell me a joke

what's the time?

exit



🔧 NLTK Downloads (first time only)

When you first run the script, it downloads:

punkt – tokenizer

wordnet – lemmatizer

omw-1.4 – word meaning data


If it doesn't work, open Python in terminal and run:

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


Note:

No internet connection is needed — weather replies are static.

This is a rule-based chatbot, not an AI/ML model.

Made for learning 
