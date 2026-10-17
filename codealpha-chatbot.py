# CodeAlpha Python Programming Internship - Task 4

def get_response(user_input):
    
    user_input = user_input.lower().strip()

  
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."


print("Chatbot: Type 'bye' to exit.")

# Keep the chat running again and again
while True:
    # Take input from the user
    user_input = input("You: ")

    # Get the reply and show it
    reply = get_response(user_input)
    print("Chatbot:", reply)

    # If the reply is Goodbye, stop the loop
    if reply == "Goodbye!":
        break