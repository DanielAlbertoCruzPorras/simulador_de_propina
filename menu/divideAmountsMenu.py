from formula.logic import calcular_propina, calcular_total, dividir_total
import os
class BreakLoop(Exception):
    pass

def desing():
    try:
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
                # Salgo de ambos while o no según se prefiera y me permite verificar que haya selección correcta de si o no
                while True:
                    option = input("¿Deseas calcular nuevamente? (SI/NO): ").upper()
                    if option == "NO": 
                        print("\nGracias por usar el simulador. ¡Hasta luego!")
                        raise BreakLoop
                    elif option != "SI" and option != "NO":
                        print("\nEntrada no válida, intenta de nuevo.")
                        input("\nPresiona Enter para continuar...")
                        continue
                    
            except ValueError:
                print("\nEntrada no válida, intenta de nuevo.")
                input("\nPresiona Enter para continuar...")
                continue
            except KeyboardInterrupt:
                print(f"\nEjecucuón interrumpida por combinación de teclado.")
                input("\nPresiona Enter para continuar...")
                continue
    except BreakLoop:
        print("Se salió de los bucles.")