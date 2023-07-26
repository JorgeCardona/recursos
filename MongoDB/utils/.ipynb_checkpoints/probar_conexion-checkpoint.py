from pprint import pprint
from pymongo import MongoClient

def listar_usuarios(cliente):
    db = cliente['admin']
    
    # Obtener una lista de todos los usuarios
    users_list = db.command('usersInfo')

    # valida si existen usuarios creados
    if users_list['users']:

        print("LOS USUARIOS ENCONTRADOS SON")
        # Mostrar los usuarios
        for user_info in users_list['users']:
            print(f"user = {user_info['user']}, role = {user_info['db']}")
        print()
    else:
        pprint("NO EXISTEN USUARIOS ADICIONADOS")

def validar_role_de_usuario(cliente, user_name):

    # Seleccionar la base de datos "admin"
    db = cliente['admin']

    # Obtener la colección "system.users" que contiene los usuarios y sus roles
    users_collection = db['system.users']
    
    # Buscar el usuario específico por su nombre
    user_info = users_collection.find_one({"user": user_name})
    
    # Mostrar los roles del usuario
    if user_info:
        print("Roles para el usuario", user_name)
        for role_info in user_info.get('roles', []):
            print(role_info)
        print()
    else:
        print("El usuario", user_name, "no existe.")
        
def listas_bases_de_datos(client):
    # Obtener una lista de todas las bases de datos disponibles
    database_list = client.list_database_names()

    print(f'LAS BASES DE DATOS ENCONTRADAS SON : {database_list}')
    print()
    
def listar_colecciones(cliente, nombre_base_de_datos):
    
    # Seleccionar la base de datos
    db = cliente[nombre_base_de_datos]
    
    # Obtener la lista de colecciones en la base de datos seleccionada
    collections_list = db.list_collection_names()
    print(f'LAS COLECCIONES ENCONTRADAS SON : {collections_list}')
    print()


def listar_documentos(cliente, nombre_base_de_datos, nombre_coleccion, total_documentos=1):

    # Seleccionar la base de datos
    db = cliente[nombre_base_de_datos]
    
    leer_coleccion = db[nombre_coleccion]
    cursor = leer_coleccion.find().limit(total_documentos)

    print('LOS DOCUMENTOS ENCONTRADOS SON')
    for documento in cursor:
        pprint(documento)
    print()
    
def existen_documentos(cliente, nombre_base_de_datos, nombre_coleccion):
    
    db = cliente[nombre_base_de_datos]
    collection = db[nombre_coleccion]
    result = collection.find_one()
    
    if result:
        return True
    return False
    
def ping_database(tipo_de_conexion, port, user, password, nombre_base_de_datos, nombre_coleccion):

    if tipo_de_conexion.lower() == 'local':
        host = 'localhost'
    elif tipo_de_conexion.lower() == 'docker':
        host = 'host.docker.internal'
    try:
        # Intentar conectarse al servidor MongoDB
        cliente = MongoClient(host, port, username=user, password=password)

        if existen_documentos(cliente, nombre_base_de_datos, nombre_coleccion):
            print("La conexión fue exitosa. El servidor MongoDB está accesible.")
            print()
            listar_usuarios(cliente)
            validar_role_de_usuario(cliente, user)
            listas_bases_de_datos(cliente)
            listar_colecciones(cliente, nombre_base_de_datos)
            listar_documentos(cliente, nombre_base_de_datos, nombre_coleccion, total_documentos=1)
            print()
        else:
            print(f"La conexión fue exitosa, pero no se encontraron documentos en la coleccion {nombre_coleccion}.")
        cliente.close()
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")