##Importacion de paquetes para captura
import math
from datetime import datetime
from operator import length_hint

## declaracion de variables
parqueadero = []
reportes =[]
capacidadCarros = 3
capacidadMotos = 2
vehiculo = {}
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
        return print("Error, Placa no existe")
#funcion para ingreso de vehiculos
def ingresoVehiculo(placa, tipo):
    horaIngreso = capturaHora()
    nuevoVehiculo = {}
    match tipo:
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
    horaSalida =capturaHora()
    for v in parqueadero:
        if v["Placa"].lower()==placa.lower():
            v['Hora Salida']=horaSalida
            # cambio el formato de String a numeros para calcular el tiempo
            h_Ingreso=datetime.strptime(v['Hora Ingreso'],calculoFormato)
            h_Salida=datetime.strptime(v['Hora Salida'],calculoFormato)
            #Calcular el tiempo en minutos para el cobro
            #print(f'ingreso :{h_Ingreso}' )
            #print(f'salida :{h_Salida}')
            tiempoMinutos= (h_Salida-h_Ingreso).total_seconds()/60
            #print(f'tiempo en minutos:{tiempoMinutos}')
            #calculo del tiempo en horas
            tiempoHora = math.ceil(tiempoMinutos/60)
            #print(f'tiempo horas:{tiempoHora}')
            match tipo:
                case 1:
                    if  v['Tipo'] =='Carro':
                        if tiempoHora ==0:
                            v['Costo'] = costoCarros
                            reportes.append(v)
                            parqueadero.remove(v)
                            return imprimirFactura(placa)
                        else:
                            costoParqueadero=costoCarros*tiempoHora
                            v['Costo']=costoParqueadero
                            reportes.append(v)
                            parqueadero.remove(v)
                            return imprimirFactura(placa)
                    else:
                        print(f'la placa :{v["Placa"]} no corresponde al tipo de vehiculo')
                        return False
                case 2:
                    if v['Tipo'] == 'Moto':
                        if tiempoHora ==0:
                            v['Costo'] = costoMotos
                            reportes.append(v)
                            parqueadero.remove(v)
                            return imprimirFactura(placa)
                        else:
                            costoParqueadero=costoMotos*tiempoHora
                            v['Costo']=costoParqueadero
                            reportes.append(v)
                            parqueadero.remove(v)
                            return imprimirFactura(placa)
                    else:
                        print(f'la placa :{v["Placa"]} no corresponde al tipo de vehiculo')
                        return False
                case _:
                    mensaje = "Error_"
                    return mensaje
        else:
            mensaje = "placa no existe"
            return mensaje

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
    opcion = int(input (f'Menu Principal \n1.Ingresar Vehiculo\n2.Salida Vehiculo\n3.Reportes\n4.Salir\nOpcion: '))
    print('******************************************')

    calculoFormato='%H:%M:%S'
    ##Este es la manera de realizar un switch en python
    match opcion:
        case 1:
            tipo = int(input(f'SubMenu \n1.Ingreso Carro\n2.Ingreso Moto\nOpcion: '))
            match tipo:##switch anidado
                case 1:
                    print("---------------------------------------")
                    if capacidadCarros > 0:
                        placa = input("Ingrese placa: ")
                        if  len(placa)==6:
                            placaExiste(placa)
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
        case 2:
            tipo = int(input(f'SubMenu \n1.Salida Carro\n2.Salida Moto\nOpcion :'))
            match tipo:
                case 1:
                    print("----------------------------------------")
                    placa = input('Ingrese la placa del Carro: ')
                    if placaExiste(placa) == True:
                        if salidaVehiculo(placa, tipo) != False:
                         capacidadCarros += 1
                    else:
                        print('El vehiculo no se encuentra registrado')
                case 2:
                    print("----------------------------------------")
                    placa = input('Ingrese la placa del Moto : ')

                    if placaExiste(placa)==True:
                        if salidaVehiculo(placa,tipo)!= False:
                            capacidadMotos += 1
                    else:
                        print('El vehiculo no se encuentra registrado')
                case _:
                    print('Opcion no valida')
        case 3:
            print("-------------------------------------")
            tipoReporte=input(f'Submenu Reportes\n1.Reporte General\n2.Ocupacion Actual\n3.Reporte vehiculos retirados\nOpcion: ')

        case 4:
            print("Hasta la vista Baby....")
            caso=1

        case _:
            print("Error opcion no valida")