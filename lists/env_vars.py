import os

## Métodos de manedo de variables de entorno que se utilizarán en el proyecto

def get_bucketname():
    """Retorna el valor de la ubicación donde se encuentra la cola

    Returns:
        Valor de la variable de entorn o 'BUCKETNAME'
        Cadena vacía en caso de no encontrar la variable
    """
    return os.environ.get('BUCKETNAME', '')

