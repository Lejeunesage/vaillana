# app/controllers/site_controller.py

from fastapi import APIRouter
from app.services.generate_nav_content import generate_and_save_nav_files
from app.services.generate_hero_content import generate_and_save_hero_files

router = APIRouter()

@router.post("/generate-site")
async def generate_site(data: dict):
    # Récupérer les données envoyées par le frontend
    nav_data = data.get("nav_data", {})
    hero_data = data.get("hero_data", {})

    # Rendre les données disponibles pour les méthodes de génération
    # Vous pouvez ensuite les utiliser dans les méthodes de génération de contenu
    # par exemple, generate_and_save_nav_files(nav_data)
    # et generate_and_save_hero_files(hero_data)

    # Appeler les méthodes principales de génération de contenu
    generate_and_save_nav_files(nav_data)
    generate_and_save_hero_files(hero_data)

    # Renvoyer une réponse pour indiquer que la génération a été effectuée avec succès
    return {"message": "Le contenu du site a été généré avec succès."}
