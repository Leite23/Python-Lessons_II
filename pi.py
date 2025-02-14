def calcular_pi(n):
    pi = 0.0
    for i in range(n):
        pi += (1/(16**i))*((4/(8*i+1)) - (2/(8*i+4)) - (1/(8*i+5)) - (1/(8*i+6)))
    return pi

n = 90
pi = calcular_pi(n)
print(f"O valor de Pi é aproximadamente {pi:.{n}f}")