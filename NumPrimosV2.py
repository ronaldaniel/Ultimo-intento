def verificar_primo():
    
    print("=" * 50)
    print("  VERIFICADOR DE NÚMEROS PRIMOS")
    print("=" * 50)
    print()

    entrada = input("Por favor, ingresa un número: ")

    try:
        
        numero = int(entrada)
    
        if numero <= 1:
            
            print()
            print(f"✗ El número {numero} NO es primo")
            print("  (Los números primos deben ser mayores a 1)")
        
        elif numero == 2:
            
            print()
            print(f"✓ El número {numero} es PRIMO")
            print("  (El 2 es el único número primo par)")
        
        elif numero % 2 == 0:
            
            print()
            print(f"✗ El número {numero} NO es primo")
            print(f"  (Es divisible entre 2)")
        
        else:
            
            es_primo = True
            divisor_encontrado = 0
            
            i = 3
            while i * i <= numero:
                if numero % i == 0:
                    
                    es_primo = False
                    divisor_encontrado = i
                    break
                i += 2  
            
            print()
            if es_primo:
                print(f"✓ El número {numero} es PRIMO")
                print("  (Solo es divisible entre 1 y él mismo)")
            else:
                print(f"✗ El número {numero} NO es primo")
                print(f"  (Es divisible entre {divisor_encontrado})")
    
    except ValueError:
        
        print()
        print(f"❌ ERROR: '{entrada}' no es un número válido")
        print("   Por favor, ingresa solo números enteros (ejemplos: 7, 13, 29)")
        print()

if __name__ == "__main__":
    verificar_primo()