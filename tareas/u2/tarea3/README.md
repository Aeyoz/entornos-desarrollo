<<<<<<< HEAD
## Manipulación Avanzada en Git trabajo con tags y ramas. <a name=id0></a>
=======
## Manipulación de repositorios avanzada con tags y ramas <a name=id0></a>
>>>>>>> 9c7a59719514e5c98b2d6b2da00a7161f01ae830

**Nombre:** Ayoze Hernández Díaz.

**Curso:** 1º Desarrollo de Aplicaciones Web.

**Asignatura:** Entornos de desarrollo.

### ÍNDICE

<<<<<<< HEAD
+ [Manipulación Avanzada en Git trabajo con tags y ramas.](#id0)
+ [Tareas](#id1)
  + [Tarea 1: Creación del repositorio y Readme inicial](#id2)
  + [Tarea 2 y 3: Commit y push inicial](#id3)
  + [Tarea 4: Ignorar archivos](#id4)
  + [Tarea 5, 6 y 7: Añadir fichero 1, creación del tag v0.1 y subida del mismo](#id5)
  + [Tarea 8: Crear una rama v0.2](#i6)
  + [Tarea 9: Añadir fichero 2](#id7)
  + [Tarea 10: Crear rama remota](#id8)
  + [Tarea 11: Merge directo](#id9)
  + [Tarea 12: Merge con conflicto](#id10)
  + [Tarea 13: Listado de cambios](#id11)
 + [ANEXO](#ANEXO)

### Tareas <a name=id1></a>

## Tarea 1: Creación del repositorio y Readme inicial <a name=id2></a>

Creamos el repositorio de nuestro ***Proyecto Millonario*** en Github y nos lo bajamos con git clone.

![](./img/001.png)

Ahora editamos el fichero [README](https://github.com/ElPayo/mi-proyecto-millonario#readme) y vamos añadiendo las preguntas realizadas por el profesor en su documento de explicación, además de añadir los comandos que se hayan usado durante la practica, por ahora se añade lo siguiente.

![](./img/002.png)

## Tarea 2 y 3: Commit incial <a name=id3></a>

Ahora guardamos los cambios con git add y git commit. Acto seguido realizaremos tanto el push como el commit iniciales.

![](./img/003.png)

## Tarea 4: Ignorar archivos <a name=id4></a>

Ahora debemos crear el fichero .gitignore en el que especificaremos los archivos y carpetas que no queremos que se suban al repositorio en la nube, en nuestro caso no queremos que se suban **privado.txt** ni **privada/**

![](./img/004.png)

Vemos una estructura de como tenemos el repositorio actualmente.

![](./img/005.png)

Ahora guardamos los cambios que se han realizado

![](./img/006.png)

## Tarea 5, 6 y 7: Añadir fichero 1, creación del tag v0.1 y subida del mismo <a name=id5></a>

Ahora añadimos el fichero 1.txt que se usará para similar la primera versión del repositorio.

![](./img/007.png)

Guardamos los cambios como se muestra arriba y hacemos que el tag ahora esté en la nube con **git push --tag origin main**.

![](./img/008.png)

## Tarea 8: Crear una rama v0.2 <a name=id6></a>

Ahora creamos la rama v0.2.

![](./img/009.png)

## Tarea 9: Añadir fichero 2 <a name=id7></a>

Nos cambiamos a la rama v0.2 y creamos el fichero 2.txt.

![](./img/010.png)

![](./img/011.png)

## Tarea 10: Crear rama remota <a name=id8></a>

Creamos la rama remotamente con **git push origin v0.2**.

![](./img/012.png)

## Tarea 11: Merge directo <a name=id9></a>

Ahora podemos mezclar el contenido de las 2 ramas sin que haya conflicto alguno.

![](./img/013.png)

## Tarea 12: Merge con conflicto <a name=id10></a>

Ahora vamos a hacer un merge para que de conflicto. Para ello debemos modificar el fichero **1.txt** tanto en la rama **v0.2** como en **main**, en las 2 ramas va a tener contenido diferente para que surja el conflicto.

![](./img/014.png)

Aquí vemos el resultado de realizar lo explicado anteriormente.

![](./img/015.png)

Ahora para arreglar los conflictos debemos modificar el fichero **1.txt** para que contenga tanto el contenido del fichero **1.txt** de **main** como el contenido del fichero **1.txt** de **v0.2**.

![](./img/016.png)

Ahora creamos el tag v0.2 y eliminamos la rama v0.2.

![](./img/017.png)

## Tarea 13: Listado de cambios <a name=id11></a>

Ahora podemos ver un listado de los cambios realizados en el repositorio.

![](./img/018.png)

----

## ANEXO : <a name=ANEXO></a>

Comandos de git usados:

+ **git add**: Se usa para guardar los cambios en los ficheros que se indiquen.
+ **git commit**: Se usa para poner un comentario a todos los ficheros que hayan sido guardados con git add.
+ **git push**: Se usa para llevar los cambios que hayan sido guardados a la nube.
+ **git branch**: Se usa para el manejo de ramas.
+ **git switch**: Se usa para cambiar entre ramas.
+ **git tag**: Se usa para marcar el punto historico de en el que 2 versiones se separan
+ **git merge**: Se usa para mezclar el contenido de 2 ramas en git.
=======
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
>>>>>>> 9c7a59719514e5c98b2d6b2da00a7161f01ae830
