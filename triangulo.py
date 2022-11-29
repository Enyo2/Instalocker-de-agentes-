print("Calculadora de area de triangulos")
print("Introduzca el valor de una base y de una altura")
base = input()
altura = input()
base_int = int(base)
altura_int = int(altura)
area = base_int * altura_int / 2
print("Su area es {}".format(area))