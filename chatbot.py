def get_response(message):
    message = message.lower().strip()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message in ("what is your name", "your name", "name"):
        return "I'm CodeBot, a simple Python chatbot."
    elif message in ("help", "what can you do"):
        return "Try saying: hello, how are you, what is your name, or bye."
    elif message in ("thanks", "thank you"):
        return "You're welcome!"
    elif message in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        return "Sorry, mujhe samajh nahi aaya. Type 'help' for options."


def main():
    print("CodeBot: Hello! Type 'bye' to exit.")
    while True:
        user = input("You: ")
        reply = get_response(user)
        print("CodeBot:", reply)
        if user.lower().strip() in ("bye", "goodbye", "exit"):
            break


if __name__ == "__main__":
    main()
