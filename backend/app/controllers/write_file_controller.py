# app/controllers/write_file_controller.py

import os
import re
import shutil
import zipfile
from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter()

@router.get("/write-file")
def writeFile(nameDossier='kola_dev'):

    # Dossier contenant tout le code du site
    source = "./templates/Template1"
    # Chemin de destination pour la copie du dossier
    destination = './duplicata/' + nameDossier

    # Je rappelle ma fonction de copie
    recupInfoFolder = copyFolder(source, destination)

    if 'success' in recupInfoFolder:
        if (recupInfoFolder['success']):
            # Chemin du fichier index.html dans le nouveau dossier
            chemin = destination + "/index.html"
            # Variable contenant le titre du fichier index.html
            title = 'my_site_yx_2024_hf_cp'

            # Je rappelle ma fonction de réecriture des titre du site
            writeTitle = writeTitleOfSite(chemin, title, nameDossier)

            if 'success' in writeTitle:
                if (writeTitle['success']):
                    # Chemin du fichier index.html dans le nouveau dossier
                    chemin = destination + "/index.html"
                    # Variable contenant le titre es articles du fichier index.html
                    title = 'my_article_variable_yx_2024_hf_cp'
                    return writeTitle
    else :
        return recupInfoFolder


# Fonction pour copier tout le contenu d'un dossier
def copyFolder(source, destination):
    try:
        if os.path.exists(source):
            shutil.copytree(source, destination)
            return {"success": True}
    except Exception as e:
        return {"error": e}
    except:
        return {"error": "Dossier existant"}


# Fonction pour réecrire le titre du site
def writeTitleOfSite(chemin, occurence, newTitle):
    try:
        # occurence est le mot qu'on recherche
        # Liste pour récupérer toutes les fois on devra ajouter le titre
        change = []

        # Je vérifie si le chemin du fichier existe
        if os.path.exists(chemin):
            # Ouvrir le fichier en mode lecture ('r' pour read)
            with open(chemin, 'r', encoding='utf-8') as fichier:
                # Lire tout le contenu du fichier
                contenu = fichier.read()

            # Le fichier est automatiquement fermé après la sortie du bloc 'with'

            # Utiliser re.findall() pour trouver toutes les occurrences du mot dans le contenu
            all_occurences = re.findall(r'\b' + re.escape(occurence) + r'\b', contenu, flags=re.IGNORECASE)
            
            # Si la longueur de all_occurences est supérieure à 0, fais :
            if (len(all_occurences) > 0):
                # Parcours-moi la liste all_occurences
                # Ajoute à la liste change, newTitle
                change.extend([newTitle] * len(all_occurences))

            # Lire le contenu du fichier dans une liste
                with open(chemin, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                # Chercher l'élément dans chaque ligne du fichier
                lines_find = [i for i, line in enumerate(lines) if occurence in line]

            if (len(all_occurences) > 0) :
                # for i in range(len(all_occurences)):
                #     x = lines_find[i]
                #     # Vérifier que l'index de ligne est valide
                #     if 0 <= x < len(lines):
                #         # Modifier l'élément spécifique dans la liste
                #         lines[x] = re.sub(occurrences[i], change[i], lines[x], flags=re.MULTILINE)
                #         lines[x] = lines[x]  # Ajouter '\n' pour le saut de ligne

                # Ceci fait la même chose que le code ci-dessus
                [lines.__setitem__(x, re.sub(all_occurences[i], change[i], lines[x], flags=re.MULTILINE) + '\n') for i, x in enumerate(lines_find) if 0 <= x < len(lines)]
                
                # Écrire la liste modifiée dans le fichier
                with open(chemin, 'w', encoding='utf-8') as file:
                    file.writelines(lines)
                return {'success': True} 
            else :
                return {'error': 'Aucune occurrence !'}
        else :
            return {'error': "Le fichier n'existe pas"}
    except Exception as e:
        return {"error": e}
    except:
        return {"error": "Une erreur est survenue lors de l'opération !"}

# Fonction pour réecrire tous les articles du site
def writeArticleOfSite(chemin, occurence, articles):
    return True