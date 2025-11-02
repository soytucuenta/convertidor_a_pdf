import subprocess
import platform
from pathlib import Path

def convertir_a_pdf_libreoffice(ruta_excel, ruta_salida):
    

    """Convierte un archivo Excel a PDF usando LibreOffice en modo headless. Chequea si
        LibreOffice está instalado y disponible en el sistema.
    Args:
        ruta_excel (str): Ruta al archivo Excel.
        """
    ruta_excel = Path(ruta_excel).resolve()
    ruta_salida = Path(ruta_salida).resolve()

    if platform.system() == "Windows":
        comando = r"C:\Program Files\LibreOffice\program\soffice.exe"
    else:
        comando = "soffice"

    if not Path(comando).exists() and platform.system() == "Windows":
        comando = r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"

    if not Path(comando).exists() and platform.system() == "Windows":
        print("No se encontró LibreOffice. Asegurate de instalarlo o agregarlo al PATH.")
        return

    try:
        print(f"Convirtiendo {ruta_excel.name}  PDF...")
        subprocess.run([
            comando,
            "--headless",
            "--convert-to", "pdf",
            "--outdir", str(ruta_salida),
            str(ruta_excel)
        ], check=True)
        print(f'PDF creado en: {ruta_salida}')
    except subprocess.CalledProcessError as e:
        print(f"Error al convertir: {e}")
