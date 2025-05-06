import os
import datetime

def saludar():
    nombre = input("\n¿Cuál es tu nombre?: ")
    print(f"\n¡Hola, {nombre}! Esta es la función de saludo.\n")

def mostrar_fecha():
    fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
    print(f"\nLa fecha actual es: {fecha_actual}\n")

def mostrar_menu():
  print("\nMenu de opciones: ")
  print("1. Saludar")
  print("2. Mostrar Fecha")
  print("3. Salir")

def main():
  while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opcion: ")

    match opcion:
      case "1":
        saludar()
      case "2":
        mostrar_fecha()
      case "3":
        os.system("cls")
        print("\n\nSaliendo...\n\n")
        break
      case _:
        print("Opcion no valida")

if __name__ == "__main__":
  main()