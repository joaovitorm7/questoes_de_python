numeros = input('Digite uma lista de números: ').split()

numeros = [int(num) for num in numeros]
print('Números ímpares :')

for num in numeros:
    if num % 2 != 0:
        print(num)