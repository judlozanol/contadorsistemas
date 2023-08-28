from binario import Binario
from decima import Decimal
from octal import Octal
from hexadecimal import Hexadecimal

condicion=5
while condicion>=5 or condicion<=0:
    try:
        condicion= int(input("Ingrese la clave numérica del sistema en el que desea contar:\n\tBinario(1)\n\tOctal(2)\n\tDecimal(3)\n\tHexadecimal(4)\n "))
        if condicion>=5 or condicion<=0:
            print("Condición Invalida") 
    except ValueError:
        print("Condición Invalida")

if condicion==1:
    p=Binario()
elif condicion==2:
    p=Octal()
elif condicion==3:
    p=Decimal()
elif condicion==4:
    p=Hexadecimal()
input("Presione enter para Iniciar el conteo...")
for i in range(101):
    print(p.valor)
    p.avanzar()
