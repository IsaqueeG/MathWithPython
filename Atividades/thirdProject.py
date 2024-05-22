# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:54:19 2024

@author: Isaque Gabriel
"""
import random

print('\n' * 50)
print('-' * 50)
print('QUIZ MATEMÁTICO')
print('-' * 50)

verifier = 1

while verifier != 0:
    operator = random.randint(0, 2) # 0 - Soma 1 - Subtração 2 - Multiplicação 3 - Divisão
    firstElement = random.randint(0, 20)
    secondElement = random.randint(0, 20)
    
    # Soma
    if operator == 0:
        answerSum = firstElement + secondElement
        question = int(input('Quanto é {} + {}\n'.format(firstElement, secondElement)))
        if question == answerSum:
            print('Parabéns! Você Acertou\n')
        else:
            print('Resposta Errada. A resposta correta é {}\n'.format(answerSum))
    
    # Subtract
    if operator == 1:
        elementsOrder = random.randint(0, 1)
        
        # Elemento 1 - Elemento 2
        if elementsOrder == 0:
            answerSubtract = firstElement - secondElement
            question = int(input('Quanto é {} - {}?\n'.format(firstElement, secondElement)))
        
        # Elemento 2 - Elemento 1
        elif elementsOrder == 1:
            answerSubtract = secondElement - firstElement
            question = int(input('Quanto é {} - {}?\n'.format(secondElement, firstElement)))
            if question == answerSubtract:
                print('Parabéns! Você Acertou\n')
            else:
                print('Resposta Errada. A resposta correta é {}\n'.format(answerSubtract))
                
    # Multiply
    if operator == 2:
        answerMultiply = firstElement * secondElement
        question = int(input('Quanto é {} x {}\n'.format(firstElement, secondElement)))
        if question == answerMultiply:
            print('Parabéns! Você Acertou\n')
        else:
            print('Resposta Errada. A resposta correta é {}\n'.format(answerMultiply))
            
    playAgain = input('Deseja jogar novamente? (S/N)\n').upper()
    if playAgain != 'S':
        print('Obrigado Por Jogar!')
        break