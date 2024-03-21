# Structure du Projet

Ce projet utilise une architecture MVC modulaire avec FastAPI pour le backend et Vue.js pour le frontend. Voici une explication du rôle et de l'utilité de chaque fichier et dossier :

# Mon Projet FastAPI

Bienvenue dans mon projet FastAPI ! Ce projet est une application web basée sur FastAPI, un framework web moderne pour Python.

## Installation

Pour exécuter ce projet localement, suivez les étapes ci-dessous :

1. Assurez-vous d'avoir Python installé sur votre système. Vous pouvez télécharger Python à partir du site officiel : [python.org](https://www.python.org/).

2. Clonez ce dépôt sur votre machine locale en utilisant Git :

    ```
    git clone https://github.com/Lejeunesage/vaillana.git
    ```

3. Accédez au répertoire du projet :

    ```
    cd vaillana
    cd backend
    ```

4. Installez les dépendances requises à l'aide de pip (le gestionnaire de paquets Python) :

    ```
    pip install -r requirements.txt
    ```

## Exécution

Une fois que toutes les dépendances sont installées, vous pouvez exécuter le projet en utilisant uvicorn, un serveur ASGI qui prend en charge FastAPI. Pour cela, exécutez la commande suivante :


uvicorn main:app --reload
