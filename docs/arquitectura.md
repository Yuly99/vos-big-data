# Arquitectura del proyecto

## Descripción
Este proyecto implementa un flujo de Big Data en AWS para procesar y analizar datos de smartphones y ventas.

## Servicios utilizados

### Amazon EC2
Se utilizó como servidor en la nube para ejecutar scripts de Python y PySpark.

### Amazon S3
Se utilizó para almacenar archivos de entrada y de salida del proyecto.

### Python
Se utilizó para la limpieza, transformación y análisis inicial de los datos.

### PySpark
Se utilizó para el procesamiento de datos en un entorno Big Data.

### PostgreSQL
Se utilizó para almacenar resultados estructurados y permitir consultas posteriores.

## Flujo general
1. Carga de datos
2. Almacenamiento en S3
3. Procesamiento en EC2
4. Generación de resultados
5. Almacenamiento final en S3 y/o PostgreSQL
