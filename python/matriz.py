def solicitar_datos_persona(i, nombres, ruts):
    nombre = input("Ingrese nombre de la persona {}: ".format(i + 1))
    rut = input("Ingrese RUT de la persona {}: ".format(i + 1))
    nombres[i] = nombre
    ruts[i] = rut

    if i < 3:
        solicitar_datos_persona(i + 1, nombres, ruts)


def mostrar_listas_ordenadas(nombres, ruts):
    print("\nLista de nombres antes de ordenarla: ", nombres)
    print("Lista de RUTs antes de ordenarla: ", ruts)

    # Ordena alfabeticamente
    nombres.sort()
    print("Lista de nombres ordenada: ", nombres)

    # Ordena ascendente y alfabeticamente
    ruts.sort()
    print("Lista de RUTs ordenada: ", ruts)


nombres = [""]
ruts = [""] 

# Solicita datos de las personas
solicitar_datos_persona(0, nombres, ruts)

# Mostrar listas ordenadas
mostrar_listas_ordenadas(nombres, ruts)
