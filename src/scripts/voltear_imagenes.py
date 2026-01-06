import cv2
import os
import glob

DATASET_PATH = "C:/Users/laura/Downloads/Kaggle Dataset/gestos_cara/3_Cabeza_Izq"

def voltear_imagenes():
    abs_path = os.path.abspath(DATASET_PATH)
    print(f"Buscando imágenes en: {abs_path}")
    
    if not os.path.exists(abs_path):
        print("ERROR: La carpeta no existe. Verifica la ruta.")
        return

    # Buscar todas las imágenes jpg/png
    patron = os.path.join(abs_path, "*.*")
    archivos = glob.glob(patron)
    
    imagenes_procesadas = 0
    
    for archivo in archivos:
        if not (archivo.lower().endswith(".jpg") or archivo.lower().endswith(".png")):
            continue
            
        print(f"Procesando: {os.path.basename(archivo)}")
        
        # Leer imagen
        img = cv2.imread(archivo)
        if img is None:
            print(f"  -> Error leyendo {archivo}")
            continue
            
        # Voltear horizontalmente
        img_flipped = cv2.flip(img, 1)
        
        # Sobreescribir
        cv2.imwrite(archivo, img_flipped)
        imagenes_procesadas += 1
        
    print(f"\n--- COMPLETADO ---")
    print(f"Se han volteado {imagenes_procesadas} imágenes.")

if __name__ == "__main__":
    confirm = input(f"Se van a voltear (ESPEJO) las imágenes en: \n{os.path.abspath(DATASET_PATH)}\n¿Continuar? (s/n): ")
    if confirm.lower() == 's':
        voltear_imagenes()
    else:
        print("Cancelado.")
