
import os
import glob
import uuid

# Ruta base del dataset de Kaggle
# DATASET_PATH = "src/dataset/gestos_cuerpo"
DATASET_PATH = "src/dataset/gestos_cara"

def renombrar_imagenes():
    print(f"Buscando carpetas en: {DATASET_PATH}")
    
    if not os.path.exists(DATASET_PATH):
        print(f"ERROR: La ruta {DATASET_PATH} no existe.")
        return

    # Listar carpetas dentro del path
    carpetas = [d for d in os.listdir(DATASET_PATH) if os.path.isdir(os.path.join(DATASET_PATH, d))]
    print(f"Carpetas encontradas: {carpetas}")

    for carpeta in carpetas:
        ruta_carpeta = os.path.join(DATASET_PATH, carpeta)
        
        # 1. Obtener todas las imágenes evitando DUPLICADOS
        archivos_unicos = set()
        for ext in ['*.jpg', '*.jpeg', '*.png']: 
            matches = glob.glob(os.path.join(ruta_carpeta, ext))
            for m in matches:
                archivos_unicos.add(os.path.abspath(m))
        
        # Convertir a lista y ordenar
        archivos = list(archivos_unicos)
        archivos.sort() # Ordenar por nombre actual para consistencia
        
        cant = len(archivos)
        print(f"  -> Procesando '{carpeta}': {cant} imágenes únicas.")
        
        temp_map = [] # [(ruta_temp, extension)]
        
        for ruta_antigua in archivos:
            folder, nombre_archivo = os.path.split(ruta_antigua)
            _, extension = os.path.splitext(nombre_archivo)
            
            # Nombre temporal único
            temp_name = f"temp_{uuid.uuid4()}{extension}"
            ruta_temp = os.path.join(folder, temp_name)
            
            try:
                os.rename(ruta_antigua, ruta_temp)
                temp_map.append((ruta_temp, extension))
            except OSError as e:
                print(f"    Error renombrando a temp {nombre_archivo}: {e}")

        # Renombrar imágenes secuencialmente
        for i, (ruta_temp, extension) in enumerate(temp_map, 1):
            if extension.lower() == '.jpeg': extension = '.jpg'
            
            nuevo_nombre = f"{carpeta}_Kaggle_{i}{extension.lower()}"
            ruta_final = os.path.join(ruta_carpeta, nuevo_nombre)
            
            try:
                os.rename(ruta_temp, ruta_final)
            except OSError as e:
                print(f"    Error renombrando final {nuevo_nombre}: {e}")
            
    print("\n--- COMPLETADO ---")

if __name__ == "__main__":
    print("Este script renombrará las imágenes al formato: Carpeta_Kaggle_N.jpg (1 hasta el total)")
    confirm = input(f"Ruta objetivo: {DATASET_PATH}\n¿Continuar? (s/n): ")
    if confirm.lower() == 's':
        renombrar_imagenes()
    else:
        print("Cancelado.")
