"""
Este script permite descargar imáges desde google o bing.
Descargar imágenes desde GOOGLE:
- Instalación:
No usar: pip install google_images_download
Algunas imágenes no se pueden descargar.
Repositorio Actualizado: 
pip install git+https://github.com/Joeclinton1/google-images-download.git
Limitación: 100 imágenes
Descargar imágenes con BING:
- Instalación:
pip install bing-image-downloader
Limitación: Al parecer no hay limites.
"""
#####################################
# Google
from google_images_download import google_images_download

#instantiate the class
response = google_images_download.googleimagesdownload()

busqueda = input("¿Qué imagen deseas descargar?: ")
cantidad = input("¿Cuántas imágenes?: ")

arguments = {"keywords":busqueda,
             "limit":cantidad,"print_urls":False}
paths = response.download(arguments)

#print complete paths to the downloaded images
print(paths)


#####################################
# Bing
#from bing_image_downloader import downloader
#downloader.download("monkey", limit=200,  output_dir='dataset', 
#                    adult_filter_off=True, force_replace=False, timeout=60)

#downloader.download("tiger", limit=200,  output_dir='dataset', 
#                   adult_filter_off=True, force_replace=False, timeout=60)
