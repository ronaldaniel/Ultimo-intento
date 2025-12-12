def verificar_par_impar(numero):
    """
    Verifica si un número es par o impar.
    
    Args:
        numero: El número a verificar
        
    Returns:
        str: Mensaje indicando si es par o impar
    """
    if numero % 2 == 0:
        return f"El número {numero} es PAR"
    else:
        return f"El número {numero} es IMPAR"


def verificar_primo(numero):
    """
    Verifica si un número es primo o no.
    
    Args:
        numero: El número a verificar
        
    Returns:
        str: Mensaje indicando si es primo o no
    """
    # Los números menores o iguales a 1 no son primos
    if numero <= 1:
        return f"El número {numero} NO es primo (los números primos son mayores a 1)"
    
    # El 2 es el único número primo par
    if numero == 2:
        return f"El número {numero} es PRIMO"
    
    # Si es par y mayor que 2, no es primo
    if numero % 2 == 0:
        return f"El número {numero} NO es primo (es divisible entre 2)"
    
    # Verificar divisibilidad desde 3 hasta la raíz cuadrada del número
    # Solo verificamos números impares (3, 5, 7, 9, ...)
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return f"El número {numero} NO es primo (es divisible entre {i})"
        i += 2
    
    return f"El número {numero} es PRIMO"


def solicitar_numero(mensaje):
    """
    Solicita un número al usuario con manejo de errores.
    
    Args:
        mensaje: Mensaje a mostrar al usuario
        
    Returns:
        int: El número ingresado por el usuario
    """
    while True:
        try:
            entrada = input(mensaje)
            
            # Verificar si la entrada está vacía
            if not entrada.strip():
                print("❌ Error: No ingresaste nada. Por favor, ingresa un número.\n")
                continue
            
            # Intentar convertir a número entero
            numero = int(entrada)
            return numero
            
        except ValueError:
            print(f"❌ Error: '{entrada}' no es un número válido. Por favor, ingresa solo números enteros.\n")


def menu_principal():
    """
    Función principal que muestra el menú y ejecuta las opciones.
    """
    print("=" * 60)
    print("  VERIFICADOR DE NÚMEROS: PAR/IMPAR Y NÚMEROS PRIMOS")
    print("=" * 60)
    
    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Verificar si un número es PAR o IMPAR")
        print("2. Verificar si un número es PRIMO")
        print("3. Verificar AMBAS cosas")
        print("4. Salir")
        
        opcion = input("\nElige una opción (1-4): ").strip()
        
        if opcion == "1":
            print("\n--- VERIFICACIÓN PAR/IMPAR ---")
            numero = solicitar_numero("Ingresa un número: ")
            resultado = verificar_par_impar(numero)
            print(f"\n✓ {resultado}\n")
            
        elif opcion == "2":
            print("\n--- VERIFICACIÓN DE NÚMERO PRIMO ---")
            numero = solicitar_numero("Ingresa un número: ")
            resultado = verificar_primo(numero)
            print(f"\n✓ {resultado}\n")
            
        elif opcion == "3":
            print("\n--- VERIFICACIÓN COMPLETA ---")
            numero = solicitar_numero("Ingresa un número: ")
            resultado_par = verificar_par_impar(numero)
            resultado_primo = verificar_primo(numero)
            print(f"\n✓ {resultado_par}")
            print(f"✓ {resultado_primo}\n")
            
        elif opcion == "4":
            print("\n¡Hasta luego! 👋\n")
            break
            
        else:
            print("\n❌ Opción inválida. Por favor, elige una opción entre 1 y 4.\n")


# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()