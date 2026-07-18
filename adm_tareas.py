# Administrador de tareas

archivo = "tareas.txt"

while True:
    print("\n===== ADMINISTRADOR DE TAREAS =====")

    # Mostrar tareas
    print("\nEsta es tu lista de tareas:\n")

    with open(archivo, "r") as f:
        tareas = f.readlines()

    if len(tareas) == 0:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea.strip()}")

# Menu

print("\n1. Agregar tarea")
print("2. Salir")

opcion = input("Elige una opción: ")

if opcion == "1":
    nueva = input("Escribe la nueva tarea: ")

    with open(archivo, "a", encoding="utf-8") as f:
        f.write(nueva + "\n")

    print("Tarea agregada correctamente.")

elif opcion == "2":
    print("lista de tareas cerrada.")

else:
    print("Opcion no valida.")