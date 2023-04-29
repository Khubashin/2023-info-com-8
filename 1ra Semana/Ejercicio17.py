frase=input('Escriba una frase: ')
fraseCadena=frase.split(" ")
indice=0
for i in range(len(fraseCadena)):
    indice+=1
    print(f'{fraseCadena[indice*(-1)]}', end=" ")