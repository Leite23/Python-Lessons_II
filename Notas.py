n = int(input('Digite a qde de notas: '))

notas = []
for i in range(n):
    notas.append(float(input('Nota a ser add: ')))

soma = 0
for i in notas:
    soma += i
    
print(f'Media: {soma/len(notas)}')
