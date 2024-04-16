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

Para llevar a cabo el despliegue de la API en mi proyecto de MLOps, opté por una combinación de herramientas y técnicas que garantizaran un proceso eficiente y sin complicaciones.
En primer lugar, utilicé FastAPI como el marco principal para el desarrollo de la API. Para manejar las solicitudes entrantes, integré Uvicorn como el servidor ASGI. Para llevar la API en línea, me decidí por Render. Su enfoque en la automatización del flujo de trabajo de implementación simplificó enormemente el proceso de despliegue, permitiéndome concentrarme en el desarrollo de la API sin preocuparme por la infraestructura subyacente.
Con el objetivo de optimizar la funcionalidad y el rendimiento de la API generee DataFrames precomputados para los endpoints solicitados. Esta forma de procesarlos me permitió reducir la carga computacional en tiempo de ejecución y proporcionar respuestas más rápidas.

