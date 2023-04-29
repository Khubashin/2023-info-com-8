fecha=input('Ingrese la Fecha actual en formato DD/MM/AAAA: ')
nacimiento=input('Ingrese su Fecha de Nacimiento en formato DD/MM/AAAA: ')

lista1=fecha.split("/")
lista2=nacimiento.split("/")

print(f'Su edad aproximada es de {int(lista1[2])-int(lista2[2])} años.')