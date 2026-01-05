<div align="center">
  <img src="https://www.eii.ulpgc.es/sites/default/files/eii-acron-mod.png"
      alt="Logo ULPGC"
      width="400"
      style="margin-bottom: 10px;"
   >
</div>

<h1 align="center">Trabajo de Curso - Memorizador (Simón dice)</h1>

<div align="center" style="font-family: 'Segoe UI', sans-serif; line-height: 1.6; margin-top: 30px;">
  <h2 style="font-size: 28px; margin-bottom: 10px;">
    Titulación: Grado en Ingeniería Informática
  </h2>
  <h3 style="font-size: 24px; margin-bottom: 10px;">
    Visión por Computador
  </h3>
</div>

**Autores:**  
- Laura Herrera Negrín  
- Dunia Suárez Rodríguez  
- Ayman Asbai Ghoudan  

<a name="trabajo"></a>
## Breve Descripción
Este proyecto implementa una versión moderna del clásico juego "Simón Dice" utilizando **Visión Artificial (Computer Vision)** y **Machine Learning**. El sistema reconoce gestos de la mano y posturas corporales en tiempo real a través de la webcam.

### Dinámica del Juego
1.  **Secuencia:** El sistema genera una secuencia de gestos.
2.  **Réplica:** El jugador debe repetir la secuencia frente a la cámara.
3.  **Posible trampa:** El sistema intentará engañar al jugador en ciertas ocasiones con un nombre distinto a "Simón". Si el jugador obedece a, por ejemplo, "Modesto dice", pierde.
4.  **Dificultad Incremental:** A medida que avanzan los niveles, la secuencia de gestos aumenta en longitud. Asimismo, el tiempo de realización de los mismos decrementará levemente.

## Arquitectura
El trabajo no dependerá de ninguna base de datos externa; se basará en un dataset propio cuya elaboración vendrá dada por el equipo, intentando así generar una gran batería de recursos con los que se pueda entrenar y ejecutar el proyecto de manera correcta.  

---
## Contenidos
- [Librerías utilizadas](#librerias)
- [Acceso directo a la memoria (redacta con LaTeX)]()
---
  
<a name="librerias"></a>
## Librerías utilizadas
[![NumPy](https://img.shields.io/badge/NumPy-%23013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)  
- Manipulación eficiente de arrays y operaciones matemáticas.  
- Soporte de cálculos matriciales y transformaciones de imágenes. 

[![OpenCV](https://img.shields.io/badge/OpenCV-%23127C71?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)  
- Procesamiento de imágenes y videos.  
- Lectura/escritura de videos, manipulación de frames, recorte de ROI, anotaciones gráficas.    

[![MediaPipe](https://img.shields.io/badge/MediaPipe-blue?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev/)
- Detección y seguimiento de manos, de rostro y del cuerpo mediante modelos preentrenados.
- Extracción de landmarks para análisis de gestos y control por visión artificial.  

[![scikit-learn](https://img.shields.io/badge/scikit--learn-orange?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
- Algoritmos de aprendizaje automático y de clasificación.
- Entrenamiento y evaluación de modelos para la toma de decisiones basada en datos.  

[![Matplotlib](https://img.shields.io/badge/Matplotlib-%2311557C?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
- Visualización de datos y resultados experimentales.
- Representación gráfica de señales, métricas y estadísticas del sistema.  

[![Pygame](https://img.shields.io/badge/Pygame-%232E8B57?style=for-the-badge&logo=pygame&logoColor=white)](https://www.pygame.org/)
- Desarrollo de interfaces gráficas y aplicaciones interactivas.
- Gestión de eventos, ventanas y elementos multimedia en tiempo real.

[![SoundDevice](https://img.shields.io/badge/SoundDevice-%234B8BBE?style=for-the-badge&logo=python&logoColor=white)](https://python-sounddevice.readthedocs.io/)
- Captura y reproducción de audio en tiempo real.
- Entrada de micrófono para control por voz o análisis sonoro.

[![pyttsx3](https://img.shields.io/badge/pyttsx3-%23800080?style=for-the-badge&logo=python&logoColor=white)](https://pyttsx3.readthedocs.io/)
- Conversión de texto a voz sin conexión a internet.
- Generación de feedback sonoro y mensajes descritos para el usuario.

[![Pillow](https://img.shields.io/badge/Pillow-%23E34F26?style=for-the-badge&logo=python&logoColor=white)]()
- Carga, procesamiento y conversión de imágenes.
- Soporte para distintos formatos y manipulación básica de imágenes.

[![JAX](https://img.shields.io/badge/JAX-%23000000?style=for-the-badge&logo=jax&logoColor=white)](https://jax.readthedocs.io/)
- Computación numérica acelerada y diferenciación automática.
- Optimización de operaciones matemáticas avanzadas y cálculo eficiente.

[![JAXlib](https://img.shields.io/badge/JAXlib-%23663399?style=for-the-badge&logo=python&logoColor=white)](https://github.com/google/jax)
- Backend de bajo nivel para JAX.
- Ejecución eficiente en CPU/GPU de operaciones matemáticas.

[![ipykernel](https://img.shields.io/badge/ipykernel-purple?style=for-the-badge&logo=jupyter&logoColor=white)](https://ipython.org/)
- Integración del entorno Python con Jupyter Notebook.
- Facilita el desarrollo, pruebas y documentación interactiva del proyecto.

[![Time](https://img.shields.io/badge/Time-%23000000?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/time.html)  
- Medición de tiempos de inferencia y procesamiento frame a frame.  

--- 

<a name="entorno"></a>
### 🖥️ Preparación del entorno
Para garantizar la correcta ejecución del memorizador *Simón dice*, es necesario configurar un entorno de Python con las librerías requeridas. Este entorno incluye herramientas para procesamiento y análisis de información biométrica. Para ello, se creó un nuevo entorno de **Conda** con Python *3.11*:
```bash
conda create --name VC_Trabajo python=3.11
conda activate VC_Trabajo
pip install numpy==2.2.6 opencv-contrib-python==4.12.0.88 mediapipe==0.10.14 scikit-learn==1.7.2
pip install matplotlib==3.10.7 pygame==2.6.1 sounddevice==0.5.3 pyttsx3==2.99
pip install pillow jax jaxlib ipykernel
```
El motivo por el que se han fijado versiones para los diversos paquetes empleados en este proyecto, viene dada por la incompatibilidad entre los mismos que derivaba de manera directa en la imposibilidad de ejecución del código del juego.  

---

> Uso de la IA
- Explicación de algunas funciones
- Ayuda con la gestión de ciertas librerías
- Guía para mejorar la interfaz de usuario
- Estructura y redacción del Readme
