from time import *

hora = 24
minuo = 60

for hora in range(hora):
    for minuo in range(minuo):
        print(f'{hora:02}:{minuo:02}')
        sleep(5)