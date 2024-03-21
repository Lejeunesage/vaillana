# generate_hero_content.py

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

# Assurez-vous que le dossier "hero" existe
os.makedirs("hero", exist_ok=True)

def save_content_to_file(content, filename):
    # Sauvegarder le contenu dans un fichier dans le dossier "hero"
    with open(os.path.join("hero", filename), "w") as file:
        file.write(content)

def generate_hero_html():
    # Générer le contenu HTML de la section héros avec l'IA
    prompt = "Générer le contenu HTML de la section héros avec le titre '{siteName}' et le sous-titre '{siteDescription}'."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text.strip()

def generate_hero_css():
    # Générer le contenu CSS de la section héros avec l'IA
    prompt = "Générer le contenu CSS pour la section héros du site '{siteName}'."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def generate_hero_js():
    # Générer le contenu JavaScript de la section héros avec l'IA
    prompt = "Générer le contenu JavaScript pour la section héros du site '{siteName}'."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def generate_and_save_hero_files():
    # Générer et sauvegarder les fichiers HTML, CSS et JavaScript de la section héros
    hero_html = generate_hero_html()
    hero_css = generate_hero_css()
    hero_js = generate_hero_js()

    save_content_to_file(hero_html, "index.html")
    save_content_to_file(hero_css, "styles.css")
    save_content_to_file(hero_js, "script.js")
