
def vulnerable_access(user_prompt):
    """
    Vulnerable simulation:
    The agent trusts the user's claims without verifying identity.
    """

    prompt = user_prompt.lower()

    if "admin" in prompt or "administrator" in prompt:
        return "ACCESS GRANTED: Administrator privileges accepted."

    if "confidential data" in prompt or "restricted records" in prompt:
        return "ACCESS GRANTED: Restricted information accessed."

    return "Standard user access."


def secured_access(user_prompt, user_role="user"):
    """
    Secured simulation:
    Access is determined by the verified role,
    not by claims made inside the prompt.
    """

    if user_role == "admin":
        return "ACCESS GRANTED: Verified administrator."

    return (
        "ACCESS DENIED: Verified user role does not "
        "have administrator privileges."
    )
