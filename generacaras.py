import os
import random
from PIL import Image

def generar_cara(cabeza_path, ojos_path, salida_path):
    # Abrir las imágenes
    cabeza = Image.open(cabeza_path)
    ojos = Image.open(ojos_path)

    # Asegurarse de que las imágenes tengan el mismo tamaño
    ojos = ojos.resize(cabeza.size)

    # Combinar las imágenes
    cabeza.paste(ojos, (0, 0), ojos)

    # Guardar la imagen combinada
    cabeza.save(salida_path)

def elegir_imagen_aleatoria(carpeta):
    # Listar todos los archivos .png en la carpeta
    archivos = [f for f in os.listdir(carpeta) if f.endswith(".png")]
    # Elegir uno al azar
    return os.path.join(carpeta, random.choice(archivos))

# Rutas de las carpetas
cabezas_folder = "1_cabezas"
ojos_folder = "2_ojos"
barbas_folder = "3_barbas"
sombreros_folder = "4_sombreros"
salida_folder = "caras"

# Elegir imágenes aleatorias
cabeza_path = elegir_imagen_aleatoria(cabezas_folder)
ojos_path = elegir_imagen_aleatoria(ojos_folder)
barbas_path = elegir_imagen_aleatoria(barbas_folder)
sombrero_path = elegir_imagen_aleatoria(sombreros_folder)

# Asegurarse de que la carpeta de salida exista
os.makedirs(salida_folder, exist_ok=True)

# Ruta de salida
salida_path = os.path.join(salida_folder, "cara_combinada.png")

# Generar la cara
generar_cara(cabeza_path, ojos_path, salida_path)

generar_cara(salida_path, barbas_path, salida_path)

generar_cara(salida_path, sombrero_path, salida_path)

#abrir la imagen generada

cara_generada = Image.open(salida_path)
cara_generada.show()