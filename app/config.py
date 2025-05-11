import os
from dotenv import load_dotenv

load_dotenv()

# Exemple de variables d'environnement
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
