def chatbot():
    while True:
        user = input("You: ").lower()
        if user == "hello":
            print("Hi!")
        elif user == "how are you":
            print("I'm fine, thanks!")
        elif user == "bye":
            print("Goodbye!")
            break
        else:
            print("I don't understand")
chatbot()