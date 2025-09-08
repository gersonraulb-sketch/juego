from datos import pj, objetos

def tienda(): # Tienda de los objetos básicos del jugador 
    print("Bienvenido")
    print("Items disponibles:")

    for i, (clave, item) in enumerate(objetos.items(), 1):
        print(f"{i}. {item['nombre']} - {item['valor']} monedas")

    print(f"\nTienes {pj['dinero']} monedas") # Saldo del usuario

    compras = input("¿Qué quieres comprar? (Ej: 1,3,5): ") # Acción de compra del usuario
    

    items_comprados = [] # Objetos seleccionados para la compra
    total = 0 # Costo de los objetos 

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

    print("\nEquipado:")
    if pj['equipado']['arma']:
        print(f"Arma: {objetos[pj['equipado']['arma']]['nombre']}")
    else:
        print("Arma: Ninguna")

    if pj['equipado']['armadura']:
        print(f"Armadura: {objetos[pj['equipado']['armadura']]['nombre']}")
    else:
        print("Armadura: Ninguna")