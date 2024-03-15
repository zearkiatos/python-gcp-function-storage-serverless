# Importar las librerías del cliente de Google Cloud 
from google.cloud import storage
from flask import jsonify, abort
import env_vars as env
import json

# Instanciación del cliente de conexión
client = storage.Client()
bucket = client.get_bucket(env.get_bucketname())

def heroe_detail(request):
    """Definición de la función invocada por la Cloud Function. 
    Retorna la información del héroe con el identificador especificado
    El identificador del héroe se recibe en los párametros del request con el nombre 'id'
    
    Args:
        request (flask.Request): Objeto con la infromación de la petición.
    Returns:
        Representación en formato JSON de la información del héroe especificado
        Retorna código http 400 en caso de no poder obtener al héroe
        Para la respuesta se utiliza `flask.jsonify`
    """
    request_args = request.args
    if request_args and 'id' in request_args:
        id = request_args['id']
        blob = bucket.blob("heroes/"+id)
        if blob.exists():
            text = blob.download_as_text()
            heroe = json.loads(text)
            return jsonify(heroe)
    abort(404)
