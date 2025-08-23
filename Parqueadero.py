##Importacion de paquetes para captura
import math
from datetime import datetime
from operator import length_hint

## declaracion de variables
parqueadero = []
reportes =[]
capacidadCarros = 50
capacidadMotos = 20
##vehiculo = {}##posible no utilizacion del diccionario
caso = 0
costoCarros = 2500
costoMotos = 1500

#Funcion para validar placa
def placaExiste(placa):
        if not parqueadero:
            return False
        for v in parqueadero:
            if v['Placa'].lower() == placa.lower():
                return True
        return False
#funcion para ingreso de vehiculos
def ingresoVehiculo(placa, tipo):
    horaIngreso = capturaHora()
    nuevoVehiculo = {}#evita que se re escriban los datos existentes - crea un nuevo vehiculo.
    match tipo:##tambien conocido como switch
        case 1:
            nuevoVehiculo['Placa']=(placa)
            nuevoVehiculo['Tipo']=("Carro")
            nuevoVehiculo['Hora Ingreso']=horaIngreso
            parqueadero.append(nuevoVehiculo)
            print("Vehiculo ingresado con exito")
            return True
        case 2:
            nuevoVehiculo['Placa'] = (placa)
            nuevoVehiculo['Tipo'] = ("Moto")
            nuevoVehiculo['Hora Ingreso'] = horaIngreso
            parqueadero.append(nuevoVehiculo)
            print("Vehiculo ingresado con exito")
            return True
        case _:
            return False

#Funcion para salida de vehiculos
def salidaVehiculo(placa, tipo):
    horaSalida = capturaHora()
    for v in parqueadero:
        if v["Placa"].lower() == placa.lower():
            v['Hora Salida'] = horaSalida
            h_Ingreso = datetime.strptime(v['Hora Ingreso'], calculoFormato) # datetime.strptime realiza un formateo de la hora para poder realizar calculos
            h_Salida = datetime.strptime(v['Hora Salida'], calculoFormato)
            tiempoMinutos = (h_Salida - h_Ingreso).total_seconds() / 60
            tiempoHora = max(1, math.ceil(tiempoMinutos / 60))#math.ceil redondea la cifra al numero siguente ejemplo 1.5->2
            if tipo == 1 and v['Tipo'] == 'Carro':
                v['Costo'] = costoCarros * tiempoHora
            elif tipo == 2 and v['Tipo'] == 'Moto':
                v['Costo'] = costoMotos * tiempoHora
            else:
                print("El tipo de vehículo no coincide")
                return False

            reportes.append(v)
            parqueadero.remove(v)
            imprimirFactura(placa)
            return True

    print("Placa no existe")
    return False


#funcion imprimir
def imprimirFactura(placa):
    for v in reportes:
        if v['Placa'].lower()==placa.lower():
            print(f'---FACTURA-----')
            print(f'Placa:{v['Placa']}')
            print(f'Tipo vehiculo:{v['Tipo']}')
            print(f'Hora Ingreso:{v['Hora Ingreso']}')
            print(f'Hora Salida:{v['Hora Salida']}')
            print(f'Valor:{v['Costo']}')
            print(f'--------------')

##funcion captura de hora
def capturaHora():
    ahora = datetime.now()  ##Captura la hora del sistema automaticamente
    horaFormato = ahora.strftime('%H:%M:%S')  ##se le da formato a la hora del sistema
    return horaFormato

##ciclo para el Programa
while caso == 0:
    ##Menu Principal para el ingreso o salida de Vehiculos
    print("******************************************")
    print(f'Bienvenidos Al Parqueadero el Rayadero\nCapacidad de motos: {capacidadMotos}\nCapacidad Carros: {capacidadCarros}')
    print('******************************************')
    opcion =(input (f'Menu Principal \n1.Ingresar Vehiculo\n2.Salida Vehiculo\n3.Reportes\n4.Salir\nOpcion: '))
    print('******************************************')
    calculoFormato = '%H:%M:%S'

    if opcion.isdigit():#validacion para saber si es numero.
        entrada = int(opcion)
        try:
            ##Este es la manera de realizar un switch en python
            match entrada:
                case 1:
                    submenu1=(input(f'SubMenu \n1.Ingreso Carro\n2.Ingreso Moto\nOpcion: '))
                    if submenu1.isdigit():
                        tipo=int(submenu1)
                        try:
                            match tipo:##switch anidado
                                case 1:
                                    print("---------------------------------------")
                                    if capacidadCarros > 0:
                                        placa = input("Ingrese placa: ")
                                        if  len(placa)==6:
                                            if placaExiste(placa) == True:
                                                print('La placa ya esta ingresada')
                                            else:
                                                if ingresoVehiculo(placa,tipo) == True:
                                                    capacidadCarros -= 1
                                                else:
                                                    print("Error al ingresar Vehiculo")
                                        else:
                                            print("Error al ingresar la Placa")
                                    else:
                                        print('El parqueadero esta lleno, vuelva mas tarde')
                                case 2:
                                    print("----------------------------------")
                                    if capacidadMotos > 0:
                                        placa = input("Ingrese placa: ")
                                        if len(placa) == 6 or len(placa)==5:
                                            placaExiste(placa)
                                            if placaExiste(placa) == True:
                                                print('La placa ya esta ingresada')
                                            else:
                                                if ingresoVehiculo(placa, tipo) == True:
                                                    capacidadMotos -= 1
                                                else:
                                                    print("Error al ingresar Vehiculo")
                                        else:
                                            print("Error al ingresar la Placa")
                                    else:
                                        print('El parqueadero esta lleno, vuelva mas tarde')
                                case _:
                                    print('Opcion no valida')
                        except valueError:
                            print("Error 400")
                    else:
                        print("Lo digitado no es un numero")
                case 2:
                    submenu2 = (input(f'SubMenu \n1.Salida Carro\n2.Salida Moto\nOpcion :'))
                    if submenu2.isdigit():
                        tipo=int(submenu2)
                        try:
                            match tipo:
                                case 1:
                                    print("----------------------------------------")
                                    placa = input('Ingrese la placa del Carro: ')
                                    if placaExiste(placa) == True:
                                        if salidaVehiculo(placa, tipo):
                                         capacidadCarros += 1
                                    else:
                                        print('El vehiculo no se encuentra registrado')
                                case 2:
                                    print("----------------------------------------")
                                    placa = input('Ingrese la placa del Moto : ')

                                    if placaExiste(placa)==True:
                                        if salidaVehiculo(placa,tipo):
                                            capacidadMotos += 1
                                    else:
                                        print('El vehiculo no se encuentra registrado')
                                case _:
                                    print('Opcion no valida')
                        except valueError:
                            print("Error 404")
                    else:
                        print("Lo digitado no es un numero")
                case 3:
                    submenu3=(input(f'Submenu Reportes\n1.Reporte General\n2.Ocupacion Actual\nOpcion: '))
                    if submenu3.isdigit():
                        tipoReporte = int(submenu3)
                        try:
                            match tipoReporte:
                                case 1:
                                    total=0
                                    for v in reportes:
                                        total+=v['Costo']
                                        print(v)
                                    print(f'Total recaudado a la fecha: {total}')
                                case 2:
                                    for v in parqueadero:
                                        print(v)
                                case _:
                                    print("Error en la opcion")
                        except valueError:
                            print("Error 404")
                    else:
                        print("Lo digitado no es un numero")
                case 4:
                    print("Hasta la vista Baby....")
                    caso=1
                case _:
                    print("Error opcion no valida")
        except valueError: ## este es el except que cierra el try inicial
            print("error 404")
    else:# cierre del if inicial
        print("Lo digitado no es un numero")