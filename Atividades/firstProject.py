
"""

Criado em Ter. Mar. 26 23:15:12 2024
@author: Isaque Gabriel

Desafio #001
Crie um programa que o usuário forneça o valor da Diagonal maior ( D) , da 
diagonal menor (d) e o programa exiba o valor da área do losango. Pesquise a 
fórmula da área do losango. 

"""

# Menu
print('\n' * 100)
print('=' * 50)
print("Calculadora de Área do Losango")
print('=' * 50)

# Variáveis
greaterDiagonal = float(input('Digite o valor da Diagonal maior (D):'))
minorDiagonal = float(input('Digite o valor da Diagonal menor (d):'))

# Área Do Losango = (D * d) / 2
diamondArea = (greaterDiagonal * minorDiagonal) / 2

# Resultado
print(f'A Área do losango solictado com base nos dados fornecidos é: {diamondArea}')

