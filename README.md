# vos-big-data

## Descripción general
Este repositorio contiene la documentación y estructura base de un proyecto de Big Data implementado en AWS, en el cual se utilizaron servicios como Amazon EC2, Amazon S3, Python, PySpark y PostgreSQL.

## Objetivo
El objetivo del proyecto fue procesar y analizar datos de smartphones y ventas en un entorno de nube, aplicando conceptos de almacenamiento, transformación y análisis de datos.

## Tecnologías utilizadas
- Amazon EC2
- Amazon S3
- AWS CLI
- Python
- PySpark
- PostgreSQL

## Flujo general del proyecto
1. Preparación de datasets
2. Subida de archivos a Amazon S3
3. Procesamiento desde una instancia EC2
4. Ejecución de scripts en Python/PySpark
5. Generación de resultados
6. Almacenamiento final en S3 y organización de datos para análisis posterior

## Estructura del repositorio
- `docs/`: documentación del proyecto
- `src/`: scripts de procesamiento
- `results/`: resultados generados
- `images/`: evidencias visuales
- `data/`: muestra de datos

## Documentación disponible
- [Arquitectura](docs/arquitectura.md)
- [Paso a paso en AWS](docs/aws-paso-a-paso.md)
- [Análisis de datos](docs/analisis-datos.md)
- [Conclusiones](docs/conclusiones.md)

## Script principal
El archivo principal del proyecto es:

- `src/procesamiento.py`

Este script representa el flujo de:
- carga de datos
- limpieza
- unión de datasets
- análisis por marca
- análisis por ciudad
- análisis por año
- cálculo de promedios de especificaciones

## Estado actual
El repositorio contiene la estructura base, la documentación principal y el script inicial del proyecto.
