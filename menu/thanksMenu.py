import os

def desing():
  while True:
    try:
      os.system('clear')
      print(f"""
            =============================================
              ¡Gracias por usar el Simulador de Propina!
            =============================================""")

      option = input("Confirma que desea salir? (SI/NO): ").upper()
      
      if option != "SI" and option != "NO":
        raise ValueError
      
      if option == "SI":
          return 0  # Regresa 0 para indicar que el programa debe salir
      return 1  # Si no, continuar
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
