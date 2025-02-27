numeros = []

quantidade = int(input("Digite um número: "))

for i in range(quantidade):
    numero = float(input("Digite um valor para formar a lista: "))
    numeros.append(numero)

print("A lista com os respectivos números são:", numeros)

###################################################################

numeros = []

quantidade = int(input("Digite um número: "))

i = 0

while i < quantidade:
    numero = float(input("Digite um valor para forma"))
    numeros.append(numero)
    i += 1

print("A lista com os respectivos números são: ", r)


####################################################################

lista = [10, 20, 30, 40, 50]

alvo = 30

for k in range(len(lista)):
    if k == alvo:
        print(f"O alvo está na posição {k}")
        break
    else:
        print("Alvo não encontrado!")