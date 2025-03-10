import os
from dotenv import load_dotenv

# Carga las variables definidas en .env
load_dotenv()

# Variable sensible: API Key de Medisearch
MEDISEARCH_API_KEY = os.getenv("MEDISEARCH_API_KEY")
