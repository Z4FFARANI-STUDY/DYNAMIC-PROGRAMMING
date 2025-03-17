fila = []

while True:
    cliente = input('Digite o nome do cliente ou fim para sair: ')
    if cliente.lower() == 'fim':
        break
    fila.append(cliente)
    print(f'Cliente {cliente} adicionado a fila.')

while fila:
    atendido = fila.pop(0)
    print(f"Atendendo: {atendido}")

print("Todos os clientes foram atendidos!")
