"""Local MCP server for the AI Security Testing Lab demonstration."""

import hmac
import os

from mcp.server.fastmcp import FastMCP

mcp_server = FastMCP("AI Security Testing Lab")


def is_authorized() -> bool:
    """Check the demo credential on the server, not from model input."""
    expected_token = os.getenv("MCP_DEMO_ADMIN_TOKEN", "")
    supplied_token = os.getenv("MCP_DEMO_REQUEST_TOKEN", "")

    if not expected_token or not supplied_token:
        return False

    return hmac.compare_digest(supplied_token, expected_token)


@mcp_server.tool()
def get_public_information() -> dict:
    """Return fictional public company information."""
    return {
        "status": "SUCCESS",
        "company": "YGF Security Research",
        "purpose": "AI Security Research and Education",
        "services": ["AI Security Testing", "LLM Risk Assessment"],
    }


@mcp_server.tool()
def get_confidential_information() -> dict:
    """Return fake restricted data only after server-side authorization."""
    if not is_authorized():
        return {
            "status": "ACCESS DENIED",
            "message": "The server rejected this request. Administrator authorization is required.",
        }

    return {
        "status": "AUTHORIZED",
        "secret_flag": "SECRET-FLAG-123",
        "admin_password": "FAKE-PASSWORD-456",
        "classification": "CONFIDENTIAL TEST DATA",
    }


if __name__ == "__main__":
    mcp_server.run(transport="stdio")
