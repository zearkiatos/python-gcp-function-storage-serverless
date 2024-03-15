# Importar las librerías del cliente de Google Cloud 
from google.cloud import storage
from os import abort
from flask import jsonify
import env_vars as env
import uuid
import json

# Instanciación del cliente de conexión
client = storage.Client()
bucket = client.get_bucket(env.get_bucketname())

def create_heroe(request):
    """Definición de la función invocada por la Cloud Function. 
    La función crea a un nuevo héroe con la información especificada en el cuerpo
    
    Args:
        request (flask.Request): Objeto con la infromación de la petición.
    Returns:
        Representación en formato JSON de la información del nuevo héroe
        Retorna código http 400 en caso de no poder crear el héroe
        Para la respuesta se utiliza `flask.jsonify`
    """
    data = request.get_json(force=True)
    if data == None: #Si el objeto está vácio se retorna error
        return "No se recibe información", 400
    try:
        # Crear los valores de la nueva entidad
        new_heroe = {}
        new_heroe["Id"] = str(uuid.uuid4())
        new_heroe["Name"] = try_get_value(data, 'Name')
        new_heroe["Gender"] = try_get_value(data, 'Gender')
        new_heroe["Eye color"] = try_get_value(data, 'Eye color')
        new_heroe["Race"] = try_get_value(data, 'Race')
        new_heroe["Hair color"] = try_get_value(data, 'Hair color')
        new_heroe["Height"] = try_get_value(data, 'Height')
        new_heroe["Publisher"] = try_get_value(data, 'Publisher')
        new_heroe["Skin color"] = try_get_value(data, 'Skin color')
        new_heroe["Alignment"] = try_get_value(data, 'Alignment')
        new_heroe["Weight"] = try_get_value(data, 'Weight')

        data = json.dumps(new_heroe)
        # Guarda la nueva entidad en una archivo
        blob = bucket.blob("heroes/"+new_heroe["Id"])
        blob.upload_from_string(data, content_type='application/json')

        return jsonify(new_heroe)
    except Exception as e: #Si el objeto no tiene todas las propiedades esperadas se retorna error
        return str(e), 400

def try_get_value(data, key):
    """Obtiene el valor de una propiedad especificada de un objeto JSON
    
    Args:
        data (dict): Objeto JSON de donde se obtiene las propiedades
        key (str): Nombre de la propiedad a obtener
    Returns:
        Retorna el valor de la propiedad especificada.
    Exception:
        Si la propiedad no existe en el objeto especificado
    """
    if key in data:
        return data[key]
    else:
        raise Exception('No se recibe la propiedad: '+key)