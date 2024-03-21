# main.py

from fastapi import FastAPI
from app.controllers import site_controller, zip_controller
from app_config import config

# Charger la configuration en fonction de l'environnement
env = "development"  # Changez ceci en "production" pour l'environnement de production
app_config = config[env]

# Créer l'application FastAPI
app = FastAPI()

# Inclure les routes pour la génération du site et le téléchargement du fichier zip
app.include_router(site_controller.router)
app.include_router(zip_controller.router)

if __name__ == "__main__":
    import uvicorn

    # Démarrer le serveur FastAPI
    uvicorn.run(app, host="0.0.0.0", port=8000)
