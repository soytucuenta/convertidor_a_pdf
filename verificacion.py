import csv
import hashlib
from pathlib import Path
def escribir_csv(ruta_csv, datos, encabezados):

    with open(ruta_csv, 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
        escritor.writeheader()
        for fila in datos:
            escritor.writerow(fila)
    print(f'Datos escritos en {ruta_csv}')
    

def calcular_hash_archivo(ruta_archivo):

    sha256 = hashlib.sha256()
    with open(ruta_archivo, 'rb') as archivo:
        while True:
            datos = archivo.read(65536)  # Leer en bloques de 64KB
            if not datos:
                break
            sha256.update(datos)
    return sha256.hexdigest()

def catalogar_archivos_en_csv(carpeta, archivo_csv):

    carpeta = Path(carpeta).resolve()
    with open(archivo_csv, 'w', newline='', encoding='utf-8') as csvfile:
        campo_nombres = ['nombre_archivo', 'hash_sha256']
        escritor_csv = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        escritor_csv.writeheader()
        
        for archivo in carpeta.iterdir():
            if archivo.is_file():
                hash_archivo = calcular_hash_archivo(archivo)
                escritor_csv.writerow({
                    'nombre_archivo': archivo.name,
                    'hash_sha256': hash_archivo
                })
    print(f'Catalogación completada. Datos guardados en {archivo_csv}')

def buscar_archivo_en_lista(nombre_archivo, lista_archivos):
    ruta = Path(nombre_archivo)
    if not ruta.exists():
        try:
            hash_archivo = calcular_hash_archivo(ruta)
        except FileNotFoundError:
            return False
    else:
        hash_archivo = calcular_hash_archivo(ruta)

    flag = False
    for archivo in lista_archivos:
        if archivo.get('nombre_archivo') == ruta.name and archivo.get('hash_sha256') == hash_archivo:
            flag = True
    return flag


def cargar_lista_desde_csv(ruta_csv):

    lista_datos = []
    try:
        with open(ruta_csv, 'r', newline='', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            for fila in lector:
                lista_datos.append(fila)
    except FileNotFoundError:
        return []
    return lista_datos


