## Instalación de Java <a name=id0></a>

**Nombre:** Ayoze Hernández Díaz.

**Curso:** 1º Desarrollo de Aplicaciones Web.

**Asignatura:** Entornos de desarrollo.

### ÍNDICE

+ [Instalación de Java](#id0)
+ [Actualización de la máquina e instalación](#id1)
+ [Instalación de versiones específicas](#id2)
+ [Configuración de variables de entorno](#id3)

### Actualización de la máquina e instalación <a name=id1></a>

Actualizamos la maquina con **apt update** e instalamos java con **apt install default-jdk**.

![](./img/001.png)

Comprobamos que versión se ha instalado.

![](./img/002.png)

### Instalación de versiones específicas <a name=id2></a>

Teniendo la versión comprobada, instalamos otra versión, en mi caso la versión 8.

![](./img/005.png)

---

Para que quede constancia de ello, se intentó instalar la versión 13 de java, cosa que no pudo ser debido a que la distribución del sistema operativo de mi maquina (xubuntu 22) no da soporte a la misma.

![](./img/004.png)

---
### Configuración de variables de entorno <a name=id3></a>

Ahora procedemos a configurar las variables de entornos necesarias para java.

Para ello hay 2 maneras, la primera es con **update-alternatives**.

![](./img/007.png)

La segunda se hace mediante la creación de un fichero bash en el que se le adjudica un **PATH** y un **HOME** a Java.

![](./img/008.png)

