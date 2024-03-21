# generate_nav_content.py

import os
import openai
from app_config import config

# Charger la configuration en fonction de l'environnement
env = "development"  # Changez ceci en "production" pour l'environnement de production
app_config = config[env]

# Récupérer la clé API OpenAI à partir de la configuration
openai_api_key = app_config.OPENAI_API_KEY

# Définir votre clé API OpenAI
openai.api_key = openai_api_key

# Assurez-vous que le dossier "nav" existe
os.makedirs("nav", exist_ok=True)

def save_content_to_file(content, filename):
    # Sauvegarder le contenu dans un fichier dans le dossier "nav"
    with open(os.path.join("nav", filename), "w") as file:
        file.write(content)

def generate_nav_html():
    # Générer le contenu HTML de la barre de navigation avec l'IA
    prompt = "Générer le contenu HTML de la barre de navigation pour le site '{siteName}' avec les liens suivants : \n"
    prompt += "- Accueil\n"
    prompt += "- À propos\n"
    # Ajoutez d'autres liens selon vos besoins

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text.strip()

def generate_nav_css():
    # Générer le contenu CSS de la barre de navigation avec l'IA
    prompt = "Générer le contenu CSS pour la barre de navigation du site '{siteName}'."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def generate_nav_js():
    # Générer le contenu JavaScript de la barre de navigation avec l'IA
    prompt = "Générer le contenu JavaScript pour la barre de navigation du site '{siteName}'."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def generate_and_save_nav_files():
    # Générer et sauvegarder les fichiers HTML, CSS et JavaScript de la barre de navigation
    nav_html = generate_nav_html()
    nav_css = generate_nav_css()
    nav_js = generate_nav_js()

    save_content_to_file(nav_html, "index.html")
    save_content_to_file(nav_css, "styles.css")
    save_content_to_file(nav_js, "script.js")
