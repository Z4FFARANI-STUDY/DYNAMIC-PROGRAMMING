prioridade_alta = []
prioridade_baixa = []

while True:
    continuar = int(input('[1] Adicionar cliente | [2] Atender cliente | [0] Encerrar programa: '))
    match continuar:
        case 1:
            cliente = str(input('Nome do cliente: '))
            prioridade = int(input('[1] Alta prioridade | [2] Baixa prioridade: '))
            prioridade_alta.append(cliente) if prioridade == 1 else prioridade_baixa.append(cliente) if prioridade == 2 else print('Opção inválida')
        case 2:
            prioridade_alta.pop(0) if len(prioridade_alta) > 0 else prioridade_baixa.pop(0)
        case 0:
            print('Encerrando programa...')
            break
        case _:
            print('Opção inválida. Tente novamente')
            continue
    print(
f'''
PRIORIDADE ALTA:
{prioridade_alta}

PRIORIDADE BAIXA:
{prioridade_baixa}
''')
