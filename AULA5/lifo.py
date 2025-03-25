fila = []

while True:
    opcao = int(input('[1] Adicionar cliente | [2] Atender cliente | [3] Sair da estrutura: '))
    match opcao:
        case 1:
            cliente = str(input('Nome do cliente: '))
            fila.append(cliente)
            print(f"Cliente {cliente} adicionado a fila!")
        case 2:
            atendido = fila.pop(-1)
            print(f"Atendendo: {atendido}.")
        case 3:
            print("Encerrando atendimento...")
            break
        case _:
            print('Fila vazia!')
    print(fila)