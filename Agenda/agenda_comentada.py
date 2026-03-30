import csv  # Importa el módulo nativo de Python para trabajar con archivos CSV

nombres = []  # Inicializa una lista vacía para almacenar los nombres que extraeremos
# Abre el archivo CSV en modo lectura ('r') asegurando el soporte de tildes/eñes (utf-8)
with open('listado_personas.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)  # Crea un objeto lector que procesa las líneas del archivo
    next(lector)  # Saltamos cabecera = Salta la primera fila (normalmente contiene los títulos de las columnas)

    # Creamos la lista en una sola línea
    nombres = [fila[1] for fila in lector]        

print(nombres)  # Muestra en la consola la lista final con todos los nombres extraídos