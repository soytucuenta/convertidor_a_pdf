from vigilante import cargar_configuracion, iniciar_vigilante


carpeta = cargar_configuracion()["ruta_monitor"]
# cargar la carpeta y extensiones de archivos en config.json

iniciar_vigilante(carpeta)