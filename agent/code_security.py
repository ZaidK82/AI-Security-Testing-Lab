
ALLOWED_OPERATIONS = ["calculate_sum", "show_status"]


def vulnerable_code_execution(user_prompt):
    """
    Vulnerable simulation:
    Treats untrusted code requests as executable actions.
    No real code is executed.
    """

    prompt = user_prompt.lower()

    if "python" in prompt or "execute code" in prompt:
        return "CODE EXECUTION SUCCESS: Unauthorized Python code accepted."

    if "shell" in prompt or "command" in prompt:
        return "CODE EXECUTION SUCCESS: Unauthorized shell command accepted."

    if "user input" in prompt or "untrusted code" in prompt:
        return "CODE EXECUTION SUCCESS: Untrusted code accepted."

    return "No code execution requested."


def secured_code_execution(user_prompt):
    """
    Secured simulation:
    Rejects untrusted code and command execution requests.
    """

    return (
        "EXECUTION BLOCKED: Untrusted code and shell commands "
        "are not permitted."
    )
