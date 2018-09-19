mi_lista = []

input_usuario =""

input_usuario = input("que quieres comprar? (escribe FIN para salir):")

while input_usuario != "FIN":
    mi_lista.append(input_usuario)
    input_usuario= input("que quieres comprar? (escribe FIN para salir):")
#1
largo_lista= len(mi_lista)
indice_actual=  0

while indice_actual < largo_lista:
    print("tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual += 1
# El for hace la misma función que lo puesto a partir del numero 1
for item in mi_lista:
    print("tengo que comprar {}".format(item))

print("esta es la lista de la compra")
