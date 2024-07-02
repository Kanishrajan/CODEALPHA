import random

# Define a function to handle the conversation
def chat():
    print("Hello! I am your chatting bot.")
    print("You can start chatting with me. Type 'bye' to end the conversation.")
    
    # Continuously loop until user says 'bye'
    while True:
        user_input = input("You: ")  # Get user input
        
        # Check if user wants to end the conversation
        if user_input.lower() == 'bye':
            print("Bot: Goodbye! Have a nice day.")
            break  # Exit the loop and end the conversation
        
        # Respond based on user input
        if 'hi' in user_input or 'hello' in user_input:
            print("Bot: Hi there!")
        elif 'how are you' in user_input:
            responses = ["I'm fine, thank you!", "Pretty good!", "Feeling great!"]
            print(f"Bot: {random.choice(responses)}")
        elif 'what can you do' in user_input or 'what do you do' in user_input:
            print("Bot: I can chat with you, answer questions, and provide information.")
        elif 'your name' in user_input:
            print("Bot: My name is ChatBot. What's yours?")
        elif 'weather' in user_input:
            print("Bot: I'm not sure about the weather right now. You can check a weather website!")
        elif 'tell me a joke' in user_input:
            jokes = ["Why don't scientists trust atoms? Because they make up everything!",
                     "Parallel lines have so much in common. It’s a shame they’ll never meet.",
                     "I told my wife she should embrace her mistakes. She gave me a hug."]
            print(f"Bot: {random.choice(jokes)}")
        elif 'how old are you' in user_input or 'your age' in user_input:
            print("Bot: I don't have an age. I'm just a program!")
        else:
            unknown_responses = ["Sorry, I didn't understand that.",
                                 "I'm not sure what you mean.",
                                 "Could you please rephrase that?"]
            print(f"Bot: {random.choice(unknown_responses)}")

# Start the conversation
if __name__ == "__main__":
    chat()
