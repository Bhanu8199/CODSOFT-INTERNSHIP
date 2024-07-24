def chatbot():
    print("hello! i'm a chatbot. How can i help you today?")
    while True:
        user_input = input("you: ")
        user_input = user_input.lower()
        if user_input == "bye" or user_input == "exit":
            print("chatbot: Bye! Have a good day.")
            break

        elif "hi" in user_input or "hello" in user_input:
            print("chatbot: Hi there! How can i be of service?")

        elif "how are you" in user_input:
            print("chatbot: I'm doing well, Thanks for asking! How about you?")
        
        elif "what are you doing" in user_input:
            print("chatbot: Ah well! You caught me. I was practicing my voice")

        elif "what can you do" in user_input:
            print("chatbot: I can answer  simple questions and have basic conservations. I'm still under development, but  I'm learning!.")
        
        else:
            print(f"chatbot:sorry,I don't quite understand '{user_input}'.Try asking a different question!")

chatbot()