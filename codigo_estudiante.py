import numpy as np
from PIL import Image

def leer_imagen(ruta_imagen):

    # Abrir la imagen
    img = Image.open(ruta_imagen)

    return img

def obtener_info_imagen(img):

    # Obtener el número de canales
    modo = img.mode
    if modo == 'L':  # Escala de grises
        num_canales = 1
    elif modo == 'RGB':  # Imagen RGB
        num_canales = 3
    elif modo == 'RGBA':  # Imagen RGBA
        num_canales = 4
    else:
        num_canales = len(modo)  # Otros modos de imagen

    # Obtener las dimensiones de la imagen
    dimensiones = img.size  # Obtener (ancho, alto)

    return num_canales, dimensiones

def imagen_a_arreglo(img):

    # Convertir la imagen a un arreglo de NumPy
    arreglo = np.array(img)
    return arreglo

def estadisticas_intensidad(arreglo_img):

    # Calcular el promedio y la desviación estándar
    promedio = np.mean(arreglo_img)
    desviacion_estandar = np.std(arreglo_img)

    return promedio, desviacion_estandar

def estadisticas_por_canal(arreglo_img):

    # Verificar el número de dimensiones del arreglo
    if len(arreglo_img.shape) == 2:
        # Imagen de un solo canal
        promedio = np.mean(arreglo_img)
        desviacion_estandar = np.std(arreglo_img)
        resultados = {
            'Canal_1': {
                'Promedio': promedio,
                'Desviación Estándar': desviacion_estandar
            }
        }
    elif len(arreglo_img.shape) == 3:
        # Imagen de múltiples canales
        resultados = {}
        num_canales = arreglo_img.shape[2]

        for canal in range(num_canales):
            promedio = np.mean(arreglo_img[:, :, canal])
            desviacion_estandar = np.std(arreglo_img[:, :, canal])
            resultados[f'Canal_{canal+1}'] = {
                'Promedio': promedio,
                'Desviación Estándar': desviacion_estandar
            }
    else:
        raise ValueError("El arreglo de imagen debe tener 2 o 3 dimensiones.")

    return resultados

ruta_imagen = '/content/Fotografia-de-stock.png'


# Leer la imagen

img = leer_imagen(ruta_imagen)
display(img)

# Obtener información de la imagen
num_canales, dimensiones = obtener_info_imagen(img)
print("Número de canales:", num_canales)
print("Dimensiones:", dimensiones)

# Convertir la imagen a un arreglo de NumPy
arreglo_img = imagen_a_arreglo(img)

# Calcular estadísticas de intensidad general
promedio, desviacion_estandar = estadisticas_intensidad(arreglo_img)
print("Promedio de intensidad:", promedio)
print("Desviación estándar de intensidad:", desviacion_estandar)

# Calcular estadísticas por canal
estadisticas_canales = estadisticas_por_canal(arreglo_img)
print("Estadísticas por canal:", estadisticas_canales)
