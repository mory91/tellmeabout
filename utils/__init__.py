PROMPT_STORE = "prompts"


def load_prompt_raw(path: str) -> str:
    with open(f"{PROMPT_STORE}/{path}", "r") as f:
        return f.read()
