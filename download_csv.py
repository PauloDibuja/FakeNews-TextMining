import requests
import re
import os
from dotenv import load_dotenv

def descargar_csv_desde_google_sheets(link, nombre_archivo="output.csv"):
    # Extraer el ID del documento
    match = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', link)
    if not match:
        raise ValueError("No se pudo extraer el ID del enlace proporcionado.")
    
    sheet_id = match.group(1)

    # Extraer el gid si está presente
    gid_match = re.search(r'gid=([0-9]+)', link)
    gid = gid_match.group(1) if gid_match else "0"

    # Armar URL de exportación
    export_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

    print(f"Descargando desde: {export_url}")

    response = requests.get(export_url)

    if response.status_code == 200:
        with open(nombre_archivo, "wb") as f:
            f.write(response.content)
        print(f"CSV guardado como {nombre_archivo}")
    else:
        print(f"Error: No se pudo descargar el CSV. Código de estado: {response.status_code}")

if __name__ == "__main__":
    # Cargar variables del .env
    load_dotenv()

    link = os.getenv("GOOGLE_SHEET_LINK")
    if not link:
        raise EnvironmentError("No se encontró GOOGLE_SHEET_LINK en el archivo .env")

    descargar_csv_desde_google_sheets(link)
