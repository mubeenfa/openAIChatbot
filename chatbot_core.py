import logging
from openai import OpenAI, APIError, AuthenticationError, RateLimitError, Timeout
from typing import List, Dict


class OpenAIChatbot:
    def __init__(self, api_key: str, model_name: str = "gpt-3.5-turbo"):
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name
        self.conversation_history: List[Dict[str, str]] = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

    def get_response(self, user_input: str) -> str:
        """Send user input to OpenAI and return assistant's reply."""
        if not user_input.strip():
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

        except AuthenticationError:
            return "❌ Authentication failed. Check your API key."
        except RateLimitError:
            return "⚠️ You are being rate-limited. Please try again later."
        except Timeout:
            return "⏳ The request timed out. Try again."
        except APIError as e:
            return f"🔥 OpenAI API error: {e}"
        except Exception as e:
            logging.error("Unexpected error", exc_info=True)
            return f"❗ Unexpected error: {e}"
