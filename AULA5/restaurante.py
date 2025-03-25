# um restaurante recebe pedidos de clientes e os coloca em uma fila para a cozinha. Cada pedido tem um nome e um tempo estimado de preparo. Crie um programa que adicione pedidos à fila e exiba a ordem de preparo. Ao servir um pedido, remova o da fila e exiba quem será servido em suida.

fila_cozinha = []

while True:
    opcao = int(input('[1] Realizar pedido | [2] Servir pedido | [0] Encerrar programa: '))
    match opcao:
        case 1:
            pedido = [str(input('Nome do prato: ')), int(input('Tempo de preparo (min): '))]
            fila_cozinha.append(pedido)
            fila_cozinha.sort(key=lambda x: x[1])
        case 2:
            fila_cozinha.pop(0)
        case 3:
            print('Encerrando programa...')
            break
        case _:
            print('Opção inválida. Tente novamente.')
    print(fila_cozinha)
