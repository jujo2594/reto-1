import os
import core
import random
diccPacientes = { }

def loadInfoPaciente(fileName):
    global diccPacientes
    if (core.checkFile('pacientes.json')):
        diccPacientes = core.LoadInfo('pacientes.json')
    else:
        core.crearInfo('pacientes.json', diccPacientes)
def mainMenu():
    crearMenu = True
    print('MENU PACIENTES')
    print('1. Registrar Paciente', '2. Buscar Paciente', '3. Mostrar informacion paciente', '4. Volver al menu principal', sep ='\n')
    opcion = int(input(' Ingrese la opcion del menu que desea realizar: '))
    if opcion == 1:
        os.system('cls') and os.system('clear')
        nombre = (input('Ingrese el nombre del paciente: ').strip()).upper()
        raza = (input('Ingrese  la raza de la mascota: ').strip()).upper()
        edad = int(input('Ingrese la edad del paciente: '))
        nombrePropietario = (input('Ingrese el nombre del propietario: ').strip()).upper()
        print('Ingrese el tipo de mascota:\n 1. Perro.\n 2. Gato.\n 3. Reptil.\n 4. Ave')
        tipo = (input('Ingrese el tipo de mascota: ').strip()).upper()
        while( tipo !='PERRO' and tipo !='GATO' and tipo !='REPTIL' and tipo !='AVE'):
            print('Ingrese un tipo de mascota dentro de la lista mostrada: ')
            tipo = (input('Ingrese el tipo de mascota: ').strip()).upper()
        id = str(random.randint(1,10000)).zfill(5)
        pacientes ={
            'id': id,
            'nombre':nombre,
            'raza':raza,
            'edad':edad,
            'nombrePropietario':nombrePropietario,
            'tipo':tipo
        }
        diccPacientes.update({f'{id}':pacientes})
        print(diccPacientes)
        core.crearInfo('pacientes.json',diccPacientes)
    elif opcion == 2:
        os.system('cls') and os.system('clear')
        nombreBusqueda = (input('Ingrese el nombre de la mascota a buscar: ').strip()).upper()
        encontrado = False
        for llave, valor in enumerate(diccPacientes):
            if (nombreBusqueda == diccPacientes[valor]['nombre']):
                print(f"El NOMBRE del paciente es: {nombreBusqueda}")
                print(f"El ID del paciente es: {diccPacientes[valor]['id']}")
                print(f"La RAZA del paciente es: {diccPacientes[valor]['raza']}")
                print(f"La EDAD del paciente es: {diccPacientes[valor]['edad']}")
                print(f"El NOMBRE PROPIETARIO del paciente es: {diccPacientes[valor]['nombrePropietario']}")
                print(f"El TIPO del paciente es: {diccPacientes[valor]['tipo']}")
                encontrado = True
                break
        if not encontrado:
            print('No se encontro el nombre que esta buscando por favor ingrese otro nombre')
    elif opcion == 3:
        os.system('cls') and os.system('clear')
        print('LISTADO PACIENTES:')
        for llave, valor in enumerate(diccPacientes):
            print(f"{valor}: {diccPacientes[valor]['nombre']}")
        busqueda = input('Ingrese el codigo del paciente que desea buscar: ')
        validar = diccPacientes.get(busqueda,-1)
        if validar == -1:
            print('Ingrese nuevamente un codigo que se encuentre dentro del listado')
            os.system('pause') and os.system('sleep')
        else:
            diccPacientes[busqueda].update({'historial':(input('Ingrese el historial del paciente: ').strip()).upper()})
            core.EditarData('pacientes.json', diccPacientes)
            print(f'ID: {busqueda}')
            print(f'NOMBRE: {diccPacientes[busqueda]["nombre"]}')
            print(f'RAZA: {diccPacientes[busqueda]["raza"]}')
            print(f'EDAD: {diccPacientes[busqueda]["edad"]}')
            print(f'NOMBRE PROPIETARIO: {diccPacientes[busqueda]["nombrePropietario"]}')
            print(f'TIPO: {diccPacientes[busqueda]["tipo"]}')
            print(f'HISTORIAL: {diccPacientes[busqueda]["historial"]}')
            print(diccPacientes)
    elif opcion == 4:
        crearMenu = False
        if crearMenu:
            mainMenu()