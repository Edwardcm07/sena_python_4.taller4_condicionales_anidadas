#TALLER 4 PYTHON
#AUTOR: EDUAR ALEJANDRO CANO MONTOYA
#FECHA:21 de septiembre de 2022

from datetime import date
hoy=date.today()   #fecha actual
print("Hoy es el dia: ", hoy)
print()
print("EJERCICIO DE LAS CLASES DE TRIANGULOS")
a=int(input("digite el valor de A: "))
b=int(input("digite el valor de B: "))
c=int(input("digite el valor de C: "))

if a==b and a==c and b==c:
    print("EL TRIANGULO ES EQUILATERO")
else:
    if a==b or a==c or a==c:
        print("EL TRIANGULO ES ISOCELES")
    else:
        print("EL TRIANGULO ES ESCALENO")
print()
animal=input("digite un animal: ")
animal=animal.upper()
if animal=="PERRO":
    print("Este aniaml es el mejor amigo del hombre: ", animal)
elif animal=="GATO":
    print("Este animal persigue a los ratones: ", animal)
elif animal=="OSO":
    print("Este animal vive en el polo norte: ", animal)
else:
    print("No es un PERRO, no es un GATO, ni es un OSO... es: ", animal)
print()
print("FIN")
