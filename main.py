import os
import datetime

def mostrar_menu():
  print("\nMenu de opciones: ")
  print("1. Saludar")
  print("2. Mostrar Fecha")
  print("3. Salir")

def main():
  while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")

    match opcion:
      case "1":
        print("Funcion de saludar")
      case "2":
        print("Funcion de Mostrar fecha")
      case "3":
        os.system("cls")
        print("\n\nSaliendo...\n\n")
        break
      case _:
        print("Opcion no valida")

if __name__ == "__main__":
  main()