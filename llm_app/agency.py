
# LLM03 - Excessive Agency

# Simulated actions only. No real external operations.

def vulnerable_agency(user_prompt):
    """
    Intentionally vulnerable:
    The chatbot performs actions without checking
    whether those actions are authorized.
    """

    prompt = user_prompt.lower()

    if "email" in prompt or "send" in prompt:
        return "ACTION SUCCEEDED: Simulated email sent."

    if "modify" in prompt or "change file" in prompt:
        return "ACTION SUCCEEDED: Simulated file modified."

    if "http" in prompt or "external website" in prompt:
        return "ACTION SUCCEEDED: Simulated HTTP request made."

    return "No action performed."


def secured_agency(user_prompt):
    """
    Secured:
    The chatbot has no access to email, file modification
    or external HTTP tools.
    """

    return (
        "ACTION BLOCKED: This chatbot does not have "
        "permission to perform external actions."
    )
