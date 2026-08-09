# Administrador de tareas

import os

# Crear la carpeta "listas" si no existe
if not os.path.exists("listas"):
    os.makedirs("listas")


while True:

    print("\n ADMINISTRADOR DE TAREAS ")

    # Mostrar las listas existentes
    archivos = os.listdir("listas")

    if len(archivos) == 0:
        print("\nNo tienes ninguna lista creada.")
    else:
        print("\nTus listas:")
        
        for i, archivo in enumerate(archivos, start=1):
            nombre_lista = archivo.replace(".txt", "")
            print(f"{i}. {nombre_lista}")

    print("\n1. Crear una lista")
    print("2. Entrar a una lista")
    print("3. Salir")

    opcion = input("\nElige una opción: ")

    # Crear una lista
    if opcion == "1":

        nombre = input("\nEscribe el nombre de la nueva lista: ")

        archivo = f"listas/{nombre}.txt"

        if os.path.exists(archivo):
            print("Esa lista ya existe.")
        else:
            with open(archivo, "w", encoding="utf-8") as f:
                pass

            print("Lista creada correctamente.")


    # Entrar a una lista
    elif opcion == "2":

        archivos = os.listdir("listas")

        if len(archivos) == 0:
            print("\nNo hay listas para abrir.")
            continue

        print("\nElige una lista:")

        for i, archivo in enumerate(archivos, start=1):
            nombre_lista = archivo.replace(".txt", "")
            print(f"{i}. {nombre_lista}")

        try:
            seleccion = int(input("\nNúmero de la lista: "))

            if seleccion < 1 or seleccion > len(archivos):
                print("Número de lista no válido.")
                continue

            archivo = "listas/" + archivos[seleccion - 1]

        except ValueError:
            print("Debes escribir un número.")
            continue


        # Menú de la lista
        while True:

            nombre_lista = archivos[seleccion - 1].replace(".txt", "")

            print(f"\n===== LISTA: {nombre_lista} =====")

            with open(archivo, "r", encoding="utf-8") as f:
                tareas = f.readlines()

            if len(tareas) == 0:
                print("\nNo hay tareas pendientes.")
            else:
                print("\nEsta es tu lista de tareas:\n")

                for i, tarea in enumerate(tareas, start=1):
                    print(f"{i}. {tarea.strip()}")


            print("\n1. Agregar tarea")
            print("2. Eliminar tarea")
            print("3. Volver a las listas")

            opcion_lista = input("\nElige una opción: ")


            # Agregar tarea
            if opcion_lista == "1":

                nueva = input("\nEscribe la nueva tarea: ")

                with open(archivo, "a", encoding="utf-8") as f:
                    f.write(nueva + "\n")

                print("Tarea agregada correctamente.")


            # Eliminar tarea
            elif opcion_lista == "2":

                if len(tareas) == 0:
                    print("\nNo hay tareas para eliminar.")
                    continue

                try:
                    numero = int(input("\nNúmero de tarea que quieres eliminar: "))

                    if numero < 1 or numero > len(tareas):
                        print("Número de tarea no válido.")
                        continue

                    tareas.pop(numero - 1)

                    with open(archivo, "w", encoding="utf-8") as f:
                        f.writelines(tareas)

                    print("Tarea eliminada correctamente.")

                except ValueError:
                    print("Debes escribir un número.")


            # Volver
            elif opcion_lista == "3":

                print("\nVolviendo a las listas...")
                break


            else:
                print("Opción no válida.")


    # Salir
    elif opcion == "3":

        print("\nAdministrador de tareas cerrado.")
        break


    else:
        print("\nOpción no válida.")