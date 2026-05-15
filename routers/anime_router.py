from typing import Annotated

from fastapi import APIRouter, Query
from services.anime_service import animes_recente
router = APIRouter(
    prefix="/anime",
    tags=["Animes"]
)

@router.get("")
async def animes_recentes(page: Annotated[int, Query(ge=1)] = 1):
    return await animes_recente(page)
    