# ProyectoMLOPS

## Descripción:

Este proyecto de MLOps utiliza FastAPI para crear una API que ofrece acceso a tres conjuntos de datos de Steam: user_reviews, user_items y steam_games. Incluye limpieza de datos, 
análisis exploratorio de videojuegos de steam y varios endpoints para acceder a la información. Un endpoint contiene un sistema de recomendación de juegos basado en similitud de coseno. 
El deployment se realiza con Render.

## Características principales

- Análisis de datos de Steam
- API con FastAPI
- Sistema de recomendación de juegos
- Despliegue con Render

## Deployment de la API

Para llevar a cabo el despliegue de la API opté por una combinación de herramientas y técnicas que garantizaran un proceso eficiente y sin complicaciones.
En primer lugar, utilicé FastAPI como el marco principal para el desarrollo de la API. Para manejar las solicitudes entrantes, integré Uvicorn como el servidor ASGI. Para llevar la API en línea, me decidí por Render como plataforma de alojamiento y despliegue ya que ofrece una infraestructura confiable y escalable, lo que simplificó la implementación y la gestión de la API de gran manera.
Con el objetivo de optimizar la funcionalidad y el rendimiento de la API generé DataFrames precomputados para los endpoints solicitados. Esta forma de procesarlos me permitió reducir la carga computacional en tiempo de ejecución y proporcionar respuestas más rápidas.

## Endpoints

Para la realización de los endpoints hice primero una limpieza de los tres datasets. Luego utilizando Jupyter Notebooks, Python y librerías de Python realicé varias transformaciones cruzadas entre los tres datasets para poder extraer los datos necesarios de la mejor manera posible. En algunos casos tuve que reducir la cantidad de columnas porque al intentar procesar, mi computadora se quedaba procesando por horas y en algunos casos se quedaba completamente congelada. Luego, una vez obtenidos los datos correspondientes mediante funciones, almacené los resultados en dataframes que luego fueron utilizados por FastAPI para ser consumidos por la API.

## Sistema de recomendación

El sistema de recomendación que realicé opera sobre el dataframe de juegos y realiza las recomendaciones en base al género del mismo. El sistema toma como argumentos el título de un juego específico y un parámetro top_n, que especifica cuántos juegos similares se deben recomendar. Luego extrae los géneros de los juegos, calcula una matriz de similitud coseno entre los juegos basada en estas características, encuentra el índice del juego dado, calcula la similitud entre el juego dado y todos los otros juegos, ordena los juegos por su similitud al juego dado en orden descendente, selecciona los top_n juegos más similares excluyendo el propio juego dado, y finalmente, extrae los títulos de los juegos recomendados y los devuelve como una lista..


