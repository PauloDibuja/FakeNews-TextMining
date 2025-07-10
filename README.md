# Instalación de dependencias

# Windows (PowerShell)
```bash
./script_install.ps1
```
# Linux / MacOS
```bash
./script_install.sh
```

# Descarga de CSV de Google Sheets

1. Crea archivo .env en la raíz del proyecto y agregar:
    ```plaintext
    GOOGLE_SHEET_ID=tu_id_de_google_sheet
    ```
    También puedes asignar manualmente variable de entorno `GOOGLE_SHEET_ID` con el ID de tu Google Sheet.

    ```bash
    export GOOGLE_SHEET_ID=tu_id_de_google_sheet
    ```
2. Ejecuta el script de Python para descargar el CSV:
    ```bash
    python download_csv.py
    ```
# Recursos

- Stop Words Español (`stop_words_spanish.txt`) - CountWordsFree : https://countwordsfree.com/stopwords/spanish
- Polars : https://docs.pola.rs/
- Scikit-Learn / Latent Dirichlet Allocation : https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html 
  