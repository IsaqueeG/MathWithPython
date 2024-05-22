# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:44:04 2024

@author: Isaque Gabriel
Desenvolva um programa que fatore polinômios
"""

from sympy import *

print('\n' * 50)
print('-' * 50)
print('FATORADOR DE POLINÔMIOS')
print('-' * 50)

polynomialVar = input('Digite O Polinômio:\n')
factoredPolynomia = factor(polynomialVar)

print('\n' * 2)
print('-' * 50)
print(factoredPolynomia)
print('-' * 50)