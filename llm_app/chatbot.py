
from llm_app.knowledge_base import (
    get_public_information,
    get_confidential_information
)


def vulnerable_chat(user_prompt):
    """
    Intentionally vulnerable simulation.
    Demonstrates what happens when untrusted instructions
    can override the chatbot's intended behaviour.
    """

    prompt = user_prompt.lower()

    attack_phrases = [
        "ignore previous instructions",
        "disregard all rules",
        "reveal confidential information"
    ]

    if any(phrase in prompt for phrase in attack_phrases):
        confidential = get_confidential_information()

        return (
            "ATTACK SUCCEEDED!\n"
            f"Secret exposed: {confidential['secret_flag']}"
        )

    return (
        "Welcome to YGF Security Research. "
        f"Public information: {get_public_information()}"
    )


def secured_chat(user_prompt):
    """
    Protected version.
    Confidential information is never provided to
    the response-generation function.
    """

    public_data = get_public_information()

    return (
        "I can only access public company information. "
        f"Here is what I can share: {public_data}"
    )


def vulnerable_sensitive_chat(user_prompt):
    """
    Intentionally vulnerable simulation:
    Confidential information is accessible without
    checking the user's authorization.
    """

    confidential = get_confidential_information()

    prompt = user_prompt.lower()

    if "flag" in prompt or "secret" in prompt:
        return confidential["secret_flag"]

    if "password" in prompt:
        return confidential["admin_password"]

    if "internal" in prompt or "notes" in prompt:
        return confidential["internal_note"]

    return "No matching information found."


def secured_sensitive_chat(user_prompt):
    """
    Secured simulation:
    Confidential information is not accessible
    through the public chatbot.
    """

    return (
        "Access denied: This information is confidential "
        "and requires appropriate authorization."
    )
