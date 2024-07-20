texto = input("Digite palavras, que eu direi qual é a maior delas: ")

palavras = texto.split()

maior_palavra = max(palavras, key=len)

print("A maior palavra é:", maior_palavra)