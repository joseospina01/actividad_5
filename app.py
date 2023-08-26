def ejercicio_1():
    numeros = []
    for i in range(5):
        num = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)
    
    maximo = max(numeros)
    minimo = min(numeros)
    
    print("El número máximo es:", maximo)
    print("El número mínimo es:", minimo)

def ejercicio_2():
    numero = int(input("Ingrese un número: "))
    
    es_primo = True
    if numero <= 1:
        es_primo = False
    else:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
    
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")

def ejercicio_3():
    n = int(input("Ingrese un número: "))
    suma = 0
    while n != 0:
        suma += n % 10
        n //= 10
    print("La suma de los dígitos es:", suma)

def ejercicio_4():
    frase = input("Ingrese una frase: ")
    invertida = frase[::-1]
    print("Frase invertida:", invertida)

def ejercicio_5():
    cantidad = int(input("Ingrese la cantidad de términos de la serie: "))
    
    a = 0
    b = 1
    print("Serie de Fibonacci:")
    for _ in range(cantidad):
        print(a, end=" ")
        a, b = b, a + b

def main():
    while True:
        print("\nMenú de ejercicios:")
        print("1. Encontrar máximo y mínimo")
        print("2. Número primo")
        print("3. Suma de dígitos")
        print("4. Invertir frase")
        print("5. Serie de Fibonacci")
        print("0. Salir")
        
        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 0:
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