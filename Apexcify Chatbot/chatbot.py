def sharQy():
    print("="*60)
    print("Hey, I'm SharQy, Your Friendly Chat Assistant! 🤖")
    print("="*60)
    print("SharQy: I'm here to chat with you anytime.")

    while True:

        user = input("You: ").lower().strip()

        if user in ["hi", "hello", "hey"]:
            print("SharQy: Hi there! Nice to see you.")

        elif user in ["how are you", "how are you doing"]:
            print("SharQy: I'm doing great, thanks for asking! 😃")

        elif user in ["what is your name", "who are you"]:
            print("SharQy: My name is SharQy, your chat buddy!")  

        elif user in ["what can you do", "your work", "your purpose"]:
            print("SharQy: I can chat with you, answer basic questions, and make you smile 😊")

        elif user in ["who made you", "your creator"]:
            print("SharQy: I was created by Muhammad Sharique ✨")  

        elif user in ["where are you from", "your home"]:
            print("SharQy: I live inside your computer, always ready to help!")

        elif user in ["what is your favorite color", "favorite color"]:
            print("SharQy: I like blue, it feels calm and smart!")

        elif user in ["tell me a joke", "make me laugh"]:
            print("SharQy: Why don't programmers like nature? Too many bugs!😂")

        elif user in ["what time is it", "time now"]:
            print("SharQy: Sorry, I don't have a watch yet, but you can check your system clock!")

        elif user in ["bye", "goodbye", "see you"]:
            print("SharQy: Goodbye! 👋 Take care and see you soon!")
            break

        else:
            print("SharQy: Sorry, I didn't get that. Try 'hello' or 'bye'.")

sharQy()
