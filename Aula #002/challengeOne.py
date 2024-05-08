# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 01:44:42 2024

@author: Isaque Gabriel

Crie um programa que o usuário forneça os três lados de um triângulo e o programa
diga se ele é: acutângulo, retângulo ou obtusângulo.

ACUTÂNGULO = Todos os ângulos do triângulos são menores que 90°
RETÂNGULO = Quando um dos ângulos têm 90°
OBTUSÂNGULO = Um dos ângulos do triângulos for maior que 90°

TEORIA

A^2 < B^2 + C^2 = ACUTÂNGULO
A^2 = B^2 + C^2 = RETÂNGULO
A^2 > B^2 + C^2 = OBTUSÂNGULO

OPERADORES

==
!=
>
<
>=
<=

OPERADORES LÓGICOS
AND
OR
NOT

"""

print('\n' * 50)
print('=' * 30)
print(' Classificador de Triângulos')
print('=' * 30)

# Variáveis

A = float(input('Digite o maior lado do triângulo:'))
B = float(input('Digite o segundo lado do triângulo:'))
C = float(input('Digite o terceiro lado do triângulo:'))

if A**2 < (B**2 + C**2) :
    print('-' * 50)
    print('O Seu triângulo é classificado como: Acutângulo')
    print('-' * 50)
    
elif A**2 == (B**2 + C**2) :
    print('-' * 50)
    print('O Seu triângulo é classificado como: Retângulo')
    print('-' * 50)
    
elif A**2 > (B**2 + C**2) :
    print('-' * 50)
    print('O Seu triângulo é classificado como: Obtusângulo')
    print('-' * 50)



