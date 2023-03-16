# calculadora simples

while ...:

    operadores_permitidos = '+-*/'
    numeros_validos = None

    try:
        entrada_1 = float(input('Digite um número\n'))
        entrada_2 = float(input('Digite outro número\n'))

        numeros_validos = True
    except:
        numeros_validos = None

    operador = input('Digite o operador (+, -, /, *)')

    if numeros_validos is None:
        print('Algum valor digitado é inválido')
        continue

    if len(operador) > 1:
        print('Você digitou mais de um operador.')
        continue
    
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

#####################
    if operador == '+':
        soma = entrada_1 + entrada_2
        print(soma)
    elif operador == '-':
        sub = entrada_1 - entrada_2
        print(sub)
    elif operador == '*':
        multi = entrada_1 * entrada_2
        print(multi)
    elif operador == '/':
        div = entrada_1 / entrada_2
        print(div)
    else:
        print('Não é pra isso acontecer')


    sair = input('Deseja sair? [s]im ').lower().startswith('s')
    
    if sair:
        break 

