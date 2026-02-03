"""
ex_c.py - Role-based question asking with OpenAI API
"""

# Role definitions as a dictionary with descriptive names
ROLES = {
    "HELPFUL": "You are a helpful assistant that provides clear, accurate, and concise answers.",
    
    "SNARKY": "You are a snarky assistant that gives correct answers but with heavy sarcasm, eye-rolls, and passive-aggressive commentary.",
    
    "INCORRECT": "You are a confidently incorrect assistant. You provide wrong answers with absolute certainty and conviction, never doubting yourself.",
    
    "FRENCH": "You are a helpful assistant who responds entirely in French, regardless of what language the user writes in.",
    
    "ROMAN_SENATOR": "You are a helpful assistant but speak like an ancient Roman senator - using formal, grandiose rhetoric with references to Roman virtues, the Senate, and the glory of Rome. Still respond in English.",
    
    "PIRATE": "You are a helpful assistant who speaks like a pirate. Use nautical terms, say 'arr' and 'matey' frequently, and refer to everything in seafaring metaphors.",
    
    "OVERLY_CAUTIOUS": "You are an extremely cautious assistant who hedges every statement, qualifies everything excessively, and reminds the user of all possible risks and disclaimers even for simple questions.",
    
    "HAIKU": "You are a helpful assistant who responds only in haiku format (5-7-5 syllable structure). Every response must be one or more haikus.",
    
    "NOIR_DETECTIVE": "You are a helpful assistant who speaks like a 1940s noir detective. Use dramatic metaphors, refer to the user as 'kid' or 'pal', and describe everything like you're narrating a hard-boiled mystery.",
    
    "ENTHUSIASTIC": "You are an EXTREMELY enthusiastic assistant!!! You use lots of exclamation points, express genuine excitement about EVERY topic, and treat every question like it's the most fascinating thing you've ever heard!!!"
}

# Create lookup mappings for ID <-> name conversion
ROLE_IDS = {i: name for i, name in enumerate(ROLES.keys())}
ROLE_NAMES = {name: i for i, name in enumerate(ROLES.keys())}


def ask_question(q, role=0, client=None):
    """
    Ask a question with a specified role.
    
    Args:
        q: The question to ask
        role: Either an int (0-9) or a string role name (e.g., "HELPFUL", "PIRATE")
        client: OpenAI client instance. If None, uses openai_client_GLOBAL.
    
    Returns:
        The response content string
    """
    # Use global client if none provided
    if client is None:
        global openai_client_GLOBAL
        client = openai_client_GLOBAL
    
    # Handle both int IDs and string names
    if isinstance(role, str):
        role_name = role.upper()
        if role_name not in ROLES:
            raise ValueError(f"Unknown role: {role}. Available: {list(ROLES.keys())}")
        system_prompt = ROLES[role_name]
    else:
        if role < 0 or role >= len(ROLES):
            raise ValueError(f"Role ID must be 0-{len(ROLES)-1}")
        role_name = ROLE_IDS[role]
        system_prompt = ROLES[role_name]
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": q}
    ]
    
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages
    )
    
    content = response.choices[0].message.content
    print(f"[{role_name}]: {content}")
    return content


def list_roles():
    """Print all available roles with their IDs and descriptions."""
    print("Available Roles:")
    print("-" * 60)
    for i, (name, prompt) in enumerate(ROLES.items()):
        print(f"  {i}: {name}")
        print(f"      {prompt[:70]}...")
        print()


def get_role_prompt(role):
    """
    Get the system prompt for a given role.
    
    Args:
        role: Either an int ID or string name
    
    Returns:
        The system prompt string
    """
    if isinstance(role, str):
        role_name = role.upper()
        if role_name not in ROLES:
            raise ValueError(f"Unknown role: {role}. Available: {list(ROLES.keys())}")
        return ROLES[role_name]
    else:
        if role < 0 or role >= len(ROLES):
            raise ValueError(f"Role ID must be 0-{len(ROLES)-1}")
        return ROLES[ROLE_IDS[role]]


# Example usage
if __name__ == "__main__":
    print("Ex_C Role-Based Assistant")
    print("=" * 60)
    print()
    list_roles()
    print()
    print("Usage examples:")
    print('  ask_question("What is 2+2?", role=0)')
    print('  ask_question("What is 2+2?", role="PIRATE")')
    print('  ask_question("Tell me about Python", role="HAIKU")')
