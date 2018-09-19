numero = int(input("ingresa el numero uno:"))
numero2 = int(input("ingresa el numero dos:"))

print("MENU")
print("1) MULTIPLICACIÓN")
print("2) DIVICIÓN")
print("3) SUMA")
print("4) RESTA")


opcion=input("Selecciona el tipo de operación que quieres realizar")

if opcion == "1":
    mult = numero * numero2
    print("El resultado de la multiplicacion es:", mult)

if opcion == "2":
    div = numero / numero2
    print("El resultado de la divición es:", div)

if opcion == "3":
    sum = numero + numero2
    print("El resultado de la suma es:", sum)

if opcion == "4":
    res = numero - numero2
    print("El resultado de la resta es:", res)



