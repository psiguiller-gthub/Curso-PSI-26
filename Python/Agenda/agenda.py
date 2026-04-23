# Agenda de Contactos
import csv 

def agregar_contacto(contacto, archivo):  # contacto es un diccionario con los datos del nuevo contacto a agregar, y archivo es el nombre del archivo CSV donde se almacenarán los contactos. La función abre el archivo en modo de escritura (append) y utiliza csv.writer para escribir una nueva fila con los datos del contacto en el archivo CSV.
    with open(archivo, mode='a', newline='') as file: # Abre el archivo en modo de escritura (append) y con newline='' para evitar líneas en blanco adicionales.

        ID = contacto['ID']
        nombre = contacto['nombre']
        apellido = contacto['apellido']
        telefono = contacto['telefono']
        email = contacto['email']
        poblacion = contacto['poblacion'] 

        writer = csv.writer(file) # Crea un objeto writer para escribir en el archivo CSV
        writer.writerow([ID,nombre, apellido, telefono, email, poblacion]) # Escribe una nueva fila en el archivo CSV con los datos del contacto utilizando writer.writerow() y 
                                                                           # pasando una lista con los valores correspondientes a cada campo del contacto.
def cargar_contactos(archivo):
    contactos = []
    with open(archivo, mode='r') as file: # Abre el archivo en modo de lectura (read) para cargar los contactos existentes desde el archivo CSV. 
        reader = csv.DictReader(file) # La función utiliza csv.DictReader para leer el archivo CSV y convertir cada fila en un diccionario, que luego se agrega a la lista de contactos.
        for row in reader: # Itera sobre cada fila del archivo CSV utilizando un bucle for. Cada fila se representa como un diccionario (row).
            contactos.append(row) # Agrega el diccionario de cada fila a la lista de contactos utilizando contactos.append(row).
    return contactos

def mostrar_contactos(contactos):
    for contacto in contactos:
        print(f"ID: \n{contacto['ID']}, \nNombre: {contacto['nombre']} \nApellido: {contacto['apellido']}, \nTeléfono: {contacto['telefono']}, \nEmail: {contacto['email']}, \nPoblación: {contacto['poblacion']}")

if __name__ == "__main__":

    archivo_csv = 'listado_personas.csv'
    contactos = cargar_contactos(archivo_csv)   
    mostrar_contactos(contactos)

    # Agregar un nuevo contacto
    contacto = {
        'ID': 6,
        'nombre': 'Maria',
        'apellido': 'Pérez',
        'telefono': '123456789',
        'email': 'm.p@example.com',
        'poblacion': 'Madrid'
    }
    agregar_contacto(contacto, archivo_csv)
    contactos = cargar_contactos(archivo_csv) # Después de agregar el nuevo contacto, se vuelve a cargar la lista de contactos desde el archivo CSV para reflejar los cambios realizados.
    mostrar_contactos(contactos)