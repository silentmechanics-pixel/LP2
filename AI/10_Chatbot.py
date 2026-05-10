def chatbot():
    print("Welcome to Smart Cafe Chatbot")
    print("Type 'exit' to end the chat")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Bot: Thank you for visiting Smart Cafe. Have a nice day!")
            break

        elif "hello" in user or "hi" in user:
            print("Bot: Hello! How may I help you today?")

        elif "menu" in user:
            print("Bot: We serve Pizza, Burgers, Sandwiches, Coffee and Cold Drinks.")

        elif "pizza" in user:
            print("Bot: Pizza starts from Rs.199. Would you like to order one?")

        elif "coffee" in user:
            print("Bot: We have Cappuccino, Espresso and Cold Coffee available.")

        elif "time" in user or "open" in user:
            print("Bot: Our cafe is open from 9 AM to 11 PM.")

        elif "location" in user or "address" in user:
            print("Bot: We are located near City Mall, Pune.")

        elif "order" in user:
            print("Bot: Your order has been placed successfully.")

        elif "bye" in user:
            print("Bot: Goodbye! Visit again.")

        else:
            print("Bot: Sorry, I did not understand your request.")


chatbot()