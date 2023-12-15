import os
import h5py
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# Directorio donde se encuentra el modelo original en Google Drive
modelo_original_ruta = '/content/drive/MyDrive/dataSetFlores/Test/modelFlores.h5'

# Cargar el modelo original desde el archivo HDF5
with h5py.File(modelo_original_ruta, 'r') as model_file:
    modelo_original = load_model(model_file)

# Directorio donde se encuentran las nuevas imágenes de prueba en Google Drive
directorio_base = '/content/drive/MyDrive/dataSetFlores/PruebaParaCalar'

# Diccionario de mapeo de clases a índices
mapeo_clases_a_indices = {'girasol': 0, 'nochebuena': 1, 'peonia': 2, 'rosa': 3, 'tulipan': 4}

# Invertir el diccionario para obtener un mapeo de índices a nombres de clases
mapeo_indices_a_clases = {v: k for k, v in mapeo_clases_a_indices.items()}

# Recorrer todas las subcarpetas y archivos en el directorio base
for subdir, _, files in os.walk(directorio_base):
    for image_file in files:
        # Cargar la imagen y preprocesarla con el tamaño correcto
        img_path = os.path.join(subdir, image_file)
        img = image.load_img(img_path, target_size=(200, 200))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalizar la imagen

        # Realizar la predicción con el modelo
        predicciones_original = modelo_original.predict(img_array)

        # Imprimir resultados
        print(f'Archivo: {img_path}')
        print(f'Flor predicha: {mapeo_indices_a_clases[np.argmax(predicciones_original[0])]}')
        print(f'Probabilidades:', predicciones_original[0])
        print('\n')

        # Graficar las métricas
        plt.bar(mapeo_clases_a_indices.keys(), predicciones_original[0])
        plt.title('Probabilidades por tipo de flor')
        plt.show()
