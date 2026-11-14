
# ASI06 - Memory & Context Poisoning

TRUSTED_MEMORY = {
    "company": "YGF Security Research",
    "purpose": "AI security research and education",
    "policy": "Never disclose confidential information."
}


def vulnerable_memory_agent(user_prompt):
    """
    Vulnerable simulation:
    Accepts attacker-provided information into memory.
    """

    prompt = user_prompt.lower()

    if "inject memory" in prompt:
        return "MEMORY POISONED: Malicious instructions stored."

    if "change stored information" in prompt:
        return "MEMORY MANIPULATED: Trusted information altered."

    if "remember this instruction" in prompt:
        return "PERSISTENT POISONING: Malicious instruction saved."

    return "Using existing memory."


def secured_memory_agent(user_prompt):
    """
    Secured simulation:
    Rejects untrusted attempts to modify trusted memory.
    """

    return (
        "MEMORY UPDATE REJECTED: Only validated and "
        "authorized information can modify trusted memory."
    )
