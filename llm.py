import anthropic
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()  # reads ANTHROPIC_API_KEY from the .env file

MODEL = "claude-sonnet-5-5"

client = Anthropic()

def ask(prompt, max_tokens=1024):
    """Send one prompt and return the model's text reply."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text

if __name__ == "__main__":
    print(ask("Say hello in one short sentence."))