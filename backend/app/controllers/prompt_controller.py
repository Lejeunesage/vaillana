from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.site_generation_service import generate_site

router = APIRouter()

class SiteInfo(BaseModel):
    title: str
    description: str
    # Ajoutez d'autres champs requis pour la génération du site

@router.post("/prompt", response_model=None)
async def prompt_for_site_info(site_info: SiteInfo):
    """
    Récupère les informations nécessaires à la génération du site via un prompt.
    """
    try:
        # Appelez le service pour générer le site avec les informations fournies
        await generate_site(site_info)
        return None
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
