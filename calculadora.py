while True:
    def soma(num1,num2):
        print(f'Seu resultado é: {num1 + num2}')
    def subtração(num1,num2):
        print(f'Seu resultado é: {round(num1 - num2,2)}')
    def multiplicação(num1,num2):
        print(f'Seu resultado é: {num1 * num2}')   
    def divisão(num1,num2):
        try:
            print(f'Seu resultado é: {round(num1 / num2,2)}')  
        except ZeroDivisionError:
            print('Não é possível dividir por 0') 
    def potenciacao(num1,num2):
        print(f'Seu resultado é: {num1 ** num2}')  
    def porcentagem(num1,num2):
        print(f'Seu resultado é: {num1 * num2 / 100}')
    def raiz(num1,num2):
        try:
            print(f'Seu resultado é: {num1 ** (1/num2)}')
        except ZeroDivisionError:
            print('Não é possível dividir por 0') 
    while True:
        try:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            break
        except ValueError:
            print('Digite um número')
    escolha = input('''Escolha uma função:
[somar] [subtrair] [multiplicar] [dividir] [potenciar] [porcentagem] [raiz quadrada]
-> ''')
    if escolha == 'somar':
        soma(num1,num2)
    if escolha == 'subtrair':
        subtração(num1,num2)
    if escolha == 'multiplicar':
        multiplicação(num1,num2)
    if escolha == 'dividir':
        divisão(num1,num2)
    if escolha == 'potenciar':
        potenciacao(num1,num2)
    if escolha == 'porcentagem':
        porcentagem(num1,num2)
    if escolha == 'raiz quadrada':
        raiz(num1,num2)
    continuar = input('Deseja continuar? [sim] [não] ')
    if continuar == 'não':
        break