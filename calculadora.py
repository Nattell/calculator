# "3+4"  ---> 7

# 1. Recoger datos del usuario
primer_numero = input("primer numero:")
operacion = input("operacion:")
segundo_numero = input("segundo numero:")

# 1.5 Convertir las str en 2 int
primer_numero = int(primer_numero)
segundo_numero = int(segundo_numero)

# 2. Calcular el resultado

if operacion == "+":
    print(primer_numero + segundo_numero)
elif operacion == "-":
    print(primer_numero - segundo_numero)
elif operacion == "*":
    print(primer_numero * segundo_numero)
elif operacion == "/":
    print(primer_numero / segundo_numero)
else:
    print("ninguna operacion es viable")
    exit()
