# Rule-Based Chatbot
# CodeAlpha Python Programming Internship - Task 4
# Author: Esha Razzaq

# Name of the chatbot
BOT_NAME = "Alpha"


def get_response(user_input):
    """Return the chatbot's reply for the user's message."""

    # Make the message lowercase and remove extra spaces
    message = user_input.lower().strip()

    # Check what the user typed and return the matching reply
    if message == "":
        return "Please type something."
    elif message == "hello" or message == "hi":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "My name is " + BOT_NAME + "."
    elif message == "what can you do":
        return "I can chat with you using simple predefined replies."
    elif message == "thanks" or message == "thank you":
        return "You're welcome!"
    elif message == "help":
        return "You can say: hello, how are you, what is your name, what can you do, thanks, bye"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand. Type 'help' to see my options."


# Welcome message
print(BOT_NAME + ": Hello! Type 'help' for options or 'bye' to exit.")

# Keep the chat running again and again
while True:
    # Take input from the user
    user_input = input("You: ")

    # Get the reply and show it
    reply = get_response(user_input)
    print(BOT_NAME + ": " + reply)

    # If the reply is Goodbye, stop the loop
    if reply == "Goodbye!":
        break
