import os

from fastapi import HTTPException
import requests



MAL_CLIENT_ID = os.getenv("MAL_CLIENT_ID")
MAL_BASE_URL = "https://api.myanimelist.net/v2"
HEADERS = {"X-MAL-CLIENT-ID": "9d3de26134abfa6109b3e81d0cf3e3a7"}

async def animes_recente(page):
    response = requests.get(
        "https://api.myanimelist.net/v2/anime/season/2026/spring",
        headers=HEADERS,
        params={"limit": 7,
    "offset": (page - 1) * 7}
    )

    return response.json()
    

async def search_animes(search):
    response = requests.get(
        "https://api.myanimelist.net/v2/anime",
        headers=HEADERS,
        params={"limit": 5,
    "q": search}
    )

    return response.json()