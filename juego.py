from datos import pj, objetos

print("Bienvenido a Generic Adventure")
pjnombre = input("ingrese su nombre :")
pj["nombre"] = pjnombre
print(f"""Tu nombre es {pj['nombre']}, un pueblerino que ha ahorrado toda su vida
  para poder convertirse en aventurero, tienes {pj['dinero']} monedas,
  has ido con el mercader para comprar equipamiento.""")


def tienda():
    print("Bienvenido")
    print("Items disponibles:")

    for i, (clave, item) in enumerate(objetos.items(), 1):
        print(f"{i}. {item['nombre']} - {item['valor']} monedas")

    print(f"\nTienes {pj['dinero']} monedas")

    compras = input("¿Qué quieres comprar? (Ej: 1,3,5): ")

    items_comprados = []
    total = 0

    for num in compras.split(","):
        try:
            num = int(num.strip()) - 1
            if 0 <= num < len(objetos):
                clave = list(objetos.keys())[num]
                item = objetos[clave]
                total += item['valor']
                items_comprados.append(item['nombre'])
        except:
            pass

    if total > pj['dinero']:
        print("¡No tienes suficiente dinero para todo eso!")
        return False
    else:
        pj['dinero'] -= total
        for num in compras.split(","):
            num = int(num.strip()) - 1
            if 0 <= num < len(objetos):
                clave = list(objetos.keys())[num]
                pj['inventario'].append(clave)

        print(f"Compra exitosa, Gastaste {total} monedas")
        print(f"Te quedan {pj['dinero']} monedas")
        print("Items comprados:", ", ".join(items_comprados))
        return True


def equipar_item():
    print("\n--- EQUIPAR ITEMS ---")

    if not pj['inventario']:
        print("No tienes items en tu inventario!")
        return

    print("Tus items:")
    for i, clave_item in enumerate(pj['inventario'], 1):
        item = objetos[clave_item]
        print(f"{i}. {item['nombre']} ({item['tipo']})")

    try:
        eleccion = int(input("\n¿Qué item quieres equipar? (número): ")) - 1
        if 0 <= eleccion < len(pj['inventario']):
            clave_item = pj['inventario'][eleccion]
            item = objetos[clave_item]

            if item['tipo'] == 'arma':
                pj['equipado']['arma'] = clave_item
                print(f"¡{item['nombre']} equipado como arma!")
            elif item['tipo'] == 'armadura':
                pj['equipado']['armadura'] = clave_item
                print(f"¡{item['nombre']} equipado como armadura!")
            else:
                print("Este item no se puede equipar")
        else:
            print("Número inválido")
    except ValueError:
        print("Por favor ingresa un número")


def calcular_stats():

    ataque_total = pj['ataque']
    defensa_total = pj['defensa']

    if pj['equipado']['arma']:
        arma = objetos[pj['equipado']['arma']]
        ataque_total += arma['ataque']

    if pj['equipado']['armadura']:
        armadura = objetos[pj['equipado']['armadura']]
        defensa_total += armadura['defensa']

    return ataque_total, defensa_total


def mostrar_stats():
    ataque, defensa = calcular_stats()
    print(f"    ESTADÍSTICAS ACTUALIZADAS    ")
    print(f"Vida: {pj['vida']}")
    print(
        f"Ataque: {ataque} (base: {pj['ataque']} + equipo: {ataque - pj['ataque']})")
    print(
        f"Defensa: {defensa} (base: {pj['defensa']} + equipo: {defensa - pj['defensa']})")
    print(f"Dinero: {pj['dinero']} monedas")

    # Mostrar equipo actual
    print("\nEquipado:")
    if pj['equipado']['arma']:
        print(f"Arma: {objetos[pj['equipado']['arma']]['nombre']}")
    else:
        print("Arma: Ninguna")

    if pj['equipado']['armadura']:
        print(f"Armadura: {objetos[pj['equipado']['armadura']]['nombre']}")
    else:
        print("Armadura: Ninguna")


def menu():
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
