fila = []

while True:
    
    op = input('Digite A para ADD ou R para remover: ')

    if op == 'A':
        nome = input('Digite o nome: ')
        fila.append(nome)
    elif op == 'R':
        removido = fila.pop(0)
        print(f'{removido} foi atendido!')
    elif op == 'S':
        break
    else:
        print('Opção inválida!')
    print(fila)