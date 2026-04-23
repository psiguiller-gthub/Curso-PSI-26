# Agenda de Contactos
import csv 

def cargar_contactos(archivo):
    contactos = []
    with open(archivo, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:          # row = fila, tupla  in reader lee cada fila del archivo CSV
            contactos.append(row)   # añade la fila a la lista de contactos
    return contactos        # devuelve la lista de contactos cargados desde el archivo CSV para su posterior uso

def mostrar_contactos(contactos):
    for contacto in contactos:
        print(f"ID: \n{contacto['ID']}, \nNombre: {contacto['nombre']} \nApellido: {contacto['apellido']}, \nTeléfono: {contacto['telefono']}, \nEmail: {contacto['email']}, \nPoblación: {contacto['poblacion']}")

if __name__ == "__main__":

    archivo_csv = 'listado_personas.csv'
    contactos = cargar_contactos(archivo_csv)
    mostrar_contactos(contactos)
