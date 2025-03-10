from medisearch_client import MediSearchClient
from config import MEDISEARCH_API_KEY

class MedisearchService:
    def __init__(self):
        # Inicializamos el cliente usando la API key desde el .env
        self.client = MediSearchClient(api_key=MEDISEARCH_API_KEY)

    def search(self, query: str):
        # Enviamos la consulta a Medisearch
        responses = self.client.send_message(
            conversation=[query],
            conversation_id=f"search-{query}"  # Puedes mejorar la generación del ID según tus necesidades
        )
        # Procesamos y formateamos las respuestas
        results = []
        for response in responses:
            if response.get("event") == "llm_response":
                results.append({
                    "tipo": "llm_response",
                    "respuesta": response.get("data")
                })
            elif response.get("event") == "articles":
                results.append({
                    "tipo": "articles",
                    "articulos": response.get("data")
                })
        return results
