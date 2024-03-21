# app/controllers/zip_controller.py

import os
import shutil
import zipfile
from fastapi import APIRouter
from starlette.responses import FileResponse


router = APIRouter()

@router.get("/download-zip")
async def download_zip():
    try:
        # Crée un dossier projet avec un nom crypté
        project_dir = "project_folder"  # Remplacez par un nom de dossier approprié
        os.makedirs(project_dir, exist_ok=True)

        # Copie tous les dossiers des sections dans le dossier projet
        copy_section_folders(project_dir)

        # Compresse le dossier projet dans un fichier zip
        zip_file = zip_project_folder(project_dir)

        # Supprime le dossier projet après la compression
        shutil.rmtree(project_dir)

        # Télécharge le fichier zip
        return FileResponse(zip_file, media_type="application/zip", filename="site_content.zip")

    except Exception as e:
        return {"error": str(e)}

def copy_section_folders(project_dir):
    # Copie tous les dossiers des sections dans le dossier projet
    section_dirs = ["nav", "hero"]  # Ajoutez d'autres noms de dossiers de section si nécessaire
    for section_dir in section_dirs:
        shutil.copytree(section_dir, os.path.join(project_dir, section_dir))

def zip_project_folder(project_dir):
    # Compresse le dossier projet dans un fichier zip
    zip_file = f"{project_dir}.zip"
    with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(project_dir):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), project_dir))
    return zip_file
