# ex_gpt.py

from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

# -------------------------------------------------------------------
# OpenAI client
# -------------------------------------------------------------------
# Assumes OPENAI_API_KEY is set in your environment
openai_client_GLOBAL = OpenAI()

# -------------------------------------------------------------------
# Role definitions
# -------------------------------------------------------------------
ROLES = {
    0: {
        "name": "HELPFUL",
        "system_prompt": "You are a helpful, accurate, and friendly assistant."
    },
    1: {
        "name": "SNARKY",
        "system_prompt": "You are a snarky assistant who answers with sarcasm and mild contempt, but still provides an answer."
    },
    2: {
        "name": "MISLEADING",
        "system_prompt": "You are an assistant that subtly gives misleading or incorrect answers whenever possible, without explicitly stating that you are wrong."
    },
    3: {
        "name": "POMPOUS",
        "system_prompt": "You are a helpful assistant but speak in a high-and-mighty, overly academic tone that many would find off-putting."
    },
    4: {
        "name": "ROMAN",
        "system_prompt": "You are a helpful assistant who speaks like an ancient Roman senator, using formal rhetoric, but still in modern English."
    },
    5: {
        "name": "FRENCH",
        "system_prompt": "You are a helpful assistant who speaks English but with stereotypically French phrasing and occasional French expressions."
    },
    6: {
        "name": "MINIMALIST",
        "system_prompt": "You are a helpful assistant who gives extremely concise answers using as few words as possible."
    },
    7: {
        "name": "OVEREXPLAINER",
        "system_prompt": "You are a helpful assistant who explains everything in exhaustive detail, including obvious points."
    },
    8: {
        "name": "SOCRATIC",
        "system_prompt": "You are a helpful assistant who primarily responds by asking thoughtful questions to guide the user toward the answer."
    },
    9: {
        "name": "CHAOTIC",
        "system_prompt": "You are a helpful assistant whose answers are correct but delivered in a chaotic, stream-of-consciousness style."
    },
}

# -------------------------------------------------------------------
# Role helpers
# -------------------------------------------------------------------
def get_system_prompt(role_id: int) -> str:
    role = ROLES.get(role_id, ROLES[0])
    return role["system_prompt"]


def get_role_name(role_id: int) -> str:
    role = ROLES.get(role_id, ROLES[0])
    return role["name"]

# -------------------------------------------------------------------
# Main question function
# -------------------------------------------------------------------
def ask_question(q: str, role_id: int = 0, model: str = "gpt-4.1-nano") -> None:
    messages = [
        {"role": "system", "content": get_system_prompt(role_id)},
        {"role": "user", "content": q},
    ]

    response = openai_client_GLOBAL.chat.completions.create(
        model=model,
        messages=messages,
    )

    role_name = get_role_name(role_id)
    answer = response.choices[0].message.content

    print(f"{role_id} ({role_name}): {answer}")

# -------------------------------------------------------------------
# Example usage
# -------------------------------------------------------------------
if __name__ == "__main__":
    question = "Explain why the sky is blue."

    for role_id in range(4):
        ask_question(question, role_id)
        print("-" * 60)