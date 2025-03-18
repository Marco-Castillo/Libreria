# Libreria

1. ### Registrar Nuevos Libros
•	Proceso:
o	El sistema solicita al usuario ingresar los datos del libro: ISBN, título, autor, año de publicación y disponibilidad.
o	Estos datos se almacenan en un registro (diccionario en Python) que representa un libro.
o	El registro se agrega a un arreglo llamado inventario, que actúa como la base de datos de libros.

2. ### Buscar un Libro Específico
•	Proceso:
o	El sistema permite buscar un libro por título o ISBN.
o	Si el usuario elige buscar por título, el sistema recorre el arreglo inventario y compara el título proporcionado con los títulos de los libros registrados.
o	Si el usuario elige buscar por ISBN, el sistema compara el ISBN proporcionado con los ISBNs de los libros registrados.
o	Si se encuentra una coincidencia, se muestra la información completa del libro.
o	Si no se encuentra, se informa al usuario que el libro no está registrado.

3. ### Ordenar los Libros
•	Proceso:
o	El sistema permite ordenar los libros por título, autor o año de publicación.
o	El usuario selecciona el criterio de ordenamiento.
o	El sistema utiliza el método Quick sort para reorganizar el arreglo inventario según el criterio seleccionado.
o	Una vez ordenado, se muestra la lista de libros con su información.

4. ### Actualizar la Información de un Libro
•	Proceso:
o	El sistema solicita al usuario el ISBN del libro que desea actualizar.
o	Busca el libro en el arreglo inventario usando una búsqueda lineal.
o	Si el libro existe, permite al usuario modificar cualquiera de sus campos (título, autor, año de publicación o disponibilidad).
o	Si el libro no existe, se informa al usuario que no se encontró.

5. ### Eliminar Registros de Libros
•	Proceso:
o	El sistema solicita al usuario el ISBN del libro que desea eliminar.
o	Busca el libro en el arreglo inventario usando una búsqueda lineal.
o	Si el libro existe, se elimina del arreglo.
o	Si el libro no existe, se informa al usuario que no se encontró.

6. ### Mostrar Libros Registrados
•	Proceso:
o	El sistema permite al usuario ver todos los libros registrados en el inventario.
o	Recorre el arreglo inventario y muestra la información de cada libro (ISBN, título, autor, año de publicación y disponibilidad).
o	Si no hay libros registrados, se muestra un mensaje indicando que el inventario está vacío.
7. ### Menú Principal

Proceso: El sistema muestra un menú interactivo con las siguientes opciones:
1.	Registrar nuevo libro.
2.	Buscar libro.
3.	Ordenar libros.
4.	Actualizar libro.
5.	Eliminar libro.
6.	Mostrar libros registrados.
7.	Salir.
o	El usuario selecciona una opción, y el sistema ejecuta la función correspondiente.
o	El menú se repite hasta que el usuario elige la opción Salir
