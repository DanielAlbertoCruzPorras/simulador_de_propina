from formula.logic import calcular_propina, calcular_total
import os

def desing():
    while True:  
        try:
            os.system('clear')
            print(f"""
            =============================================
            Cálculo de Propina
            =============================================""")
        
            total = float(input("\tIngrese el monto total de la cuenta: $"))
            porcentaje = int(input("\tIngrese el porcentaje de propina (por ejemplo: 10, 15, 20): "))
        
            propina = calcular_propina(total, porcentaje)
            
            if total < 0 or porcentaje < 0:
                raise ValueError
            
            print(f""" 
            =============================================
            La propina calculada es: ${propina}
            El total a pagar es: ${calcular_total(total, propina)}
            =============================================
            """)
        
            option = input("¿Deseas calcular nuevamente? (SI/NO): ").upper()
        
            if option == "NO": 
                print("\nGracias por usar el simulador. ¡Hasta luego!")
                break
        except ValueError:
            print("\nEntrada no válida, intenta de nuevo.")
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
