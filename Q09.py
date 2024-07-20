numeros = input('Digite uma lista de números separados por espaço: ' ).split()

if numeros:
    menor_num = min(map(float, numeros))
    print("O menor numero da lista é: ", menor_num)
else:
    print('A lista está vazia.')