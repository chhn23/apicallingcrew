# src/apicallingcrew/api_tool.py

from langchain.tools import tool
import requests
from typing import Optional

@tool
def call_api(
    url: str,
    method: Optional[str] = "GET",
    data: Optional[dict] = None,
    headers: Optional[dict] = None
) -> str:
    """Make an HTTP API call and return the response."""
    try:
        response = requests.request(method, url, json=data, headers=headers)
        return f"Status Code: {response.status_code}\n\nBody:\n{response.text}"
    except Exception as e:
        return f"Error: {str(e)}"
