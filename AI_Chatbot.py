import nltk
nltk.download('punkt')
nltk.download('punkt_tab')  # Optional but suggested

from nltk.tokenize import word_tokenize
import random
from tkinter import *

# Predefined intents with keywords and responses
intents = {
    'greeting': {
        'keywords': ['hi', 'hello', 'hey'],
        'responses': ['Hello!', 'Hi there!', 'Hey! How can I help you?']
    },
    'goodbye': {
        'keywords': ['bye', 'goodbye', 'see you'],
        'responses': ['Goodbye!', 'Take care!', 'See you later!']
    },
    'how_are_you': {
        'keywords': ['how', 'are', 'you'],
        'responses': ['I am fine, thank you!', 'Doing well, and you?']
    },
    'creator': {
        'keywords': ['who', 'created', 'you'],
        'responses': ['I was created using Python and NLTK.', 'A smart coder made me.']
    },
    'ai': {
        'keywords': ['what', 'is', 'ai'],
        'responses': ['AI is Artificial Intelligence. I am an example of it!']
    },
    'default': {
        'responses': ['Sorry, I did not understand that.', 'Can you please rephrase?', "I'm still learning."]
    }
}

# Function to predict intent based on keyword matching
def get_intent(text):
    words = word_tokenize(text.lower())
    for intent, data in intents.items():
        if intent == 'default':
            continue
        if any(word in words for word in data['keywords']):
            return intent
    return 'default'

# Get response from bot
def get_response(user_input):
    intent = get_intent(user_input)
    return random.choice(intents[intent]['responses'])

# GUI function
def send():
    user_input = e.get()
    text.insert(END, "\nYou: " + user_input)

    if user_input.strip():
        bot_response = get_response(user_input)
        text.insert(END, "\nBot: " + bot_response)
    else:
        text.insert(END, "\nBot: Please type something.")
    
    e.delete(0, END)

# GUI setup
root = Tk()
root.title("Smart AI ChatBot")

text = Text(root, bg='black', fg='lime', font=("Arial", 12))
text.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=80)
e.grid(row=1, column=0)

send_btn = Button(root, text='Send', bg='darkorange', fg='white', width=20, command=send)
send_btn.grid(row=1, column=1)

root.mainloop()
