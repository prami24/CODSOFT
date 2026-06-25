from chatbot import get_response

def simulate_conversation(inputs):
    print("==============================")
    print("Welcome to the Simple Chatbot! (Simulated)")
    print("Type 'bye' to exit.")
    print("==============================")

    for line in inputs:
        print(f"You: {line}")
        reply = get_response(line.lower().strip())
        if reply == "__EXIT__":
            print("Chatbot: Goodbye! It was nice talking to you.")
            break
        print(f"Chatbot: {reply}")


if __name__ == "__main__":
    demo_inputs = [
        "hello",
        "how are you",
        "what is your name",
        "what can you do",
        "thank you",
        "whats up",
        "bye",
    ]
    simulate_conversation(demo_inputs)
