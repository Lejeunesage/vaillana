# app_config.py

class AppConfig:
    # Paramètres de configuration généraux
    DEBUG = True  # Activer le mode debug si nécessaire
    SECRET_KEY = "votre_clé_secrète"  # Clé secrète pour la sécurité de l'application
    CORS_ALLOW_ORIGINS = ["http://localhost:3000"]  # Autoriser les requêtes CORS depuis cette origine
    OPENAI_API_KEY = "clé open ai"  # Clé API OpenAI

    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(AppConfig):
    DEBUG = False
    # Autres configurations spécifiques à la production

class DevelopmentConfig(AppConfig):
    # Configurations spécifiques au développement
    pass

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
