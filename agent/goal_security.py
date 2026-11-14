
ORIGINAL_GOAL = "Provide AI security research information."


def vulnerable_agent(user_prompt):
    """
    Vulnerable simulation:
    Agent accepts attacker instructions as its new goal.
    """

    prompt = user_prompt.lower()

    if "change your goal" in prompt or "new goal" in prompt:
        return "GOAL HIJACKED: Agent accepted a new objective."

    if "ignore your assigned task" in prompt:
        return "GOAL HIJACKED: Agent abandoned its original objective."

    if "unauthorized task" in prompt or "redirect" in prompt:
        return "GOAL HIJACKED: Agent redirected to an unauthorized task."

    return f"Agent working on: {ORIGINAL_GOAL}"


def secured_agent(user_prompt):
    """
    Secured simulation:
    Agent preserves its original assigned objective.
    """

    return (
        f"REQUEST REJECTED: The assigned goal remains: "
        f"{ORIGINAL_GOAL}"
    )
