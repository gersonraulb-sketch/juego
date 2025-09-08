from datos import * # Importaciones para parte funcional en:
from defi import * # Datos y funciones

# Intro del juego
print("Bienvenido a Generic Adventure")
pjnombre = input("ingrese su nombre :")
pj["nombre"] = pjnombre
print(f"""Tu nombre es {pj['nombre']}, un pueblerino que ha ahorrado toda su vida
  para poder convertirse en aventurero, tienes {pj['dinero']} monedas,
  has ido con el mercader para comprar equipamiento.""")

def menu(): # Menu principal de acciones del usuario
    while True:
        print("     MENU PRINCIPAL     ")
        print("1. Ir a la tienda")
        print("2. ver mi inventario")
        print("3. Equipar objetos")
        print("4. Ver mis stats")
        print("5. Salir del juego")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            tienda()
        elif opcion == "2":
            print("     INVENTARIO      ")
            for i, clave in enumerate(pj['inventario'], 1):
                item = objetos[clave]
                print(f"{i}. {item['nombre']}")
        elif opcion == "3":
            equipar_item()
            mostrar_stats()
        elif opcion == "4":
            mostrar_stats()
        elif opcion == "5":
            print("Fin del juego")
            break
        else:
            print("opcion invalida")

menu()