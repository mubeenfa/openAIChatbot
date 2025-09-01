import os
from openai import OpenAI, APIError, AuthenticationError

API_KEY = 'YOUR_OPENAI_API_KEY'

class OpenAIChatbot:
    def __init__(self, api_key, model_name="gpt-3.5-turbo"):
        # Initialize the OpenAI client with your API key
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name
        self.conversation_history = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

    def get_response(self, user_input):
        if not user_input or user_input.isspace():
            return "Please enter a message. Your input cannot be empty."

        self.conversation_history.append({"role": "user", "content": user_input})

        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=self.conversation_history
            )

            assistant_response = response.choices[0].message.content.strip()
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            return assistant_response

        except AuthenticationError as e:
            return f"Authentication failed. Please check your API key. Error: {e}"
        except APIError as e:
            return f"An OpenAI API error occurred: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"


def start_openai_chatbot(api_key):
    if not api_key or api_key == 'YOUR_OPENAI_API_KEY':
        print("Error: Please replace 'YOUR_OPENAI_API_KEY' with your actual API key.")
        return

    my_openai_chatbot = OpenAIChatbot(api_key)

    print("OpenAI Chatbot: Hello! You can start our conversation now.")
    print("Type 'quit' or 'exit' to end the chat.")
    print("-" * 50)

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit"]:
                print("OpenAI Chatbot: Goodbye! Have a great day.")
                break

            response = my_openai_chatbot.get_response(user_input)
            print(f"OpenAI Chatbot: {response}")
            print("-" * 50)
        except (EOFError, KeyboardInterrupt):
            print("\nOpenAI Chatbot: Chat terminated by user.")
            break

start_openai_chatbot(API_KEY)