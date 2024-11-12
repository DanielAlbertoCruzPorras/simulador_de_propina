import os

def desing():
    while True:
        os.system("clear")
        print(f"""
        =============================================
                    SIMULADOR DE PROPINA
        =============================================
        1. Calcular propina y total a pagar
        2. Calcular total a pagar dividido entre varias personas
        3. Salir
        =============================================
        """ )
        try:
            option = int(input("Por favor, elige una opción (1-3): "))
            if option < 1 or option > 3:
                print("\nEntrada no válida, por favor ingresa un número entre 1 y 3.")
                input("\nPresiona Enter para continuar...")
                continue
            return option
        except ValueError:
            print("\nEntrada no válida, por favor ingresa un número.")
            input("\nPresiona Enter para continuar...")
            continue
        except Exception as e:
            print(f"\nOcurrió un error inesperado.\nDescripción del error: \n{str(e)}")
            input("\nPresiona Enter para continuar...")
            continue
        except KeyboardInterrupt:
            print(f"\nEjecucuón interrumpida por combinación de teclado.")
            input("\nPresiona Enter para continuar...")
            continue