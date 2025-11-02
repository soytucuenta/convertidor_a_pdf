# Conversor Automático de PDFs

Este script automatiza la conversión de archivos a PDF en las PCs del trabajo, ideal para usuarios que no quieren (o no saben) manejar manualmente Office. Solo tienes que colocar los archivos en la carpeta correspondiente y el script se encarga del resto.

---

## Características

* Convierte automáticamente documentos a PDF.
* Evita procesos manuales repetitivos.
* Funciona en segundo plano, detectando cambios en carpetas automáticamente.

---

## Requisitos

* [LibreOffice](https://www.libreoffice.org/) (para la conversión de archivos)
* [Watchdog](https://pypi.org/project/watchdog/) (para detectar cambios en las carpetas)

Para instalar Watchdog:

```bash
pip install watchdog
```

---

## Uso

1. Coloca los archivos que quieras convertir en la carpeta de entrada configurada.
2. Ejecuta el script:

```bash
python main_cli.py
```

3. Los PDFs generados se guardarán automáticamente en la carpeta de salida.

---

## Notas

* Diseñado para usuarios que no tienen mucha experiencia con Office.
* Funciona en Windows, Linux y macOS mientras LibreOffice esté instalado.

---

##
Seguramente haga una interfaz grafica y mas funcionalidades pero para lo que lo vengo usando me sirve
