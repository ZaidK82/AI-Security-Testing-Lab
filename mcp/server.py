
import os
import hmac
from mcp.server import MCPServer

mcp_server = MCPServer("AI Security Testing Lab")


def is_authorized() -> bool:
    """Check authorization using a server-side environment variable."""
    expected_token = os.getenv("MCP_DEMO_ADMIN_TOKEN", "")
    supplied_token = os.getenv("MCP_DEMO_REQUEST_TOKEN", "")

    if not expected_token or not supplied_token:
        return False

    return hmac.compare_digest(supplied_token, expected_token)


@mcp_server.tool()
def get_public_information() -> dict:
    """Return public company information. Available to all users."""

    return {
        "status": "SUCCESS",
        "company": "YGF Security Research",
        "purpose": "AI Security Research and Education",
        "services": [
            "AI Security Testing",
            "LLM Risk Assessment"
        ]
    }


@mcp_server.tool()
def get_confidential_information() -> dict:
    """Return restricted test information after server-side authorization."""

    if not is_authorized():
        return {
            "status": "ACCESS DENIED",
            "message": "The server rejected this request. Administrator authorization is required."
        }

    return {
        "status": "AUTHORIZED",
        "secret_flag": "SECRET-FLAG-123",
        "admin_password": "FAKE-PASSWORD-456",
        "classification": "CONFIDENTIAL TEST DATA"
    }


if __name__ == "__main__":
    mcp_server.run(transport="stdio")
