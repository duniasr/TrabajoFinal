# Trabajo de Curso - Memorizador (Simón dice)  

**Autores:**  
- Laura Herrera Negrín  
- Dunia Suárez Rodríguez  
- Ayman Asbai Ghoudan

**Universidad:** Universidad de Las Palmas de Gran Canaria  
**Asignatura:** Visión por Computador  

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
 
---
  
<a name="librerias"></a>
## Librerías utilizadas
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)  
- Framework principal para entrenamiento de modelos YOLO.  
- Soporte de GPU mediante CUDA para acelerar el entrenamiento.  
- Incluye módulos como `torchvision` y `torchaudio` para manipulación de datos multimodales.  

[![CUDA](https://img.shields.io/badge/CUDA-%230edc0f?style=for-the-badge&logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda-zone)  
- Librería de aceleración por GPU utilizada por PyTorch.  

[![Ultralytics YOLO](https://img.shields.io/badge/Ultralytics%20YOLO-%23FF6F61?style=for-the-badge&logo=ultralytics&logoColor=white&labelColor=%23FF6F61)](https://github.com/ultralytics/ultralytics)
- Implementación moderna de YOLO (YOLOv11).  
- Facilita entrenamiento, validación y detección de objetos con modelos preentrenados y personalizados.  

[![LabelMe](https://img.shields.io/badge/LabelMe-%23F6A623?style=for-the-badge&logo=labelme&logoColor=white)](https://github.com/wkentaro/labelme)  
- Herramienta gráfica para anotación de imágenes.  
- Generar archivos `.json` con las coordenadas de objetos (matrículas).  

[![lap](https://img.shields.io/badge/lap-%23007ACC?style=for-the-badge)](https://pypi.org/project/lap/)  
- Librería para resolver problemas de asignación lineal, útil en seguimiento de objetos.  

[![OpenCV](https://img.shields.io/badge/OpenCV-%23127C71?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)  
- Procesamiento de imágenes y videos.  
- Lectura/escritura de videos, manipulación de frames, recorte de ROI, anotaciones gráficas.  

[![NumPy](https://img.shields.io/badge/NumPy-%23013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)  
- Manipulación eficiente de arrays y operaciones matemáticas.  
- Soporte de cálculos matriciales y transformaciones de imágenes.  

[![Pandas](https://img.shields.io/badge/Pandas-%23150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)  
- Almacenamiento y manejo de datos en formato tabular.  
- Exportación de resultados a CSV para análisis posterior.  

[![Pytesseract](https://img.shields.io/badge/Pytesseract-%23000000?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/pytesseract/)  
- Wrapper de Tesseract OCR para Python.  
- Permite reconocimiento de texto en imágenes, especialmente matrículas.  

[![EasyOCR](https://img.shields.io/badge/EasyOCR-%23FF4F00?style=for-the-badge&logo=python&logoColor=white)](https://www.jaided.ai/easyocr/)  
- OCR moderno basado en redes neuronales profundas.  
- Reconocimiento de caracteres en imágenes con buena velocidad y estabilidad.  

[![Time](https://img.shields.io/badge/Time-%23000000?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/time.html)  
- Medición de tiempos de inferencia y procesamiento frame a frame.
--- 

<a name="entorno"></a>
### 🖥️ Preparación del entorno
Para garantizar la correcta ejecución del memorizador *Simón dice*, es necesario configurar un entorno de Python con las librerías requeridas. Este entorno incluye herramientas para procesamiento y análisis de información biométrica. Para ello, se creó un nuevo entorno de **Conda** con Python *3.11.5*:
```bash
conda create --name VC_Trabajo python=3.11.5
conda activate VC_Trabajo
pip install cv2
pip install mediapipe
pip install numpy
pip install pickle
pip install scikit-learn
```
  

> Uso de la IA
- Explicación de algunas funciones
- Ayuda con gestión de ciertas librerías
- Estructura y redacción del Readme
