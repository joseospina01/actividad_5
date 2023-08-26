def ejercicio1():
    # Implementa aquí el código para el ejercicio 1

def ejercicio2():
    # Implementa aquí el código para el ejercicio 2

def ejercicio3():
    # Implementa aquí el código para el ejercicio 3

def ejercicio4():
    # Implementa aquí el código para el ejercicio 4

def ejercicio5():
    # Implementa aquí el código para el ejercicio 5

def main():
    while True:
        print("Menú:")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if _name_ == "_main_":
    main()