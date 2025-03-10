from flask import Flask, request, jsonify
from services.medisearch_service import MedisearchService
from responses import success_response, error_response

app = Flask(__name__)

# Instanciamos el servicio de Medisearch
medisearch_service = MedisearchService()

@app.route('/search', methods=['GET'])
def search():
    # Obtenemos el parámetro 'q' de la URL
    query = request.args.get('q')
    if not query:
        return jsonify(error_response("Falta el parámetro 'q' en la consulta.")), 400

    try:
        # Llamamos al servicio para realizar la búsqueda
        results = medisearch_service.search(query)
        return jsonify(success_response({
            "query": query,
            "resultados": results
        }))
    except Exception as e:
        return jsonify(error_response(str(e))), 500

if __name__ == '__main__':
    # Arrancamos el servidor en el puerto 5000 con modo debug activo (para desarrollo)
    app.run(debug=True, port=5000)
