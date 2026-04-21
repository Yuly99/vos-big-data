# Paso a paso en AWS

## 1. Bucket en S3
Se creó o utilizó un bucket en Amazon S3 para almacenar datasets y resultados.

## 2. Instancia EC2
Se utilizó una instancia EC2 con Ubuntu para ejecutar el procesamiento.

## 3. Configuración del entorno
En la instancia se instalaron herramientas como:
- Python
- Java
- Spark
- PySpark
- AWS CLI

## 4. Subida de archivos
Los datasets se subieron al bucket usando AWS CLI.

Ejemplo:
```bash
aws s3 cp archivo.csv s3://bigdata-smartphones-yuly/
