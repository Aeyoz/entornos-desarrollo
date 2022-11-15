## Instalación de Maven <a name=id0></a>

**Nombre:** [Ayoze Hernández Díaz.](https://github.com/ElPayo)

**Curso:** 1º Desarrollo de Aplicaciones Web.

**Asignatura:** Entornos de desarrollo.

### ÍNDICE

+ [Instalación de Maven](#id0)
+ [Instalación de maven en la máquina](#id1)
+ [Instalación de una versión especifica](#id2)

### Instalación de maven en la máquina <a name=id1></a>

Instalamos maven y actualizamos el estado de los paquetes de la máquina.

![](./img/001.png)

Comprobamos que se ha instalado y vemos la versión instalada.

![](./img/002.png)


### Instalación de una versión especifica <a name=id2></a>

Ahora con el comando siguiente nos descargamos el paquete de la versión que queramos o necesitemos de Maven.

![](./img/003.png)

Ahora descomprimimos el archivo.

![](./img/004.png)

Realizamos un enlace simbólico a la carpeta contenedora.

![](./img/005.png)

En el archivo **/etc/profile.d/maven.sh** metemos lo siguiente para definir el home y el path de Maven.

![](./img/006.png)

Le otorgamos permisos de ejecución al archivo descargado y recargamos el fichero anterior.

![](./img/007.png)