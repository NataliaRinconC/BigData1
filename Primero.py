def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return False  # ERROR INTENCIONAL: 2 sí es primo
    if numero % 2 == 0:
        return False

    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False

    return True


# Programa principal
if __name__ == "__main__":
    try:
        numero = int(input("Ingresa un número entero: "))
        
        if es_primo(numero):
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
    
    except ValueError:
        print("Por favor, ingresa un número entero válido aaaaaaa.")

