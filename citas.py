import os
import core
import random
from datetime import datetime

diccCitas = {}

def loadInfoPaciente(fileName):
    global diccCitas
    if core.checkFile('citas.json'):
        diccCitas = core.LoadInfo('citas.json')
    else:
        core.crearInfo('citas.json', diccCitas)

def mainMenu():
    crearMenu = True
    while crearMenu:
        os.system('cls') and os.system('clear')
        print('MENU CITAS')
        print('1. Registrar cita', '2. Buscar cita', '3. Consultar cita', '4. Volver al menu principal', sep ='\n')
        opcion = int(input(' Ingrese la opcion del menu que desea realizar: '))
        diccCPaciente = core.LoadInfo('pacientes.json')
        diccVeterinarios = core.LoadInfo('veterinarios.json')
        
        if opcion == 1:
        #REGISTRAR CITA 
            os.system('cls') and os.system('clear')
            idCita = (str(random.randint(1,10000))).zfill(5)
            
            print('LISTADO DE PACIENTES')
            for item in diccCPaciente:
                print(F'ID:{item}, NOMBRE:{diccCPaciente[item]["nombre"]}')
            idBusqueda = input('Ingrese el ID del paciente: ').strip()
            if idBusqueda in diccCPaciente:
                paciente = diccCPaciente[idBusqueda]['nombre']
                idPac = idBusqueda
            else:
                print('Ingrese un codigo del paciente que se encuentre en la lista')
                os.system('pause') and os.system('sleep 5')
                crearMenu = False
                continue
            
            print('LISTADO VETERINARIOS')
            for llave in diccVeterinarios:
                print(f'{llave}: {diccVeterinarios[llave]["nombre"]} -- Horario: {diccVeterinarios[llave]["horario"]}')
            idBusVet = (input('Ingrese el ID del veterinario: ').strip())
            if idBusVet in diccVeterinarios:
                veterinario = diccVeterinarios[idBusVet]['nombre']
                idVet = idBusVet
            else:
                print('El veterinario no se encuetra en el sistema.')
                os.system('pause') and os.system('sleep 5')
                crearMenu = False
                continue
            
            fechaCita = (input('Ingrese la fecha en la que desea programar la cita(dd/mm/aa): ').strip()).upper()
            while True:  
                try:
                    fecha = datetime.strptime(fechaCita, "%d/%m/%Y").date()
                    break
                except ValueError:
                    print('Formato de fecha no permitido, vuelva a ingresar la fecha de consulta.')
                    os.system('pause') and os.system('sleep 5')
                    break
            fechaFinal = fecha.strftime("%d/%m/%Y")
            
            horaCita = (input('Ingrese la hora en la que desea agentar la cita: ').strip()).upper()
            while True:
                try:
                    hora = datetime.strptime(horaCita, "%H:%M").time()
                    break
                except:
                    print('Formato de hora no permitido, vuelva a ingresar la hora de consulta.')
                    os.system('pause') and os.system('sleep 5')
                    break
            listaConvert = []
            for index in diccVeterinarios[idVet]['horario']:
                horarioConvert = datetime.strptime(index,"%H:%M").time()
                listaConvert.append(horarioConvert)
            if(hora in listaConvert):
                horaFinal = hora.strftime("%H:%M")
            else:
                print('La hora programada no coincide en el horario del veterinario. Vuelva a registrar la informacion.')
                os.system('pause') and os.system('sleep 5') 
                crearMenu = False
                continue
        
            citas={
                'idCita':idCita,
                'nombrePaciente':paciente,
                'idPac': idPac,
                'idVet': idVet,
                'veterinario': veterinario,
                'fechaCita':fechaFinal,
                'horaCita': horaFinal,
            }
            diccCitas.update({f'{idCita}':citas})
            core.crearInfo('citas.json',diccCitas)
            
        elif opcion == 2:
            #Buscar citas médicas por nombre 
            os.system('cls') and os.system('clear')
            print('BUSQUEDA DE CITAS')
            print('1. Busqueda por fecha', '2. Busqueda por paciente', '3. Busqueda por veterinario','4. Volver al Menu Principal')
            opcionBusqueda = int(input('Ingrese el metodo para realizar su busqueda: '))
            if opcionBusqueda == 1:
                encontrado = False
                fechaBusqueda = input('Ingrese la fecha de busqued: ')
                for llave in diccCitas:
                    if fechaBusqueda == diccCitas[llave]['fechaCita']:
                        print(f'ID CITA: {diccCitas[llave]["idCita"]}')
                        print(f'NOMBRE PACIENTE: {diccCitas[llave]["nombrePaciente"]}')
                        print(f'ID PACIENTE: {diccCitas[llave]["idPac"]}')
                        print(f'ID VETERINARIO: {diccCitas[llave]["idVet"]}')
                        print(f'NOMBRE VETERINARIO: {diccCitas[llave]["veterinario"]}')
                        print(f'FECHA CITA: {fechaBusqueda}')
                        print(f'HORA CITA: {diccCitas[llave]["horaCita"]}')
                        os.system('pause') and os.system('sleep 5')
                        encontrado = True
                        break
                if not encontrado:
                    print('No se encuentra asignada una cita para la fecha ingresada')
                    os.system('pause') and os.system('sleep 5')
            elif opcionBusqueda == 2:
                encontrado2 = False
                veterinarioBusqueda = (input('Ingrese el nombre del paciente: ').strip()).upper()
                for llave2 in diccCitas:
                    if veterinarioBusqueda == diccCitas[llave2]['nombrePaciente']:
                        print(f'ID CITA: {diccCitas[llave2]["idCita"]}')
                        print(f'NOMBRE PACIENTE: {veterinarioBusqueda}')
                        print(f'ID PACIENTE: {diccCitas[llave2]["idPac"]}')
                        print(f'ID VETERINARIO: {diccCitas[llave2]["idVet"]}')
                        print(f'NOMBRE VETERINARIO: {diccCitas[llave2]["veterinario"]}')
                        print(f'FECHA CITA: {diccCitas[llave2]["fechaCita"]}')
                        print(f'HORA CITA: {diccCitas[llave2]["horaCita"]}')
                        os.system('pause') and os.system('sleep 5')
                        encontrado2 = True
                        break
                if not encontrado2:
                    print('No se encuentra asignada una cita para el paciente ingresado')
                    os.system('pause') and os.system('sleep 5')
            elif opcionBusqueda == 3:
                encontrado3 = False
                veterinarioBusqueda = (input('Ingrese el nombre del paciente: ').strip()).upper()
                for llave3 in diccCitas:
                    if veterinarioBusqueda == diccCitas[llave3]['veterinario']:
                        print(f'ID CITA: {diccCitas[llave3]["idCita"]}')
                        print(f'NOMBRE PACIENTE: {diccCitas[llave3]["nombrePaciente"]}')
                        print(f'ID PACIENTE: {diccCitas[llave3]["idPac"]}')
                        print(f'ID VETERINARIO: {veterinarioBusqueda}')
                        print(f'NOMBRE VETERINARIO: {diccCitas[llave3]["veterinario"]}')
                        print(f'FECHA CITA: {diccCitas[llave3]["fechaCita"]}')
                        print(f'HORA CITA: {diccCitas[llave3]["horaCita"]}')
                        os.system('pause') and os.system('sleep 5')
                        encontrado3 = True
                        break
                if not encontrado3:
                    print('No se encuentra asignada una cita para el vdterinario ingresado')
                    os.system('pause') and os.system('sleep 5')
            elif opcionBusqueda == 4:
                crearMenu = False
                
        elif opcion == 3:
        #MOSTRAR CITA Y AGREGAR INFO DEL PACIENTE Y DEL VETERINARIO 
            print('MOSTRAR CITA Y AÑADIR INFORMACION DEL VETERINARIO')
            for cod in diccCitas:
                print(f'ID: {diccCitas[cod]}, NOMBRE PACIENTE: {diccCitas[cod]["nombrePaciente"]}')
            codBusqueda = input('Ingrese el ID de la cita que dese buscar: ').strip()
            checkCod = diccCitas.get(codBusqueda,-1)
            if checkCod == -1:
                print('Ingrese nuevamente el codigo de la cita, ya que no se encuentra registrada')
            else:
                for hor in diccVeterinarios:
                    if diccCitas[cod]['veterinario'] == diccVeterinarios[hor]['nombre']:
                        tituloUni = diccVeterinarios[hor]['titulo']
                        horario = diccVeterinarios[hor]['horario']
                        diccCitas[cod].update({'titulo':tituloUni})
                        diccCitas[cod].update({'horario':horario})
                        break
                for a in diccCPaciente:
                    if diccCitas[cod]['nombrePaciente'] == diccCPaciente[a]['nombre']:
                        raza = diccCPaciente[a]['raza']
                        edad = diccCPaciente[a]['edad']
                        diccCitas[cod].update({'razaPaciente':raza})
                        diccCitas[cod].update({'edadPaciente':edad})
                        break
                core.EditarData('citas.json',diccCitas)
                print(f'ID CITA: {codBusqueda}')
                print(f'NOMBRE PACIENTE: {veterinarioBusqueda}')
                print(f'ID PACIENTE: {diccCitas[cod]["idPac"]}')
                print(f'ID VETERINARIO: {diccCitas[cod]["idVet"]}')
                print(f'NOMBRE VETERINARIO: {diccCitas[cod]["veterinario"]}')
                print(f'FECHA CITA: {diccCitas[cod]["fechaCita"]}')
                print(f'TITULO: {diccCitas[cod]["titulo"]}')
                print(f'HORA CITA: {diccCitas[cod]["horario"]}')
                print(f'HORA CITA: {diccCitas[cod]["raza"]}')
                print(f'HORA CITA: {diccCitas[cod]["edad"]}')
            
        elif opcion == 4:
        #EDITAR INFORMACION: 
            print('MODIFICACION DE CITAS') 
            for llave in diccCitas:
                print(f'ID: {llave}, NOMBRE PACIENTE: {llave["nombrePaciente"]}')
            idBusqueda = input('Ingrese el codigo de la cita que desea modificar: ')
            
                
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            crearMenu = False
            if crearMenu:
                mainMenu()
        