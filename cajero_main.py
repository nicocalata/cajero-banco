import time
import pwinput
from usuario import *
#Cajero

dinero_actual = 100000
contenedor = ContenedorDeUsuarios()

def registrarse():
    print("\tRegistrarme")
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    clave = pedir_valor("Ingrese la contraseña: ")
    usuario=Usuario(nombre_usuario,clave)
    contenedor.registrar_usuario(usuario)
    print("Registro terminado\n---------------------")
  
def pedir_valor(texto):
    while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print("\033[;33m""Tiene que ser un valor numérico""\033[;37m")

def hora_y_fecha():
    return "Dia: "+time.strftime("%d/%m/%y")+"\nHora: "+time.strftime("%H:%M:%S")

def ticket_(var_retirar,saldo_actual):
    print("\n""\t---BANCO---"+"\nRetiraste: $"+str(var_retirar)+"\nSaldo Actual: $"+str(saldo_actual))
    print(hora_y_fecha(),"\n")

def depositar():
    user = input("Ingrese su usuario: ")
    password = pedir_valor("Ingrese su contraseña: ")
    user = contenedor.validar_usuario(user,password)
    if (user):
        monto=pedir_valor("Ingrese el monto a depositar: ")
        if monto>0:
            user.depositar(monto)
        else:
            print("El monto a depositar no puede ser menor a 0 ")
    else:
        print("Usuario y/o clave inválida\n---------------------")

def extraer():
    usuario = input("Ingrese su usario: ")
    try:
        ingreso_clave = int(pwinput.pwinput(prompt="Ingrese su clave: "))
    except ValueError:
        print("\033[;33m""La clave es numérica""\033[;37m")
        return 
    user = contenedor.validar_usuario(usuario,ingreso_clave)
    if user:
        retirar = pedir_valor("Extraccion: ")
        if retirar <0:
            print("El monto a extraer no puede ser menor a 0 ")  
            return
        if user.verificar_extraccion(retirar):
            user.extrae(retirar)
        else:
            print("No hay dinero suficiente")
            return
        ticket = input("Desea retirar ticket?\n Y / N ").lower()
        if ticket == "y":
            ticket_(retirar,user.plata)
            return
        else:
            return 
    else:
        print("Usuario y/o clave inválida\n---------------------")
        return

def get_saldo ():
    user = input("Ingrese su usuario: ")
    password = pedir_valor("Ingrese su contraseña: ")
    user = contenedor.validar_usuario(user,password)
    if (user):
        print("Saldo Actual: "+str(user.plata))
    else:
        print("Usuario y contraseña incorrecta\n---------------------")

print("\tBienvenido al Banco ")
while True:
    print("\n1) Extraccion\n2) Depósito\n3) Saldo actual\n4) Registrarse\n5) Salir")
    opcion = input()
    if opcion == "1":
        extraer()
    elif opcion == "2":
        depositar()
    elif opcion == "3":
        get_saldo()
    elif opcion == "4":
        registrarse()
    elif opcion == "5":
        print("Que tenga un buen día\n---------------------")
        break
    else:
        print("Opción inválida\n---------------------")

