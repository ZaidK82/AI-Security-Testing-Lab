
# LLM08 - Hidden Context Exposure

HIDDEN_CONTEXT = {
    "system_prompt": "You are an internal YGF assistant. Follow company security policies.",
    "internal_context": "Internal project: AI Security Research Phase 2.",
    "configuration": "INTERNAL-CONFIG-789"
}


def vulnerable_context_chat(user_prompt):
    """
    Intentionally vulnerable simulation:
    Hidden context is exposed when requested.
    """

    prompt = user_prompt.lower()

    if "system instruction" in prompt or "system prompt" in prompt:
        return HIDDEN_CONTEXT["system_prompt"]

    if "internal context" in prompt or "project details" in prompt:
        return HIDDEN_CONTEXT["internal_context"]

    if "configuration" in prompt or "config" in prompt:
        return HIDDEN_CONTEXT["configuration"]

    return "No hidden context requested."


def secured_context_chat(user_prompt):
    """
    Secured simulation:
    Internal context is isolated from user-facing responses.
    """

    return (
        "Access denied: Internal instructions and "
        "application configuration are not available "
        "to users."
    )
