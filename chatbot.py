import logging
from config import API_KEY, MODEL_NAME
from chatbot_core import OpenAIChatbot


def start_openai_chatbot():
    if not API_KEY:
        print("Error: API key not found. Please set OPENAI_API_KEY in your .env file.")
        return

    bot = OpenAIChatbot(API_KEY, MODEL_NAME)

    print("OpenAI Chatbot: Hello! You can start our conversation now.")
    print("Type 'quit' or 'exit' to end the chat.")
    print("-" * 50)

    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit"]:
                print("OpenAI Chatbot: Goodbye! Have a great day.")
                break

            response = bot.get_response(user_input)
            print(f"OpenAI Chatbot: {response}")

    except (EOFError, KeyboardInterrupt):
        print("\nOpenAI Chatbot: Chat terminated by user.")
    finally:
        logging.info("Chat session ended.")


if __name__ == "__main__":
    start_openai_chatbot()
