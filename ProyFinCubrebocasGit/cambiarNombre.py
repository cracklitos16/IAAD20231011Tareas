# import os

# # Ruta al directorio que contiene las imágenes
# directorio = 'C:/Users/carlo/Documents/TEC/Semestre 8/Inteligencia Artificial/ActividadesIA/ProyFin2Cubrebocas/fotosNegativas'

# # Obtener la lista de archivos en el directorio
# archivos = os.listdir(directorio)

# # Iterar sobre cada archivo
# for archivo in archivos:
#     # Obtener la raíz del nombre del archivo y la extensión
#     nombre, extension = os.path.splitext(archivo)

#     # Verificar si el nombre del archivo tiene una letra mayúscula
#     if any(letra.isupper() for letra in nombre):
#         # Construir el nuevo nombre de archivo reemplazando la letra mayúscula por minúscula
#         nuevo_nombre = nombre.lower() + extension

#         # Crear la ruta completa del archivo original y el nuevo archivo
#         ruta_original = os.path.join(directorio, archivo)
#         ruta_nuevo = os.path.join(directorio, nuevo_nombre)

#         # Renombrar el archivo
#         os.rename(ruta_original, ruta_nuevo)
#         print(f'negativas {archivo} -> {nuevo_nombre}')
        
        
#***********************************************************************

import os

def renombrar_fotos(directorio, prefijo, extension):
    # Cambiar al directorio especificado
    os.chdir(directorio)

    # Obtener la lista de archivos en el directorio actual
    archivos = os.listdir()

    # Filtrar solo archivos con la extensión especificada
    fotos = [archivo for archivo in archivos if archivo.endswith(extension)]

    # Ordenar la lista de fotos
    fotos.sort()

    # Renombrar las fotos
    for i, foto in enumerate(fotos, start=1):
        nuevo_nombre = f"{prefijo}{i}.{extension}"
        os.rename(foto, nuevo_nombre)
        print(f'negativa {foto} a {nuevo_nombre}')

if __name__ == "__main__":
    # Especificar el directorio, prefijo y extensión de las fotos
    directorio_fotos = "C:/Users/carlo/Documents/TEC/Semestre 8/Inteligencia Artificial/ActividadesIA/ProyFin2Cubrebocas/fotosNegativas"
    prefijo = "negativaa"
    extension = "jpg"

    # Llamar a la función para renombrar las fotos
    renombrar_fotos(directorio_fotos, prefijo, extension)


