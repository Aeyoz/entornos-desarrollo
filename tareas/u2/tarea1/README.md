## Manipulación de repositorios en Git <a name=id0></a>

**Nombre:** Ayoze Hernández Díaz.

**Curso:** 1º Desarrollo de Aplicaciones Web.

**Asignatura:** Entornos de desarrollo.

### ÍNDICE

+ [Manipulación de repositorios en Git](#id0)
+ [](#id1)
+ [](#id2)
+ [](#id3)
+ [](#id4)
+ [](#id5)
+ [](#id6)
+ [](#id7)
+ [](#id8)

### Introducción <a name=id1></a>

Esta tarea tiene como objetivo que el alumno, es decir el autor de este README, se familiarice tanto con la creación como manipulación de repositorios en GIT.

## Tareas <a name=id2></a>

### Tarea: Configuración <a name=id3></a>

Antes de empezar con el resto de las tareas, lo principal es configurar quienes somos.

![Imagen1](./img/001.png)


### Tarea: Creación de un repositorio <a name=id4></a>

Creamos la carpeta contenedora del repositorio y ejecutamos git init.

![Imagen2](./img/002.png)

Nos sale una advertencia que nos suguiere que escojamos el nombre que queremos usar para nuestra rama principal, nos da las opciones de **main** o **master** como recomendaciones principales, en este caso escogemos main y la establecemos como rama por defecto.

![Imagen1-1](./img/001-1.png)

### Tarea: Comprobar el restado del repositorio <a name=id5></a>

Ahora toca comprobar el estado del repositorio y hacer cambios a este mismo. Para esto comprobaremos primeramente el estado del repositorio; acto seguido se crea el fichero indice.txt y añadimos los 2 primeros capítulos y se vuelve a comprobar el estado del repositorio con **git status**.

![Imagen3](./img/003.png)


### Tarea: Realizando Commit's <a name=id6></a>

Para poder realizar un **commit** crearemos un archivo indice.txt y le añadiremos contenido. Luego volveremos a comprobar el estado del repositorio y guardaremos los cambios mediante **git add**  y **git commit -m**.

![Imagen4](./img/004.png)

![Imagen5](./img/005.png)

### Tarea: Modificación de ficheros <a name=id7></a>

Modificamos el fichero indice.txt y añadimos los 2 últimos capítulos. Después de esto miraremos las diferencias entre el indice.txt de antes y el de ahora con **git diff**.

![Imagen6](./img/006.png)

Añadimos los cambios con **git add** y **git commit -m**.

![Imagen7](./img/007.png)

### Tarea: Historial <a name=id8></a>

Ahora tendremos que ver el historico de todos los cambios que se han realizado en este repositorio. Para ello usamos **git show** y **git amend**

![Imagen8](./img/008.png)