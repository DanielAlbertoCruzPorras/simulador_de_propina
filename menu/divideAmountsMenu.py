from formula.logic import calcular_propina, calcular_total, dividir_total
import os

def desing():
    
    while True:
        try:
            os.system('clear') 
            print(f"""
            =============================================
                    Dividir Cuenta entre Varias Personas
            =============================================""")

            total = float(input("\tIngrese el monto total de la cuenta: "))
            porcentaje = int(input("\tIngrese el porcentaje de propina (por ejemplo:10, 15, 20): "))
            personas = int(input("\tIngrese el número de personas: "))

            propina = calcular_propina(total, porcentaje)
            totalMasPropina = calcular_total(total, propina)
            
            if total < 0 or porcentaje < 0 or personas < 0:
                raise ValueError
            
            print(f"""
            =============================================
            La propina calculada es: ${propina}
            El total a pagar es: ${totalMasPropina}
            Monto por persona: ${dividir_total(totalMasPropina, personas)}
            =============================================
            """)

            option = input("¿Deseas calcular nuevamente? (SI/NO): ").upper()
            # Quiero implementar un break doble y una excepción solo para este segmento
            # Esto para no borrar la info ya calculada
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