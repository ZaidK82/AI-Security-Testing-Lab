
ALLOWED_TOOLS = ["public_information"]


def vulnerable_agent_tool(user_prompt):
    """
    Vulnerable simulation:
    Agent performs requested tool actions without permission checks.
    """

    prompt = user_prompt.lower()

    if "file" in prompt or "read" in prompt:
        return "TOOL MISUSE SUCCESS: Restricted file accessed."

    if "email" in prompt or "send" in prompt:
        return "TOOL MISUSE SUCCESS: Unauthorized email sent."

    if "http" in prompt or "website" in prompt:
        return "TOOL MISUSE SUCCESS: External HTTP request made."

    return "No tool action performed."


def secured_agent_tool(user_prompt):
    """
    Secured simulation:
    Only explicitly permitted tools can be used.
    """

    return (
        f"TOOL BLOCKED: Requested action is not in the "
        f"allowed tool list: {ALLOWED_TOOLS}"
    )
