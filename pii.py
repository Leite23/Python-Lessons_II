def pi():
    soma = 0
    for i in range(10000000):
        soma += (-1)**(i)*4/(2*i+1)
    return soma

print(pi())