def convertir_a_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32 #Convierte una temperatura de Celsius a Fahrenheit.
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit): # Convierte una temperatura de Fahrenheit a Celsius.
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():
    try:
        opcion = input("¿Qué desea convertir? (1: F a C, 2: C a F): ")
        if opcion == "1":
            fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit}°F equivale a {celsius:.2f}°C")
        elif opcion == "2":
            celsius = float(input("Ingrese la temperatura en Celsius: "))
            fahrenheit =  convertir_a_fahrenheit(celsius)
            print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")
        else:
            print("Opción inválida. Por favor elija 1 o 2.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()