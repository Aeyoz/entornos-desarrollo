## Manipulación de repositorios avanzada con tags y ramas <a name=id0></a>

**Nombre:** Ayoze Hernández Díaz.

**Curso:** 1º Desarrollo de Aplicaciones Web.

**Asignatura:** Entornos de desarrollo.

### ÍNDICE

+ [Manipulación de repositorios avanzada con tags y ramas](#id0)
+ [Introducción](#id1)
+ [Tareas](#id2)
+ [Tarea 1: ](#id3)
+ [Tarea 2:](#id4)
+ [Tarea 3:](#id5)
+ [Tarea 4:](#id6)
+ [Tarea 5:](#id7)
+ [Tarea 6:](#id8)
+ [Tarea 7:](#id9)
+ [Tarea 8:](#id10)
+ [Tarea 9:](#id11)
+ [Tarea 10:](#id12)
+ [ANEXO](#ANEXO)

### Introducción <a name=id1></a>

En esta tarea se trabajará con el manejo tags y versiones en repositorios de Github.

### Tareas <a name=id2></a>

### Tarea 1: README <a name=id3></a>

Con el repositorio creado, se deberá de crear un README.md o usar el que ya está creado. En este [README.md](https://github.com/ElPayo/mi-proyecto-millonario)

### Tarea 2: Commit inicial <a name=id4></a>

Realizamos el commit inicial en el que simplemente tenemos el archivo con la primera pregunta a realizar.

### Tarea 3: Push inicial <a name=id5></a>

En el push inicial intentaremos definir la rama principal como main o master.

### Tarea 4: Creación del fichero .gitignore <a name=id6></a>

Ahora creamos un fichero .gitignore en el que definimos los archivos y carpetas que no queremos que sean subidos al repositorio en la nube.

### Tarea 5: Primer fichero <a name=id7></a>

Creamos el fichero 1.txt.

### Tarea 6: Crear el tag v0.1 <a name=id8></a>

Con **git tag v0.1** creamos el tag v0.1 en nuestro repositorio, y para llevarlo a la nube realizamos un **git push --tag origin master**.

### Tarea 7: Creación de la rama v0.2 <a name=id9></a>

Creamos la rama v0.2 con **git branch v0.2** y nos cambiamos de rama con **git switch v0.2** o con **git checkout v0.2**

### Tarea 8: Segundo fichero <a name=id10></a>

En la rama v0.2 creamos el fichero 2.txt y guardamos los cambios con **git add .** y **git commit -m "Mensaje"**.

### Tarea 9: Merge directo <a name=id11></a>

Cambiamos a la rama main con **git switch main** y realizamos un **git merge v0.2 -m "merge v0.2 sin conflictos"** para mezclar el contenido de las 2 ramas.

### Tarea 10: Merge con conflicto. <a name=id12></a>


### Tarea 11: Listado de ramas <a name=id12></a>

### Tarea 12: Listado de cambios <a name=id12></a>



----

### ANEXO <a></a name=ANEXO>