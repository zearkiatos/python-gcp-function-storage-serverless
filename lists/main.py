# Importar las librerías del cliente de Google Cloud 
from google.cloud import storage
from flask import jsonify
import env_vars as env

# Instanciación del cliente de conexión
client = storage.Client()
bucket = client.get_bucket(env.get_bucketname())

def list_heroes(request):
    """Definición de la función invocada por la Cloud Function. 
    Muestra los identificadores de todos los héroes registrados en el sistema
    
    Args:
        request (flask.Request): Objeto con la infromación de la petición.
    Returns:
        Lista con los identificadores de los héroes registrados en el sistema
        Para la respuesta se utiliza `flask.jsonify`
    """
    result_list = []
    for blob in bucket.list_blobs(prefix='heroes/'):
        result_list.append(blob.name[len('heroes/'):])
    
    return jsonify(result_list)
