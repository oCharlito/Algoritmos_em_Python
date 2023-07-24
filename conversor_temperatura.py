def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def main():
    try:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius:.2f} graus Celsius é igual a {fahrenheit:.2f} graus Fahrenheit.")
        print(f"{celsius:.2f} graus Celsius é igual a {kelvin:.2f} Kelvin.")
    except ValueError:
        print("Por favor, digite um valor numérico válido em graus Celsius.")

if __name__ == "__main__":
    main()
