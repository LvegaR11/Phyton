#Punto 2 de la actividad
flag = True
def calcular(edad):
    if edad < 18:
        print("Usted es aun es menor de edad")
    elif edad >= 18 and edad <= 65:
        print("Usted es mayor de edad")
    else:
        print("Usted es una persona de la tercera edad")

while flag:
    try:
        print("Por favor ingrese su edad")
        edad = input()
        print(f"Su edad es {edad}")
        calcular(int(edad))
        flag = False
    except:
        print("Usted no ingreso un valor valido")