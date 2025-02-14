def soma(*args):
    args = sum(args)
    print(args)
soma(1,2,3,4,5)

def media(*args):
    args = sum(args)/len(args)
    print(args)
media(1,2,3,4,5)

def juntar_strings(*args):
    resultado = ""
    for i in range(len(args)):
        resultado += str(args[i])
        if i < len(args) - 1:
            resultado += " "
    return resultado

print(juntar_strings("Python", "é", "bom!", 2025)) 

