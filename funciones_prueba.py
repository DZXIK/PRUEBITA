#imports
import numpy as np
import time
import os
import random
#limpiar pantalla
os.system("cls")
#matriz
habitaciones = np.zeros((2,5),int)
#listas
lista_ruts_clientes=[]
lista_nombres_clientes=[]
lista_nombres_mascotas=[]
lista_cantidad_dias=[]
lista_id=[]
#funciones de menu e Ingresar
def mostrar_menu():
    print("""\t\tBienvenido a Mascota Segura\t\t\n un lugar seguro para tu mascota
    
    1. Ingresar Bascota
    2. Buscar Mascota
    3. Retirar Mascota y pagar
    4. Cancelar Procedimiento""")
def validar_opcion():
        while True:
            try:
                opcion = int(input("Ingrese opción: "))
                if opcion >= 1 and opcion <= 4:
                    return opcion
                else:
                    print("¡ERROR! ¡OPCIÓN INVALIDA!")
            except:
                print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su RUT sin puntos ni dígito verificador: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("¡ERROR! ¡INGRESE UN RUT VÁLIDO!")
        except:
            print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_nombre():
    while True:
        nombre = input("Ingrese el primer nombre del cliente: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha() and not nombre.isspace():
            return nombre
        else:
            print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")
def validar_nombre_mascota():
    while True:
        nombre = input("Ingrese nombre de la mascota: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha() and not nombre.isspace():
            return nombre
        else:
            print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")
def validar_dias():
    print("Días de hostadia")
    while True:
        try:
            cantidad_dias = int(input("cuantos dias desea dejar a la mascota?: "))
            if cantidad_dias > 0:
                return cantidad_dias
            else:
                print("ERROR!! DEBE QUEDARSE AL MENOS UN DIA")
        except:
            print("ERROR!! DEBE INGRESAR SOLO NUMEROS ENTEROS")
#funciones para buscar mascota
def buscar_mascota():
    buscar=int(input("Ingrese el rut del cliente para buscar su mascota: "))

#Funciones Para cargar
def ingrear_mascota():
    os.system("cls")
    print("""
    \t\tHola!! así que deseas ingresar una mascota mascota
    \t\t--------------------------------------------------
    \t\t ingresa los datos que se solicitan""")
    validar_rut()
    lista_ruts_clientes.append
    validar_nombre()
    validar_nombre_mascota()
    validar_dias()


#falta hacer el grabar con los validar