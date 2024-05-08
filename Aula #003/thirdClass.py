# ESTRUTURAS DE REPETIÇÃO

"""
WHILE => ENQUANTO
FOR => PARA
range() => Gera uma sequência de números dentro de uma faixa específica.
range(<quantidade_de_numeros_a_serem_gerados>)
range(<inicio_da_faixa>,<fim_da_faixa>,[,<incremento])

for<variavel> in range([maneira_1|maneira_2])

MÉDIA ARITMÉTICA: X = X1 + X2 + X3 + ... Xn / n
MÉDIA GEOMÉTRICA:   X = raiz enesima(X1 * X2 * X3 ... * Xn)
"""

"""
print('\n' * 100)
print('-' * 40)
print('  Programa para o cálcula da média')
print('-' * 40)
n = int(input('Quantos Números Deseja Calcular A Média Aritmética? '))
print('-' * 40)
i = 1
b = 0

while i <= n:
    a = float(input(f'Digite o {i}º Número:'))
    b += a
    i += 1
    c = b / n

print('\n' * 2)
print('-' * 100)
print(f'A média aritmética dos números informados é {c}')
print('\n' * 100)
"""

"""
a=list(range(10,25,3))
print(a)
"""

print('\n' * 100)
print('-' * 40)
print('  Programa para o calcular a Média Geométrica')
print('-' * 40)
n = int(input('Quantos Números Deseja Calcular A Média Geométrica? '))
print('-' * 40)
i = 1
b = 1
for cont in range(n):
    a = float(input(f'Digite o {i}º número:'))
    i += 1
    b = a * b
c = (b)**(1/n)
print('\n' * 3)
print('-' * 40)
print(f'A média geométrica dos números informados é {c}')
print('\n' * 40)

