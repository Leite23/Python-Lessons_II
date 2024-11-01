    
notas = [1,4,10]
def media(notas):
    soma = 0
    for i in notas:
        soma += i
    media = soma/len(notas)    
    return media

y = [1,4,10]
print(media(y))

z = [1,10,10]
print(media(z))