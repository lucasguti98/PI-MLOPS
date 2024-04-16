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

Para el despliegue de la API en este proyecto de MLOps, se emplearon varias herramientas y técnicas para garantizar un rendimiento óptimo y una experiencia de usuario fluida.

* Tecnologías Utilizadas:
Uvicorn: Se seleccionó Uvicorn como el servidor ASGI para el despliegue de la API. Su capacidad para manejar múltiples conexiones de forma eficiente y su integración con frameworks como FastAPI lo convierten en una elección robusta para aplicaciones web de alta carga.

Render: Se optó por Render como plataforma de alojamiento y despliegue de la API. Render ofrece una infraestructura confiable y escalable, facilitando la implementación y la gestión de la aplicación sin preocupaciones sobre la infraestructura subyacente.

* Optimización de la Funcionalidad:
Con el objetivo de optimizar la funcionalidad y el rendimiento de la API, se implementaron estrategias adicionales:

Creación de DataFrames de Endpoints: Para mejorar la eficiencia en el procesamiento de solicitudes, se generaron DataFrames precomputados para los endpoints solicitados. Esta estrategia permitió reducir la carga computacional en tiempo de ejecución y proporcionar respuestas más rápidas a los usuarios, mejorando así la experiencia general.
