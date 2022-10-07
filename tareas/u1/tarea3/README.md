## Ejercicio de Puerto Systems <a name=id0></a>

**Nombre:** Ayoze Hernández Díaz.

**Curso:** 1º Desarrollo de Aplicaciones Web.

**Asignatura:** Entornos de desarrollo.

### ÍNDICE

- [Ejercicio de Puerto Systems](#)
  - [ÍNDICE](#índice)
  - [Descripción y análisis del problema <a name=id1></a>](#descripción-y-análisis-del-problema-)
  - [Diseño de la aplicación <a name=id2></a>](#diseño-de-la-aplicación-)
  - [Modelo de vida de la aplicación <a name=id3></a>](#modelo-de-vida-de-la-aplicación-)
  - [Codificación de la aplicación <a name=id4></a>](#codificación-de-la-aplicación-)
  
### Descripción y análisis del problema <a name=id1></a>

La empresa de Puerto Systems ha recibido un nuevo encargo de software en el que hay que diseñar una aplicación para una tienda que se especializa en vender productos estéticos.

Dicha tienda desea trabajar con software libre y desea expliícitamente que la aplicación sea capaz de cumplir con las siguientes funciones <a name=idfunciones></a>:

+ Proporcionar facturas de las ventas.
+ Llevar la cuenta de lo que vende cada trabajador.
+ Controlar el stock de productos en almacén.
+ Operar con lector de código de barras y tarjetas de crédito.
+ Controlar los precios de los productos y ofrecer la posibilidad de operar con ellos.
+ El tiempo de respuesta de la aplicación ha de ser lo menor posible.
+ No se podrán procesar dos peticiones a la vez, aunque haya varios equipos funcionando simultáneamente.

La empresa además de lo anteriormente expuesto desea almacenar la siguiente informacion de sus trabajadores y productos por lo que hará falta una base de datos que lleve la información de estos.

### Diseño de la aplicación <a name=id2></a>

La aplicación del cliente necesitará que en su desarrollo se tenga en cuenta la creación de las funcionalidades descritas en el [apartado anterior](#idfunciones):

Para almacenar la información de la tienda es necesario una base de datos que contendrá las siguientes tablas y vistas para almacenar la información. Las tablas originales son las de productos y trabajadores. 

<table>
<tr>
<td>

|   Trabajadores   |
|------------------|
|DNI|
|Nombre|
|Apellidos|
|Nº de la seguridad social|
|Fecha de nacimiento|
|Teléfono|
|Localidad|


</td><td>

| Productos | 
|-----------|
|  Código  |
|  Marca   |
|  Nombre  |
|  Precio  |
| Cantidad |

</td>
</table>

Las tabla de items por empleados es una tabla necesaria para que se pueda hacer un recuento de los items que ha vendido cada trabajador; mientras que la vista de recuento de items lleva un recuento de los items que la tienda tiene y vende diariamente.

<table>
<td>

|  Recuento de Items  | 
|---------------------|
| Nº de Items Totales |
|Nº de Items Vendidos |
|Nº de Items Restantes|

</td> 

<td>

|  Items por empleado | 
|---------------------|
|   Id del Empleado   |
|   Id del producto   |

</td> 

</tr>
</table>

En la vista de Recuento de Items las columnas de la tabla se describen a continuación:

+ Los Items totales equivaldría al resultado de una consulta a la Tabla de productos en la columna de Cantidad.

+ Los Items vendidos sería un **count()** de la tabla que se debe crear de productos vendidos por los empleados.

+ El tercer campo de la tabla sería una resta de los Items totales - los Items vendidos.

Además se tendrá un **trigger o procedimiento** que después de cada día reemplace el valor **Cantidad** de la tabla **Productos** con el valor de **Items Restantes** de la **Vista Items**

+ Para poder operar con los precios de los artículos de la tienda habría que construir algún tipo de función que obtenga los valores del precio de cada artículo para que se pueda operar con ellos, a continuación se muestra un ejemplo de 2 productos cullo precio ha sido multiplicado:


```

operaciones_precios(productoA,productoB):
        multiplicacion = productoA * ProductoB
        return multiplicacion

```

----

+ El cliente debe de disponer a su disposición alguna página que muestre las facturas que se le hayan realizado a los clientes suyos, una factura ejemplo mostraría lo siguiente:

```
+----------------------+
|       Factura        |
+----------------------+
|   Vendedor = Miguel  |
+----------------------+
|   Producto = Pincel  |
+----------------------+
|    Precio = 2.5 €    |
+----------------------+
|Precio + IVA = 2.675 €|
+----------------------+
```

----

+ Para poder operar con códigos de barras se tendría que aplicar algún tipo de lector de códigos de barras.

----

+ Para que la aplicación tenga el menor tiempo de respuesta posible debe estár lo mayor optimizada posible. 

----

+ Para que no se puedan realizar 2 peticiones a la vez se deberá de tener algún tipo de administrador de sesiones para que cuando uno de los usuarios esté realizando algún tipo de petición el otro no pueda.

### Modelo de vida de la aplicación <a name=id3></a>

Para que no haya malentendidos se utilizará una metodología ágil en el desarrollo de la aplicación, por lo que el Puerto Systems irá preguntando datos sobre la aplicación para saber lo que el cliente realmente quiere y adecuar esta información al desarrollo de la aplicación. Se irán subiendo los cambios al repositorio de el Puerto Systems y se le comunicará al cliente que ese repositorio existe para que ellos puedan ir echando un vistazo a los cambios de la aplicación y que se comuniquen con el Puertos Systems en caso de que no les guste alguna implementación o en caso de que quieran añadir alguna que otra cosa.

Para que se pueda organizar las ideas y los procesos en desarrollo de se usará Trello, una herramienta de flujo que permite organizar mediante tickets las tareas a realizar, los tickets llevan un nombre sencillo y descriptivo de la tarea, pero dentro de los tickets está una descripción más elaborada de la misma.

Se celebrarán 2 reuniones de media hora al día, una al inicio para saber en qué se va a trabajar y como se repartirá el trabajo en ese día, y al final del día se celebrará otra reunión de media hora para comunicar como se ha comportado cada una de las tareas descritas en la primera reunión y para comunicar los cambios importantes que se crean necesarios. 

---

### Codificación de la aplicación <a name=id4></a>

La aplicación estará hecha en python debido a que es el lenguage de programación en el que se tiene más experiencia y el que mejor conozco.

---

### Pruebas <a name=id5></a>

Las pruebas se ejecutarán várias veces al día, una vez a mitad de la jornada y otra vez una hora antes del fin de la jornada, que es media hora antes de la 2ª reunión del día. Se le pide al cliente que cuando la aplicación se les sea entregada notifiquen cualquier tipo de error en la aplicación para así poder detectar que es lo que falla y arreglarlo lo más pronto posible.

---

