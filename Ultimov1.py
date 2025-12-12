
def verificar_par_impar():
  
    print("=" * 50)
    print("  VERIFICADOR DE NÚMEROS PARES E IMPARES")
    print("=" * 50)
    print()
    
    
    entrada = input("Por favor, ingrese un número: ")
    
    
    try:
        
        numero = int(entrada)
        
       
        if numero % 2 == 0:
            print()
            print(f"✓ El número {numero} es PAR")
        else:
            print()
            print(f"✓ El número {numero} es IMPAR")
    
    except ValueError:
        
        print()
        print(f"❌ ERROR: '{entrada}' no es un número válido")
        print("   Por favor, ingresa solo números enteros (ejemplos: 5, 42, -7)")
        print()

# Ejecutar el programa
if __name__ == "__main__":
    verificar_par_impar()