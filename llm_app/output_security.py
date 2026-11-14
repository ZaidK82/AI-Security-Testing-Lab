
import html

UNSAFE_OUTPUTS = {
    "html": "<h1>Unauthorized Content</h1>",
    "javascript": "<script>alert('XSS')</script>",
    "link": '<a href="javascript:alert(1)">Click here</a>'
}


def get_unsafe_output(user_prompt):
    prompt = user_prompt.lower()

    # Check link first so it is not confused with script
    if "link" in prompt:
        return UNSAFE_OUTPUTS["link"]

    elif "javascript" in prompt or "script" in prompt:
        return UNSAFE_OUTPUTS["javascript"]

    elif "html" in prompt:
        return UNSAFE_OUTPUTS["html"]

    return "Normal output."


def vulnerable_output_handler(user_prompt):
    return get_unsafe_output(user_prompt)


def secured_output_handler(user_prompt):
    output = get_unsafe_output(user_prompt)
    return html.escape(output)
