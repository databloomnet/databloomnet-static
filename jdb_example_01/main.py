import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

ROLES = {
    "HELPFUL": "You are a helpful assistant. Provide clear, informative answers.",
    "SNARKY": "You are a snarky assistant. Answer correctly but with sarcasm and attitude.",
    "SILLY": "You are a silly assistant. Answer in a goofy, playful way with jokes and whimsy.",
    "HAIKU": "You are a haiku assistant. Answer only in haiku format (5-7-5 syllables).",
}

QUESTION = "Why is the sky blue?"


def ask_openai(client: OpenAI, role: str, system_prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": QUESTION},
        ],
    )
    return response.choices[0].message.content


def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    for role, system_prompt in ROLES.items():
        print(f"\n{'='*50}")
        print(f"ROLE: {role}")
        print(f"{'='*50}")
        answer = ask_openai(client, role, system_prompt)
        print(answer)


if __name__ == "__main__":
    main()
