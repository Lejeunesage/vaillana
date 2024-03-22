# app/controllers/write_file_controller.py

import os
import re
import requests
import shutil
import uuid
import zipfile
from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter()

@router.get("/download-image")
def downloadImage():
    try:
        url = "https://cdn.futura-sciences.com/cdn-cgi/image/width=1920,quality=50,format=auto/sources/images/dossier/773/01-intro-773.jpg"

        nom_fichier = './download_image/' + uuid.uuid4().hex + '.jpg'

        # Télécharger l'image en utilisant urllib
        reponse = requests.get(url, stream=True)

        if reponse.status_code == 200:
            # Ouvrir un fichier en mode écriture binaire pour sauvegarder l'image
            with open(nom_fichier, 'wb') as f:
                # Écrire le contenu de la réponse dans le fichier par petits morceaux
                for morceau in reponse.iter_content(1024):
                    f.write(morceau)
            return {"success": True}
        else:
            # Afficher un message si la requête échoue
            return {"error": "La requête a échoué !"}
    except Exception as e:
        # Afficher une erreur en cas de problème
        return{"error", str(e)}

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
                    # Variable contenant le titre es articles du fichier index.html
                    variable = 'my_article_variable_yx_2024_hf_cp'
                    # Liste contenant les articles
                    articles = [
                        "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum ex quos voluptatem blanditiis eveniet eum itaque. Harum magnam explicabo officia vitae quam aut minus numquam veniam facilis vero, sit, architecto incidunt, ad amet qui deserunt. Modi officiis, facilis recusandae eaque aperiam suscipit, tenetur cupiditate ipsa atque maiores dignissimos obcaecati quos eligendi perspiciatis. Quo blanditiis dicta quasi porro dolore dolorem nihil incidunt, quisquam eveniet labore, amet placeat earum modi. Harum nam eligendi, numquam facilis quibusdam quod sed voluptatem dolor.",
                        "Porro ipsa esse totam sunt error officiis pariatur impedit iste in. Obcaecati sint qui tenetur at modi veniam quisquam, sequi laudantium, officia harum atque! Velit a nam, praesentium sapiente cumque ab accusamus dolorem modi consequuntur, quam perferendis sunt incidunt ut! Dolorum minus iure unde! Omnis fuga iure quod, earum totam reprehenderit possimus saepe est tenetur qui error quasi veritatis eos repudiandae odio facere eligendi sequi maxime labore obcaecati quia esse velit quam. Qui dolorem quia voluptatibus cupiditate debitis nesciunt corrupti.",
                        "Libero praesentium explicabo autem beatae vero, magnam eos expedita numquam voluptates pariatur dolore neque sequi quos, porro iusto, rerum non iste quasi nemo similique tenetur dolorum a in quae? Saepe, amet mollitia? Amet, expedita cumque enim in quos veniam iure voluptas doloremque ipsum molestiae earum quam vitae ratione ipsam ipsa libero sapiente fuga nihil quo dicta molestias? Ipsum eveniet voluptates sint ex ut dolores, fugit eos, quod quisquam at saepe quibusdam magnam cumque consequuntur molestias possimus laudantium sapiente placeat. Sit, recusandae sunt nisi, omnis velit quidem necessitatibus voluptate non itaque laboriosam, magnam quasi fuga! Quidem, dolorum tempore repudiandae animi incidunt vero obcaecati fugiat fuga, aspernatur aperiam illum, voluptas accusamus id suscipit cupiditate modi nobis quisquam atque ad sit? Animi id consequatur neque, rerum blanditiis, itaque aspernatur iure minima accusamus praesentium officiis quas nisi harum voluptates molestiae tenetur ipsa possimus repellendus rem, hic maxime voluptatum illo. Corporis inventore sint, quas vel, laborum distinctio porro rerum placeat repellendus nostrum fugiat odio. Deserunt animi rem perspiciatis autem ipsam ut? Animi architecto molestias ab dolore, officia aut magni repudiandae minus, eum consequatur inventore aliquam aperiam sapiente hic ducimus eius reiciendis quis quam consectetur mollitia maiores fugit porro facilis? Ad consequatur quis beatae eum enim fugit, possimus nam ipsa dicta accusamus perferendis rerum iure, itaque architecto tempore dolorem recusandae totam exercitationem! Dolorum, reiciendis corrupti! Saepe veritatis ut deleniti laudantium eos voluptatum modi placeat deserunt natus laboriosam, non provident, beatae consectetur dignissimos officia dolores soluta. Exercitationem, dicta laudantium corporis numquam quasi id quibusdam veritatis architecto nisi nesciunt recusandae! Dignissimos, commodi. Nulla, veniam porro. Culpa itaque nesciunt dolorem hic illum repellat amet sapiente vitae doloremque corporis ipsam molestias, sequi nulla dolor quisquam suscipit voluptatum eos nihil natus maiores! Odio alias maiores atque, a, hic eligendi doloremque cupiditate adipisci autem earum velit fugit minima commodi, totam laboriosam tempora esse praesentium eum!",
                        "Blanditiis, iusto quisquam ipsa dolorum quos aspernatur commodi autem voluptatibus doloremque ea! Laboriosam vero dolorem exercitationem totam neque commodi consectetur tempora ex aut libero, alias facilis minus eveniet laborum, enim nihil temporibus voluptatem assumenda, quo dicta architecto magnam inventore obcaecati? Dolorum quaerat quos ad, ipsam asperiores beatae maiores sed? Earum reprehenderit aliquid obcaecati enim repellat? Accusamus sapiente laboriosam maxime veritatis nam soluta alias rem, harum in magnam iure minima nostrum vel ipsa. Est explicabo quo et nobis non accusamus nemo nesciunt amet, sit natus quam dolores! Voluptatibus quisquam porro cumque facilis pariatur earum harum quam velit aliquam eum illo recusandae accusamus alias minima repellendus nihil, tempora, maiores aut deleniti quas? Amet, tempora pariatur consequatur aliquid eum veniam, qui expedita dignissimos corrupti, saepe fugiat dicta ducimus quisquam aspernatur quaerat ipsa voluptate mollitia veritatis est rerum aut excepturi minima officia. Neque, cumque soluta! Sapiente unde debitis fugiat, numquam tenetur in voluptatum quia voluptas. Earum a, officiis suscipit praesentium veritatis eum iusto natus est, id eius illo, voluptatem recusandae ipsa. Possimus unde quia non omnis nihil! Ex culpa eum hic eaque reprehenderit iste ipsam. Atque facere sint repudiandae tempora maiores quisquam nobis dolor eaque explicabo laborum, quo perspiciatis, velit numquam ex consequuntur exercitationem dignissimos harum odio ad omnis officiis? Porro cumque voluptas ullam consequuntur necessitatibus soluta non, consectetur corporis? Quisquam accusantium praesentium quis totam laborum est earum esse, minus enim minima consectetur repellendus facilis tenetur commodi corrupti ducimus dolores ea quas iure nulla nihil saepe perferendis sunt?"
                    ]

                    # Je rappelle ma fonction de réecriture des articles du site
                    writeArticle = writeArticleOfSite(chemin, variable, articles)
                    return writeArticle
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
    
