print("Bienvenido a la encuesta de datos basico : ")

nombre = input("Por favor ingrese su nombre : ")

comida_favorita = input("¿Cual es su comida favorita? :  ")
dinero_disponible = int(input("¿Cuanto dinero tiene en su cartera? : "))

while True:
    clima_favorito = input("¿Te gusta el clima frio? (si/no) : ")
    if clima_favorito == 'si':
        clima_frio = True
        break
    elif clima_favorito == 'no':
        clima_frio = False
        break
    else:
        print("Por favor, ingrese 'si' o 'no' ")

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
        edad = int(input("por favor ingrese su edad : "))
        print(f"Su edad es {edad}")
        calcular(int(edad))
        flag = False
    except:
        print("Usted no ingreso un valor valido")

print("Gracias por completar el formulario")

print("Su informacion es:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Comida favorita: {comida_favorita}")
print(f"Dinero disponible: {dinero_disponible}")
print(f"Clima frio: {clima_frio}")