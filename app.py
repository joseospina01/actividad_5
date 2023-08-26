def ejercicio_1():
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")

def ejercicio_2():
    limite = int(input("Ingresa un número límite: "))
    suma = 0
    for i in range(1, limite + 1):
        suma += i
    print("La suma de los números del 1 al", limite, "es:", suma)

def ejercicio_3():
    num = int(input("Ingresa un número: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de", num, "es:", factorial)

def ejercicio_4():
    base = float(input("Ingresa la base: "))
    exponente = int(input("Ingresa el exponente: "))
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    print(base, "elevado a la", exponente, "es:", resultado)

def ejercicio_5():
    while True:
        contraseña = input("Ingresa la contraseña (debe tener al menos 8 caracteres): ")
        if len(contraseña) >= 8:
            print("Contraseña válida. ¡Registro exitoso!")
            break
        else:
            print("La contraseña es demasiado corta. Inténtalo nuevamente.")

def main():
    while True:
        print("Menú de ejercicios:")
        print("1. Par o impar")
        print("2. Suma de números")
        print("3. Factorial")
        print("4. Potencia")
        print("5. Registro con contraseña")
        print("6. Salir")
        
        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 6:
            print("¡Hasta luego!")
            break
        elif opcion == 1:
            ejercicio_1()
        elif opcion == 2:
            ejercicio_2()
        elif opcion == 3:
            ejercicio_3()
        elif opcion == 4:
            ejercicio_4()
        elif opcion == 5:
            ejercicio_5()
        else:
            print("Opción inválida. Selecciona nuevamente.")

if __name__ == "__main__":
    main()


