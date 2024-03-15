# Funciones y Cloud storage

## Objetivos

- Aplicar los conocimientos y conceptos de aplicaciones serverless vistos en clase.
- Crear y publicar aplicaciones Cloud Function en GCP
- Crear y configurar buckets para el manejo de archivos

## Estructura de carpetas

En el proyecto encontrará tres carpetas principales:

- La carpeta `collections` en donde se encuentra la colección de Postman para poder realizar pruebas sobre las funciones publicadas
- La carpeta `crear` en donde se encuentra la implementación de la función que nos permitirá crear nuevos heroes 
- La carpeta `listar` en donde se encuentra la implementación de la función que nos dará la lista de los identificadores de héroes 
- La carpeta `detalle` en donde se encuentra la implementación de la función que nos permite ver la información de un héroe especifico de acuerdo a un identificador 

## Creación del bucket de almacenamiento

Para crear el bucket de almacenamiento, debe ejecutar el siguiente comando:

```console
gsutil mb -p <id_proyecto> -c standard -l us-central1 -b on gs://<nombre_booket>
```

Debe tener presente que el nombre debe ser único entre todas las cuentas de Google Cloud.


## Publicacion de la funciones 

Debe tener presente que las funciones se conectarán al Cloud Storage previamente creado. Para ello se configurará una variable de entorno con el nombre del bucket. Es importante que remplace el nombre en el comando antes de publicarlo.

### Crear

Para poder publicar la función, debe abrir una consola de comandos en la ubicación donde descargamos el repositorio. Posteriormente, debe ejecutar los sigioentes comandos:

```console
cd crear
gcloud functions deploy funcion-heroes-storage-crear --entry-point crear_heroe --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1 --set-env-vars BUCKETNAME=<nombre_bucket>
cd ..
```

En la consola deberá observar un mensaje de confirmación de creación de la función

### Listar

Para poder publicar la función, debe abrir una consola de comandos en la ubicación donde descargamos el repositorio. Posteriormente, debe ejecutar los sigioentes comandos:

```console
cd listar
gcloud functions deploy funcion-heroes-storage-listar --entry-point listar_heroes --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1 --set-env-vars BUCKETNAME=<nombre_bucket>
cd ..
```

En la consola deberá observar un mensaje de confirmación de creación de la función

### Detalle

Para poder publicar la función, debe abrir una consola de comandos en la ubicación donde descargamos el repositorio. Posteriormente, debe ejecutar los sigioentes comandos:

```console
cd detalle
gcloud functions deploy funcion-heroes-storage-detalle --entry-point detalle_heroe --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1 --set-env-vars BUCKETNAME=<nombre_bucket>
cd ..
```

En la consola deberá observar un mensaje de confirmación de creación de la función