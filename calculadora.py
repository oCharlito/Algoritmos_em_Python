def calculadora():
    numero1 = int(input('Digite o número 1: '))
    operacao = input('Digite a operação (+, -, /): ')
    numero2 = int(input('Digite o número 2: '))

    resultado = 0

    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '/':
        resultado = numero1 / numero2
    else:
        print('Operação inválida')
        return

    print(f'{numero1} {operacao} {numero2} = {resultado}')

# Chamar a função calculadora
calculadora()
