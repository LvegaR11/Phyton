#Punto 1 de la actividad
def calcular(edad):
    if edad < 18:
        print("Usted aun es menor de edad")
    elif edad >= 18 and edad <= 65:
        print("Usted es mayor de edad")
    else:
        print("Usted es una persona de la tercera edad")

print("Por favor ingrese su edad")
edad = input()
print(f"Su edad es {edad}")
calcular(int(edad)) 