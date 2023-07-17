import os
import core
import random
from datetime import datetime

diccVeterinarios = { }

def loadInfoVeterinarios(fileName):
    global diccVeterinarios
    if core.checkFile('veterinarios.json'):
        diccVeterinarios = core.LoadInfo('veterinarios.json')
    else:
        core.crearInfo('veterinarios.json', diccVeterinarios)
def mainMenu():
    crearMenu = True
    print('MENU VETERINARIO')
    print('1. Registrar Veterinario', '2. Buscar Veterinario', '3. Mostrar informacion', '4. Volver al menu principal', sep ='\n')
    opcion = int(input(' Ingrese la opcion del menu que desea realizar: '))
    if opcion == 1:
        os.system('cls') and os.system('clear')
        nombre = (input('Ingrese el nombre del veterinario: ').strip()).upper()
        titulo = (input('Ingrese el titulo del veterinario: ').strip()).upper()
        while True:
            fechaRegistro = input('Ingrese la fecha de registro formato(dd/mm/aa): ')
            try:
                fecha = datetime.strptime(fechaRegistro, "%d/%m/%Y").date()
                break
            except ValueError:
                print('El formato de fecha no es el correcto, vuelva a registrar la fecha')
                break
        fechaFinal = fecha.strftime("%d/%m/%Y")
        #strptime: strp time es un método de la clase datetime en python se utiliza para convertir una cadena de texto en un objeto 'datetime'
        #strftime: Se utiliza para formatear un objeto 'datetime' en una cadena de texto segun un formato especifico.
        id = str(random.randint(1,10000)).zfill(5)
        veterinarios ={
            'id': id,
            'nombre':nombre,
            'titulo':titulo,
            'fechaRegistro':fechaFinal
        }
        diccVeterinarios.update({f'{id}':veterinarios})
        print(diccVeterinarios)
        core.crearInfo('veterinarios.json',diccVeterinarios)
    elif opcion == 2:
        os.system('cls') and os.system('clear')
        nombreBusqueda = (input('Ingrese el nombre del veterinario a buscar: ').strip()).upper()
        encontrado = False
        for llave, valor in enumerate(diccVeterinarios):
            if (nombreBusqueda == diccVeterinarios[valor]['nombre']):
                print(f"El ID del veterinario es: {diccVeterinarios[valor]['id']}")
                print(f"El NOMBRE del veterinario es: {nombreBusqueda}")
                print(f"El titulo del veterinario es: {diccVeterinarios[valor]['titulo']}")
                print(f"La FECHA DE REGISTRO es: {diccVeterinarios[valor]['fechaRegistro']}")
                encontrado = True
                break
        if not encontrado:
            print('No se encontro el nombre que esta buscando por favor ingrese otro nombre')
    elif opcion == 3:
        os.system('cls') and os.system('clear')
        print('LISTADO VETERINARIOS:')
        for llave, valor in enumerate(diccVeterinarios):
            print(f"{valor}: {diccVeterinarios[valor]['nombre']}")
        busqueda = input('Ingrese el codigo del veterinario que desea buscar: ')
        validar = diccVeterinarios.get(busqueda,-1)
        if validar == -1:
            print('Ingrese nuevamente un codigo que se encuentre dentro del listado')
            os.system('pause') and os.system('sleep')
        else:
            while True:
                print('INGRESE HORARIO VETERINARIO:')
                horario1 = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00']
                horario2 = ['08:01','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00']
                horario3 = ['16:01','17:00','18:00','19:00','20:00','21:00','22:00','23:00','23:59']
                print(f'Horario 1: {horario1}, Jornada: Madrugada-Mañana')
                print(f'Horario 2: {horario2}, Jornada: Mañana - Tarde')
                print(f'Horario 3: {horario3}, Jornada: Tarde - Noche')
                print('1. Para ingresar el horario 1: ','2. Para ingresar el horario 2: ', '3. Para ingresar el horario 3: ',sep = '\n')
                opcionHorario = int(input('Ingrese el horario que desea asignar al veterinario: '))
                try:
                    if(opcionHorario == 1):
                        horario = horario1
                    elif(opcionHorario == 2):
                        horario = horario2
                    elif(opcionHorario == 3):
                        horario = horario3
                    else:
                        print('Ingrese una opcion disponible dentro del menu')
                except Exception as e:
                    print(f'Error: {e}')
                diccVeterinarios[busqueda].update({'horario':horario})
                core.EditarData('veterinarios.json', diccVeterinarios)
                print(f'ID: {busqueda}')
                print(f'NOMBRE: {diccVeterinarios[busqueda]["nombre"]}')
                print(f'TITULO: {diccVeterinarios[busqueda]["titulo"]}')
                print(f'FECHA REGISTRO: {diccVeterinarios[busqueda]["fechaRegistro"]}')
                print(f'HORARIO: {diccVeterinarios[busqueda]["horario"]}')
                print(diccVeterinarios)
                break
    elif opcion == 4:
        crearMenu = False
        if crearMenu:
            mainMenu()