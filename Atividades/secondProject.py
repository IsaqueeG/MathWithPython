"""
Criado na Qua. Mar. 27 00:23:03 2024
Projeto #002
Autor: Isaque Gabriel

Crie um programa que o usuário DECIDA SE DESEJA CALCULAR O VOLUME DO 
CUBO , DO PARALELEPIPEDO RETÂNGULO E DO CILINDRO (use pi=3,14), 
SOLICITE DO USUÁRIO AS INFORMAÇÕES NESCESSÁRIA PARA ENCONTRAR O 
VOLUME DESEJADO. Pesquise as fórmulas dos volumes do Cubo, 
do paralelepípedo retângulo e do Cilindro.
"""

PI = 3.14

print('\n' * 50)
print('=' * 25)
print(' Calculadora de Volume')
print('=' * 25)

# Menu
print('Escolha Uma Opção:\n')
print('[1] Volume Do Cubo\n[2] Volume Do Paralelepípedo Retângulo\n[3] Volume Do Cilindro\n')
value = int(input('>'))

if value == 1:
    cubeSize = float(input('Digite o tamanho de um dos lados do cubo:\n>'))
    cubeVolume = cubeSize ** 3
    print('-' * 20)
    print('Volume Do Cubo: {:.1f}'.format(cubeVolume))
    print('-' * 20)

elif value == 2:
    heightForm = float(input('Digite a altura do seu Paralelepípedo Retângulo:\n>'))
    firstSideForm = float(input('Digite o tamanho de um lado da base retangular:\n>'))
    secondSideForm = float(input('Digite o tamanho do outro lado da base retangular:\n>'))
    
    formVolume = heightForm * firstSideForm * secondSideForm
    print('-' * 40)
    print('Volume Do Paralelepípedo Retângulo: {:.1f}'.format(formVolume))
    print('-' * 40)

elif value == 3:
    radiusCylinder = float(input('Digite o raio do seu cilindro:\n>'))
    heightCylinder = float(input('Digite a altura do seu cilindro:\n>'))
    
    cylinderVolume = PI * radiusCylinder ** 2 * heightCylinder
    print('-' * 25)
    print('Volume Do Cilindro: {:.1f}'.format(cylinderVolume))
    print('-' * 25)



 