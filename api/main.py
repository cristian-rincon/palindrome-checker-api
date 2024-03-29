"""Main module."""
from typing import Dict
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .models import PalindromeModel
from .utils import longest_palindrome

app = FastAPI()


@app.get("/")
async def home() -> RedirectResponse:
    """Root path, redirects to OpenAPI docs"""
    return RedirectResponse("/docs")


@app.get("/ping")
async def ping() -> Dict:
    """Healthcheck endpoint"""
    return {"message": "pong"}


@app.post("/palindrome", response_model=PalindromeModel)
async def longest_palindrome_of_text(paragraph: PalindromeModel) -> Dict[str, str]:
    """Returns the longest palindrome of the given text."""
    response = {"text": longest_palindrome(paragraph.text)}
    return response
