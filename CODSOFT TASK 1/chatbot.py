#!/usr/bin/env python3
"""Refactored simple rule-based chatbot.

This implements the requested steps:
- Step 1: Basic loop + input + lowercase + if/elif/else
- Step 2: More responses + default reply
- Step 3: Refactor into functions, welcome message, formatted output

Run:
    python chatbot.py

The bot exits when you type 'bye'.
"""

def get_response(message: str) -> str:
    """Return a chatbot response for a normalized message.

    Uses simple if/elif/else rules (easy for beginners to read).
    The input is expected to be already lowercased and stripped.
    """
    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine!"
    elif message == "what is your name":
        return "I am a friendly chatbot."
    elif message == "what can you do":
        return "I can respond to simple questions and say goodbye."
    elif message == "thank you" or message == "thanks":
        return "You're welcome!"
    elif message == "bye":
        # Return a special token to indicate exit
        return "__EXIT__"
    else:
        # Default response for unknown inputs
        return "Sorry, I didn't understand that."


def run_chatbot():
    """Main loop: greet the user, read input, and respond until exit."""
    # Welcome message
    print("==============================")
    print("Welcome to the Simple Chatbot!")
    print("Type 'bye' to exit.")
    print("==============================")

    while True:
        # Take user input and normalize it
        user_input = input("You: ").lower().strip()

        # Get a response from the rule-based function
        reply = get_response(user_input)

        # If the response is the exit token, show goodbye and break
        if reply == "__EXIT__":
            print("Chatbot: Goodbye! It was nice talking to you.")
            break

        # Print the bot reply in a clean format
        print(f"Chatbot: {reply}")


if __name__ == "__main__":
    run_chatbot()


# Sample output (example session):
# ==============================
# Welcome to the Simple Chatbot!
# Type 'bye' to exit.
# ==============================
# You: hello
# Chatbot: Hi!
# You: how are you
# Chatbot: I'm fine!
# You: what is your name
# Chatbot: I am a friendly chatbot.
# You: what can you do
# Chatbot: I can respond to simple questions and say goodbye.
# You: thank you
# Chatbot: You're welcome!
# You: what's up
# Chatbot: Sorry, I didn't understand that.
# You: bye
# Chatbot: Goodbye! It was nice talking to you.
