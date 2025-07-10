import os
from dotenv import load_dotenv
import requests
import sys

def getGoogleSeet(spreadsheet_id, outFile):
  
  url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv'
  response = requests.get(url)
  if response.status_code == 200:
    actualDir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(actualDir, outFile)
    with open(filepath, 'wb') as f:
      f.write(response.content)
      print('CSV file saved to: {}'.format(filepath))    
  else:
    print(f'Error downloading Google Sheet: {response.status_code}')

# Cargar variables del .env
load_dotenv()

link = os.getenv("GOOGLE_SHEET_ID")
if not link:
    raise EnvironmentError("No se encontró GOOGLE_SHEET_ID en el archivo .env")
filepath = getGoogleSeet(link, "results.csv")