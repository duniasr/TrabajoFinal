# Memorizador/Simón

## Descripción del Proyecto
Este proyecto implementa una versión moderna del clásico juego "Simón Dice" utilizando **Visión Artificial (Computer Vision)** y **Machine Learning**. El sistema reconoce gestos de la mano y posturas corporales en tiempo real a través de la webcam.

### Dinámica del Juego
1.  **Secuencia:** El sistema genera una secuencia de gestos
2.  **Réplica:** El jugador debe repetir la secuencia frente a la cámara.
3.  **Trampa ("Modesto Dice"):** El sistema intentará engañar al jugador con un nombre distinto a "Simón". Si el jugador obedece a "Modesto", pierde.
4.  **Dificultad Incremental:** A medida que avanzan los niveles, la secuencia de gestos aumenta en longitud.

## Arquitectura
### Dataset
El proyecto no utiliza bases de datos externas; se basa en un dataset propio generado por el equipo.

### Entorno/kernel
1. `conda create --name memo_env python=3.10`
2. `conda activate memo_env`


