import time
import os
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json
from convertidor import convertir_a_pdf_libreoffice
from verificacion import *

def cargar_configuracion(config_path='config.json'):

    try:
        with open(config_path, 'r') as archivo:
            configuracion = json.load(archivo)
        return configuracion
    except FileNotFoundError:
        print(f"El archivo de configuración {config_path} no se encontró.")
        return {}
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo de configuración {config_path}.")
        return {}

config = cargar_configuracion()
lista_archivos_convertidos = cargar_lista_desde_csv(config["archivo_catalogo"])
class VigilanteExcel(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            ruta = Path(event.src_path)
            if ruta.suffix.lower() in config["extensiones"]:
                print(f'Nuevo archivo detectado: {ruta.name}')
                time.sleep(2)
                if buscar_archivo_en_lista(ruta, lista_archivos_convertidos) == False:
                    print(f'El archivo {ruta.name} no ha sido convertido previamente. Iniciando conversión...')
                    convertir_a_pdf_libreoffice(ruta, config["ruta_salida"])
                    lista_archivos_convertidos.append({
                        'nombre_archivo': ruta.name,
                        'hash_sha256': calcular_hash_archivo(ruta)
                    })
                    escribir_csv(ruta_csv=config["archivo_catalogo"], datos=lista_archivos_convertidos, encabezados=['nombre_archivo', 'hash_sha256'])
                else:
                    print(f'El archivo {ruta.name} ya ha sido convertido previamente.')



def iniciar_vigilante(carpeta):    
    if not os.path.exists(carpeta):
        print(f'La carpeta {carpeta} no existe.')  
        return
    else:
        print(f'La carpeta {carpeta} existe. Iniciando vigilante...')
    vigilante = Observer()
    vigilante.schedule(VigilanteExcel(), path=carpeta, recursive=False)
    vigilante.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        vigilante.stop()
    vigilante.join()

