# Importa las bibliotecas necesarias
from google_images_download import google_images_download
import cv2
import os
import numpy as np

# Función para hacer el fondo de una imagen transparente
def make_background_transparent(image, threshold=0):
    # Convierte la imagen a formato BGRA (BGR con canal de transparencia)
    rgba_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    
    # Identifica píxeles negros y los hace transparentes
    black_pixels = np.all(rgba_image[:, :, :3] <= threshold, axis=2)
    rgba_image[black_pixels, 3] = 0
    
    return rgba_image

# Función principal para descargar y transformar imágenes
def download_and_transform_images(query, total_images, download_path):
    # Crea una instancia del objeto google_images_download
    response = google_images_download.googleimagesdownload()
    
    # Define los argumentos para la descarga de imágenes
    arguments = {"keywords": query, "limit": total_images, "output_directory": download_path, "image_directory": query, "format": "jpg"}

    try:
        # Intenta descargar imágenes con los argumentos dados
        paths = response.download(arguments)
    except Exception as e:
        # Maneja errores durante la descarga
        print(f"Error al descargar imágenes: {e}")
        return
    
    # Crea una carpeta para almacenar las imágenes transformadas
    transformed_folder_path = os.path.join(download_path, query, 'dataTransformed')
    os.makedirs(transformed_folder_path, exist_ok=True)

    # Obtiene la ruta de la carpeta de imágenes originales
    original_folder_path = os.path.join(download_path, query)
    
    # Verifica si la carpeta de imágenes originales existe
    if not os.path.exists(original_folder_path):
        print("No se encontró la carpeta de descarga. Es posible que no se hayan descargado imágenes.")
        return

    # Itera sobre los archivos en la carpeta de imágenes originales
    for filename in os.listdir(original_folder_path):
        if filename.endswith('.jpg'):
            original_image_path = os.path.join(original_folder_path, filename)
            try:
                # Lee la imagen original
                original_image = cv2.imread(original_image_path)
                if original_image is None:
                    print(f"No se pudo cargar la imagen: {filename}")
                    continue

                # Redimensiona la imagen original a 200x200 y guarda la variante
                resized_original_image = cv2.resize(original_image, (200, 200))
                original_variant_filename = f"{os.path.splitext(filename)[0]}_{query}_original.png"
                resized_original_path = os.path.join(transformed_folder_path, original_variant_filename)
                cv2.imwrite(resized_original_path, resized_original_image)

                # Crea variantes  distintas de la imagen
                for i in range(10):
                    variant_image = resized_original_image.copy()
                    angle = np.random.randint(0, 360)
                    rotation_matrix = cv2.getRotationMatrix2D((150, 150), angle, 1)
                    variant_image = cv2.warpAffine(variant_image, rotation_matrix, (200, 200), borderMode=cv2.BORDER_CONSTANT)
                    variant_image = make_background_transparent(variant_image)

                    # Guarda la variante de la imagen
                    variant_filename = f"{os.path.splitext(filename)[0]}_{query}_variant_{i}.png"
                    variant_path = os.path.join(transformed_folder_path, variant_filename)
                    cv2.imwrite(variant_path, variant_image)
            except Exception as e:
                print(f"Error al procesar la imagen {filename}: {e}")
    print("Descarga y variaciones completadas.")

# Uso de la función con un ejemplo específico
download_and_transform_images('Flor_nochebuena', 50, 'C:/Users/carlo/Documents/TEC/Semestre 8/Inteligencia Artificial/ActividadesIA/ProyFin1Flores/dataSetFlores/nochebuena')
