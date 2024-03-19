# Structure du Projet

Ce projet utilise une architecture MVC modulaire avec FastAPI pour le backend et Vue.js pour le frontend. Voici une explication du rôle et de l'utilité de chaque fichier et dossier :

## Dossiers

### `app/`

- **`controllers/`** : Ce dossier contient les contrôleurs qui gèrent les requêtes HTTP. Chaque fichier dans ce dossier correspond à un contrôleur spécifique.
- **`models/`** : Ce dossier contient les modèles de données de l'application.
- **`services/`** : Ce dossier contient les services qui interagissent avec les modèles et fournissent une logique métier.

### `templates/`

- Ce dossier contient les fichiers de templates HTML pour le frontend. Les fichiers HTML générés seront placés ici.

## Fichiers

### `main.py`

- Ce fichier est le point d'entrée de l'application FastAPI. Il configure et lance le serveur.

### `app/controllers/prompt_controller.py`

- Ce fichier définit le contrôleur qui gère les requêtes liées à la récupération des informations via un prompt. Il contient une route POST `/prompt` qui attend les informations nécessaires à la génération du site.

### `app/controllers/generation_controller.py`

- Ce fichier définit le contrôleur qui gère les requêtes liées à la génération des sections du site. Il contient les routes et les fonctions pour générer les sections du site.

### `app/models/site_model.py`

- Ce fichier contient le modèle de données pour le site. Il définit la structure des données nécessaires à la génération du site.

### `app/services/site_generation_service.py`

- Ce fichier contient le service qui génère le site à partir des données fournies. Il contient la logique métier pour la génération du site.

