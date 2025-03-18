# Lista para almacenar los libros (arreglo de registros)
inventario = []  # Inicializa el inventario vacío

# Función para registrar un nuevo libro
def registrar_libro():
    print("\nRegistrar nuevo libro:")  # Mensaje de inicio
    isbn = input("ISBN: ")  # Solicita ISBN
    titulo = input("Título: ")  # Solicita título
    autor = input("Autor: ")  # Solicita autor
    año = int(input("Año de publicación: "))  # Solicita año
    disponible = input("¿Está disponible? (s/n): ").lower() == 's'  # Solicita disponibilidad
    
    libro = {  # Crea un registro (diccionario)
        "ISBN": isbn,  # Asigna ISBN
        "titulo": titulo,  # Asigna título
        "autor": autor,  # Asigna autor
        "año_publicacion": año,  # Asigna año
        "disponible": disponible  # Asigna disponibilidad
    }
    inventario.append(libro)  # Agrega libro al inventario
    print("Libro registrado con éxito.")  # Confirma registro

# Función para buscar un libro por título o ISBN
def buscar_libro():
    print("\nBuscar libro:")  # Mensaje de inicio
    criterio = input("Buscar por (1) Título o (2) ISBN: ")  # Solicita criterio de búsqueda
    if criterio == "1":  # Si busca por título
        titulo = input("Ingrese el título: ")  # Solicita título
        for libro in inventario:  # Recorre inventario
            if libro["titulo"].lower() == titulo.lower():  # Compara títulos
                print("\n=== Libro encontrado ===")  # Mensaje de éxito
                print(f"ISBN: {libro['ISBN']}")  # Muestra ISBN
                print(f"Título: {libro['titulo']}")  # Muestra título
                print(f"Autor: {libro['autor']}")  # Muestra autor
                print(f"Año de publicación: {libro['año_publicacion']}")  # Muestra año
                print(f"Disponible: {'Sí' if libro['disponible'] else 'No'}")  # Muestra disponibilidad
                return  # Termina la función
    elif criterio == "2":  # Si busca por ISBN
        isbn = input("Ingrese el ISBN: ")  # Solicita ISBN
        for libro in inventario:  # Recorre inventario
            if libro["ISBN"] == isbn:  # Compara ISBNs
                print("\n=== Libro encontrado ===")  # Mensaje de éxito
                print(f"ISBN: {libro['ISBN']}")  # Muestra ISBN
                print(f"Título: {libro['titulo']}")  # Muestra título
                print(f"Autor: {libro['autor']}")  # Muestra autor
                print(f"Año de publicación: {libro['año_publicacion']}")  # Muestra año
                print(f"Disponible: {'Sí' if libro['disponible'] else 'No'}")  # Muestra disponibilidad
                return  # Termina la función
    print("Libro no encontrado.")  # Mensaje si no se encuentra

# Función para ordenar libros usando Quick Sort
def quick_sort(arr, key):
    if len(arr) <= 1:  # Caso base: si el arreglo tiene 0 o 1 elemento, ya está ordenado
        return arr
    pivot = arr[len(arr) // 2][key]  # Selecciona el pivote (elemento central)
    left = [x for x in arr if x[key] < pivot]  # Elementos menores que el pivote
    middle = [x for x in arr if x[key] == pivot]  # Elementos iguales al pivote
    right = [x for x in arr if x[key] > pivot]  # Elementos mayores que el pivote
    return quick_sort(left, key) + middle + quick_sort(right, key)  # Ordena recursivamente

# Función para ordenar libros por título, autor o año de publicación usando Quick Sort
def ordenar_libros():
    print("\nOrdenar libros por:")  # Mensaje de inicio
    print("1. Título")  # Opción 1
    print("2. Autor")  # Opción 2
    print("3. Año de publicación")  # Opción 3
    opcion = input("Seleccione una opción: ")  # Solicita opción
    
    if opcion == "1":
        key = "titulo"  # Ordenar por título
    elif opcion == "2":
        key = "autor"  # Ordenar por autor
    elif opcion == "3":
        key = "año_publicacion"  # Ordenar por año de publicación
    else:
        print("Opción no válida.")  # Mensaje de error
        return
    
    global inventario  # Accede a la variable global inventario
    inventario = quick_sort(inventario, key)  # Ordena el inventario usando Quick Sort
    
    print("\n=== Libros ordenados ===")  # Mensaje de éxito
    for libro in inventario:  # Recorre inventario ordenado
        print(f"ISBN: {libro['ISBN']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año_publicacion']}, Disponible: {'Sí' if libro['disponible'] else 'No'}")  # Muestra libro

# Función para actualizar la información de un libro
def actualizar_libro():
    print("\nActualizar libro:")  # Mensaje de inicio
    isbn = input("Ingrese el ISBN del libro a actualizar: ")  # Solicita ISBN
    for libro in inventario:  # Recorre inventario
        if libro["ISBN"] == isbn:  # Compara ISBNs
            print("=== Libro encontrado ===")  # Mensaje de éxito
            print("Ingrese los nuevos datos (deje en blanco para mantener el valor actual):")  # Instrucción
            libro["titulo"] = input(f"Nuevo título ({libro['titulo']}): ") or libro["titulo"]  # Actualiza título
            libro["autor"] = input(f"Nuevo autor ({libro['autor']}): ") or libro["autor"]  # Actualiza autor
            libro["año_publicacion"] = int(input(f"Nuevo año de publicación ({libro['año_publicacion']}): ") or libro["año_publicacion"])  # Actualiza año
            disponible = input(f"¿Está disponible? (s/n) ({'Sí' if libro['disponible'] else 'No'}): ").lower()  # Solicita disponibilidad
            if disponible in ['s', 'n']:  # Valida entrada
                libro["disponible"] = disponible == 's'  # Actualiza disponibilidad
            print("Libro actualizado con éxito.")  # Mensaje de éxito
            return  # Termina la función
    print("Libro no encontrado.")  # Mensaje si no se encuentra

# Función para eliminar un libro
def eliminar_libro():
    print("\nEliminar libro:")  # Mensaje de inicio
    isbn = input("Ingrese el ISBN del libro a eliminar: ")  # Solicita ISBN
    for libro in inventario:  # Recorre inventario
        if libro["ISBN"] == isbn:  # Compara ISBNs
            inventario.remove(libro)  # Elimina libro
            print("=== Libro eliminado ===")  # Mensaje de éxito
            return  # Termina la función
    print("Libro no encontrado.")  # Mensaje si no se encuentra

# Función para mostrar todos los libros registrados
def mostrar_libros():
    if not inventario:  # Si el inventario está vacío
        print("\nNo hay libros registrados.")  # Mensaje de inventario vacío
    else:
        print("\n=== Libros Registrados ===")  # Título
        for libro in inventario:  # Recorre cada libro en el inventario
            print(f"ISBN: {libro['ISBN']}")  # Muestra ISBN
            print(f"Título: {libro['titulo']}")  # Muestra título
            print(f"Autor: {libro['autor']}")  # Muestra autor
            print(f"Año de publicación: {libro['año_publicacion']}")  # Muestra año
            print(f"Disponible: {'Sí' if libro['disponible'] else 'No'}")  # Muestra disponibilidad
            print("-" * 30)  # Separador entre libros

# Menú principal
def menu():
    while True:  # Bucle infinito
        print("\n--- Gestión de Inventario de Librería 'Lectura S.A.' ---")  # Título
        print("1. Registrar nuevo libro")  # Opción 1
        print("2. Buscar libro")  # Opción 2
        print("3. Ordenar libros")  # Opción 3
        print("4. Actualizar libro")  # Opción 4
        print("5. Eliminar libro")  # Opción 5
        print("6. Mostrar libros registrados")  # Opción 6
        print("7. Salir")  # Opción para salir
        opcion = input("Seleccione una opción: ")  # Solicita opción
        
        if opcion == "1":  # Si elige 1
            registrar_libro()  # Llama a registrar_libro
        elif opcion == "2":  # Si elige 2
            buscar_libro()  # Llama a buscar_libro
        elif opcion == "3":  # Si elige 3
            ordenar_libros()  # Llama a ordenar_libros
        elif opcion == "4":  # Si elige 4
            actualizar_libro()  # Llama a actualizar_libro
        elif opcion == "5":  # Si elige 5
            eliminar_libro()  # Llama a eliminar_libro
        elif opcion == "6":  # Si elige 6
            mostrar_libros()  # Llama a mostrar_libros
        elif opcion == "7":  # Si elige 7
            print("Saliendo del sistema...")  # Mensaje de salida
            break  # Termina el bucle
        else:
            print("Opción no válida. Intente de nuevo.")  # Mensaje de error

# Ejecutar el menú
menu()  # Inicia el programa