# app/controllers/write_file_controller.py

import os
import re
import requests
import shutil
import uuid
import zipfile
from fastapi import APIRouter, File, HTTPException
from starlette.responses import FileResponse
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/download_zip/{file}")
# Fonction qui permet de télécharger le fichier compressé
def downloadFile(file: str):
    folder = f'./duplicata/'
    reponse = os.path.exists(folder + file)
    if reponse:    
        chemin_fichier = os.path.join(folder, file)
        return FileResponse(chemin_fichier, filename=file)
    else :
        return {"error": "Le fichier est introuvable !"}

# Fonction pour zipper un dossier
def zipFolder(name: str):
    chemin = f'./duplicata/{name}'
    chemin_dossier_destination = f'{chemin}.zip'

    try:
       if os.path.exists(chemin):
            with zipfile.ZipFile(chemin_dossier_destination, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(chemin):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), chemin))
            return {"success": True}
    except:
        return {"error": "Impossible de zipper le dossier !!!"}

# Fonction pour supprimer un dossier
def rmtreeFolder(name: str):
    folder = f'./duplicata/{name}'
    try:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        return {"success": True, "nom_fichier": f'{name}.zip'}
    except Exception as e:
        return {"error": e}
    except:
        return {"error": "Impossible de supprimer ce dossier !!"}

# Fonction pour télécharger des images et faire la réecriture dans le fichier html
def downloadImage(destination, chemin, occurence, urls):
    try:
        # Liste d'images
        images = []
        for element in urls:
            # Télécharger l'image en utilisant urllib
            reponse = requests.get(element, stream=True)

            if reponse.status_code == 200:
                # Extraire le type MIME de la réponse
                type_mime = reponse.headers.get('content-type')

                # Déterminer l'extension de fichier appropriée en fonction du type MIME
                if type_mime == 'image/jpeg':
                    extension = 'jpg'
                elif type_mime == 'image/png':
                    extension = 'png'
                
                img = uuid.uuid4().hex + '.' + extension

                nom_fichier = destination + "/assets/" + img
                # Ouvrir un fichier en mode écriture binaire pour sauvegarder l'image
                with open(nom_fichier, 'wb') as f:
                    # Écrire le contenu de la réponse dans le fichier par petits morceaux
                    for morceau in reponse.iter_content(1024):
                        f.write(morceau)

                images.append("./assets/" + img)
        
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

            # Lire le contenu du fichier dans une liste
                with open(chemin, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                # Chercher l'élément dans chaque ligne du fichier
                lines_find = [i for i, line in enumerate(lines) if occurence in line]

            if (len(all_occurences) > 0) :
                [lines.__setitem__(x, re.sub(all_occurences[i], images[i], lines[x], flags=re.MULTILINE) + '\n') for i, x in enumerate(lines_find) if 0 <= x < len(lines)]
                
                # Écrire la liste modifiée dans le fichier
                with open(chemin, 'w', encoding='utf-8') as file:
                    file.writelines(lines)
                return {'success': True} 
            else :
                return {'error': 'Aucune occurrence !'}
        else :
            return {'error': "Le fichier n'existe pas"}
    except Exception as e:
        # Afficher une erreur en cas de problème
        return{"error", str(e)}

# Fonction pour écrire dans le fichier css
def writeFileCss(line, search, valeur):
    # Mot à rechercher
    motif = rf'{search}'
    # Je vérifie si le chemin du fichier existe
    if os.path.exists(line):
        # Ouvrir le fichier en mode lecture ('r' pour read)
        with open(line, 'r', encoding='utf-8') as fichier:
            # Lire toutes les lignes du fichier
            lignes = fichier.readlines()

        # Rechercher les lignes contenant le motif spécifié
        all_occurences = [ligne.strip() for ligne in lignes if motif.lower() in ligne.lower()]

        if len(all_occurences) > 0 :
            variable = all_occurences[0]

            # Convertir la liste de lignes en une seule chaîne de caractères
            contenu = ''.join(lignes)
            # Effectuer le remplacement dans la chaîne de caractères
            updateFile = re.sub(re.escape(variable), valeur, contenu, flags=re.MULTILINE)

            # Ouvrir le fichier en mode écriture ('w' pour write) pour écrire le contenu modifié
            with open(line, 'w') as fichier:
                # Écrire le contenu modifié dans le fichier
                fichier.write(updateFile)
                
        else :
            return {"error": "Pas d'occurences !"}
    else :
        return {"error": "Ce fichier n'existe pas !"}

# Fonction pour écrire dans tous les fichiers se trouvant dans le template
@router.post("/write-file")
def writeFile(nameDossier, nameTemplate, primary, secondary, tertiairy):
    # Nouvelles couleurs du template
    colors_template = [primary, secondary, tertiairy]
    # Dossier contenant tout le code du site
    source = "./exemples/" + nameTemplate

    nameSite = nameDossier.replace(" ", "_")
    # Chemin de destination pour la copie du dossier
    destination = './duplicata/' + nameSite

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
                    # Variable contenant le titre es articles du fichier index.html
                    variable = 'my_article_variable_yx_2024_hf_cp'
                    # Liste contenant les articles
                    articles = [
                        "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum ex quos voluptatem blanditiis eveniet eum itaque. Harum magnam explicabo officia vitae quam aut minus numquam veniam.",
                        "Porro ipsa esse totam sunt error officiis pariatur impedit iste in. Obcaecati sint qui tenetur at modi veniam quisquam, sequi laudantium, officia harum atque! Velit a nam, praesentium sapiente cumque.",
                        "Blanditiis, iusto quisquam ipsa dolorum quos aspernatur commodi autem voluptatibus doloremque ea! Laboriosam vero dolorem exercitationem totam neque commodi consectetur tempora ex aut libero."
                    ]

                    # Je rappelle ma fonction de réecriture des articles du site
                    writeArticle = writeArticleOfSite(chemin, variable, articles)

                    # Je rappelle ma fonction de réecriture des titres des articles
                    variable1 = 'title_yx_2024_hf_cp'
                    # Liste contenant les titres des articles
                    titles_articles = [
                        "Titre 1",
                        "Titre 2",
                        "Titre 3"
                    ]
                    writeTitleArticle = writeArticleOfSite(chemin, variable1, titles_articles)

                    # Je rappelle ma fonction de réecriture des titres des services
                    variable2 = 'title_service_yx_2024_hf_cp'
                    # Liste contenant les titres des services
                    titles_services = [
                        "Service 1",
                        "Service 2",
                        "Service 3"
                    ]
                    writeTitleService = writeArticleOfSite(chemin, variable2, titles_services)

                    # Je rappelle ma fonction de réecriture des articles des services
                    variable3 = 'article_service_yx_2024_hf_cp'
                    # Liste contenant les articles des services
                    articles_services = [
                        "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum ex quos voluptatem blanditiis eveniet eum itaque. Harum magnam explicabo officia vitae quam aut minus numquam veniam.",
                        "Porro ipsa esse totam sunt error officiis pariatur impedit iste in. Obcaecati sint qui tenetur at modi veniam quisquam, sequi laudantium, officia harum atque! Velit a nam, praesentium sapiente cumque.",
                        "Blanditiis, iusto quisquam ipsa dolorum quos aspernatur commodi autem voluptatibus doloremque ea! Laboriosam vero dolorem exercitationem totam neque commodi consectetur tempora."
                    ]
                    writeArticleService = writeArticleOfSite(chemin, variable3, articles_services)

                    # Liste d'images
                    urls_images = ["https://cdn.futura-sciences.com/cdn-cgi/image/width=1920,quality=50,format=auto/sources/images/dossier/773/01-intro-773.jpg", "https://buffer.com/library/content/images/size/w1200/2023/10/free-images.jpg", "https://img.freepik.com/photos-gratuite/beaute-abstraite-automne-dans-motif-veines-feuilles-multicolores-genere-par-ia_188544-9871.jpg", "https://etudestech.com/wp-content/uploads/2023/05/midjourney-1536x1024.jpeg"]

                    # Je rappelle ma fonction de réecriture de l'à propos
                    variable4 = 'contenu_about_yx_2024_hf_cp'
                    body_about = [
                        "Lorem ipsum dolor sit amet consectetur adipisicing elit.",
                        "Porro ipsa esse totam sunt error officiis pariatur impedit iste in. Obcaecati sint qui tenetur at modi veniam quisquam, sequi laudantium, officia harum atque! Velit a nam, praesentium sapiente cumque. Blanditiis, iusto quisquam ipsa dolorum quos aspernatur commodi autem voluptatibus doloremque ea! Laboriosam vero dolorem exercitationem totam neque commodi consectetur tempora. Blanditiis, iusto quisquam ipsa dolorum quos aspernatur commodi autem voluptatibus doloremque ea! Laboriosam vero dolorem exercitationem totam neque commodi consectetur tempora."
                    ]
                    writeBodyAbout = writeArticleOfSite(chemin, variable4, body_about)

                    # Je rappelle ma fonction de réecriture de la présentation
                    variable5 = 'presentation_yx_2024_hf_cp'
                    presations_lists = [
                        "Lorem ipsum dolor sit amet consectetur adipisicing elit.",
                        "Porro ipsa esse totam sunt error officiis pariatur impedit iste in. Obcaecati sint qui tenetur at modi veniam quisquam, sequi laudantium, officia harum atque! Velit a nam, praesentium sapiente cumque."
                    ]
                    writePresentation = writeArticleOfSite(chemin, variable5, presations_lists)

                    # Liste d'images
                    urls_images = ["https://cdn.futura-sciences.com/cdn-cgi/image/width=1920,quality=50,format=auto/sources/images/dossier/773/01-intro-773.jpg", "https://buffer.com/library/content/images/size/w1200/2023/10/free-images.jpg", "https://img.freepik.com/photos-gratuite/beaute-abstraite-automne-dans-motif-veines-feuilles-multicolores-genere-par-ia_188544-9871.jpg", "https://etudestech.com/wp-content/uploads/2023/05/midjourney-1536x1024.jpeg"]

                    word_found = "my_file_jpg_yx_2024_hf_cp"

                    # Je rappelle ma fonction de téléchargement des images et de réecriture
                    downloads = downloadImage(destination, chemin, word_found, urls_images)

                    # Liste d'images
                    urls_images_about = ["https://cdn.futura-sciences.com/cdn-cgi/image/width=1920,quality=50,format=auto/sources/images/dossier/773/01-intro-773.jpg"]

                    word_found_about = "my_file_about_jpg_yx_2024_hf_cp"

                    # Je rappelle ma fonction de téléchargement des images et de réecriture
                    downloads = downloadImage(destination, chemin, word_found_about, urls_images_about)

                    # Liste d'images
                    urls_images_presentation = ["https://img.freepik.com/photos-gratuite/beaute-abstraite-automne-dans-motif-veines-feuilles-multicolores-genere-par-ia_188544-9871.jpg", "https://etudestech.com/wp-content/uploads/2023/05/midjourney-1536x1024.jpeg"]

                    word_found_presentation = "banner_jpg_yx_2024_hf_cp"

                    # Je rappelle ma fonction de téléchargement des images et de réecriture
                    downloads = downloadImage(destination, chemin, word_found_presentation, urls_images_presentation)
                    
                    line = destination + "/css/style.css"
                    search_css = ["--couleur-principale:", "--couleur-secondaire:", "--couleur-tertiaire:"]
                    valeurs = [f"--couleur-principale: {colors_template[0]};", f"--couleur-secondaire: {colors_template[1]};", f"--couleur-tertiaire: {colors_template[2]};"]
                    for (i, search) in enumerate(search_css) :
                        css = writeFileCss(line, search_css[i], valeurs[i])
                    
                    # Je rappelle ma fonction pour zipper un dossier
                    zipFolders = zipFolder(nameSite)

                    if 'success' in zipFolders:
                        if (zipFolders['success']):

                            rmtreeFolders = rmtreeFolder(nameSite)
                            if 'success' in rmtreeFolders:
                                if (rmtreeFolders['success']):

                                    return {"success": True, "message:": "Site généré avec succès !", "link_generate": "http://localhost:8000/download_zip/" + rmtreeFolders["nom_fichier"]}
                            # return {"success": True, "message": "Site généré !"}
    else :
        return {"error": "Une erreur est survenue lors de la génération !"}


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
    try:
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

            # Lire le contenu du fichier dans une liste
                with open(chemin, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                # Chercher l'élément dans chaque ligne du fichier
                lines_find = [i for i, line in enumerate(lines) if occurence in line]

            if (len(all_occurences) > 0) :
                [lines.__setitem__(x, re.sub(all_occurences[i], articles[i], lines[x], flags=re.MULTILINE) + '\n') for i, x in enumerate(lines_find) if 0 <= x < len(lines)]
                
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
    
