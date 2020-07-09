# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:58:24 2020

@author: Angela
"""
#Ejercicio ara determinar si un aumno a aprobado


def determinaraprobado(promedio):
    if promedio >= 11:
        resultado = 'Aprobado'
    else:
        resultado = 'Desaprobado'
    return resultado

promedio = int(input("Promedio: "))
print(determinaraprobado(promedio))