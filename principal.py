import os
import pacientes
import veterinarios
import citas
from datetime import datetime

if __name__ == '__main__':
    iniciar = True
    while iniciar:
        os.system('cls') and os.system('clear')
        print('1. Ingresar Menu Pacientes: ', '2. Ingresar Menu Veterinarios: ', '3. Ingresar Menu Citas: ', '4. Salir: ', sep ='\n')
        opcion = int(input('Ingrese una opcion del menu: '))
        try:
            if opcion == 1:
                os.system('cls') and os.system('clear')
                pacientes.loadInfoPaciente('pacientes.json')
                pacientes.mainMenu()
                os.system('pause') and os.system('sleep')
            elif opcion == 2:
                os.system('cls') and os.system('clear')
                veterinarios.loadInfoVeterinarios('veterinarios.json')
                veterinarios.mainMenu()
                os.system('pause') and os.system('sleep')
            elif opcion == 3:
                os.system('cls') and os.system('clear')
                citas.loadInfoPaciente('citas.json')
                citas.mainMenu()
                pass
                os.system('pause') and os.system('sleep')
            elif opcion == 4:
                os.system('clear')
                iniciar = False
            else:
                os.system('clear')
                print('Ingrese una opcion valida')
        except ValueError:
            print('Ingrese un numero, de acuerdo a las opciones del menu')
        except Exception as e:
            print(f'Error: {e}')