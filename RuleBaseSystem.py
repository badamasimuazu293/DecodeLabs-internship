# Simple Rule-Based Chatbot

print("🤖 ChatBot: Hello! Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("🤖 ChatBot: Hello! How are you today?")

    elif user_input == "how are you":
        print("🤖 ChatBot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("🤖 ChatBot: My name is MuazBot.")

    elif user_input == "bye" or user_input == "exit":
        print("🤖 ChatBot: Goodbye! Have a great day.")
        
    elif user_input == "help":
        print("🤖 ChatBot: Available commands: hello, hi, how are you, what is your name, help, exit")
        break

    else:
        print("🤖 ChatBot: Sorry, I don't understand that.")