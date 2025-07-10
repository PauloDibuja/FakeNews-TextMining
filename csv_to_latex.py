import csv
import os

def escapar_latex(texto: str) -> str:
    """
    Escapa los caracteres especiales de LaTeX en una cadena de texto.
    """
    reemplazos = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
        '\\': r'\textbackslash{}',
    }
    for original, escapado in reemplazos.items():
        texto = texto.replace(original, escapado)
    return texto

def generar_latex_de_csv(ruta_csv: str):
    """
    Lee un archivo CSV y genera el código LaTeX para una tabla en un archivo .tex.

    Args:
        ruta_csv (str): La ruta al archivo de entrada .csv.
    """
    try:
        with open(ruta_csv, mode='r', newline='', encoding='utf-8') as archivo_csv:
            lector_csv = list(csv.reader(archivo_csv))

        if not lector_csv:
            print("Advertencia: El archivo CSV está vacío.")
            return

        encabezado = lector_csv[0]
        datos = lector_csv[1:]
        num_columnas = len(encabezado)

        # Inicia la escritura del código LaTeX
        codigo_latex = []
        codigo_latex.append(r'\begin{table}[ht]')  # [ht] sugiere la posición a LaTeX
        codigo_latex.append(r'\centering')

        # Define el formato de las columnas ('l' para izquierda, 'c' para centro, 'r' para derecha)
        formato_columnas = ' '.join(['l'] * num_columnas)
        codigo_latex.append(f'\\begin{{tabular}}{{{formato_columnas}}}')
        codigo_latex.append(r'\hline')

        # Fila del encabezado en negrita
        fila_encabezado = [r'\textbf{' + escapar_latex(celda) + r'}' for celda in encabezado]
        codigo_latex.append(' & '.join(fila_encabezado) + r' \\')
        codigo_latex.append(r'\hline')
        
        # Filas de datos
        for fila in datos:
            fila_escapada = [escapar_latex(celda) for celda in fila]
            codigo_latex.append(' & '.join(fila_escapada) + r' \\')

        # Cierre de la tabla
        codigo_latex.append(r'\hline')
        codigo_latex.append(r'\end{tabular}')
        
        # Añade un caption y una etiqueta para referencias cruzadas
        nombre_tabla = os.path.basename(ruta_csv).replace('_', ' ').replace('.csv', '')
        codigo_latex.append(f'\\caption{{Tabla generada desde {nombre_tabla}.}}')
        codigo_latex.append(f'\\label{{tab:{nombre_tabla}}}')
        codigo_latex.append(r'\end{table}')

        return "\n".join(codigo_latex)
    except FileNotFoundError:
        print(f"❌ Error: No se pudo encontrar el archivo CSV en '{ruta_csv}'")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")


# --- CÓMO USAR EL SCRIPT ---
if __name__ == '__main__':


    complete_tex_file = "complete.tex"
    # append all post tema tex files to complete.tex
    with open(complete_tex_file, 'w', encoding='utf-8') as complete_file:
        for i, j in [(a, b) for a in range(5) for b in range(5)]:
            nombre_archivo_csv = f'post_{i + 1}_tema_{j + 1}.csv'
            complete_file.write(generar_latex_de_csv(nombre_archivo_csv))
            complete_file.write("\n\n")
    print(f"✅ El archivo LaTeX completo se ha generado en '{complete_tex_file}'.")

    pass
"""
for i, j in [(a, b) for a in range(5) for b in range(5)]:
        nombre_archivo_csv = f'post_{i + 1}_tema_{j + 1}.csv'

        # 2. Define el nombre del archivo .tex que quieres generar
        nombre_archivo_tex = nombre_archivo_csv.replace('.csv', '.tex')

        # 3. Llama a la función para generar el archivo
        generar_latex_de_csv(nombre_archivo_csv, nombre_archivo_tex)

        # (Opcional) Imprime el contenido generado
        print("\n--- Contenido del archivo .tex generado ---")
        with open(nombre_archivo_tex, 'r', encoding='utf-8') as f:
            print(f.read())
        print("-----------------------------------------")
"""