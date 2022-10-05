## ETS <a name=id0></a>

**Nombre:** Ayoze Hernández Díaz.

**Curso:** 1º Desarrollo de Aplicaciones Web.

**Asignatura:** Entornos de desarrollo.

### ÍNDICE

+ [ETS](#id0)
+ [Descripción del problema](#id1)
+ [Análisis inicial de la información](#id2)
+ [Diseño y modelo de vida de la aplicación](#id3)
+ [Codificación de la aplicación](#id4)
+ [](#id5)

### Descripción del problema <a name=id1></a>

La empresa de Puerto Systems ha recibido un nuevo encargo de software en el que hay que diseñar una aplicación para una tienda que se especializa en vender productos estéticos.

Dicha tienda desea trabajar con software libre y desea expliícitamente que la aplicación sea capaz de cumplir con las siguientes funciones <a name=idfunciones></a>:

+ Proporcionar facturas de las ventas.
+ Llevar la cuenta de lo que vende cada trabajador.
+ Controlar el stock de productos en almacén.
+ Operar con lector de código de barras y tarjetas de crédito.
+ Controlar los precios de los productos y ofrecer la posibilidad de operar con ellos.
+ El tiempo de respuesta de la aplicación ha de ser lo menor posible.
+ No se podrán procesar dos peticiones a la vez, aunque haya varios equipos funcionando simultáneamente.

La empresa además de lo anteriormente expuesto desea almacenar la siguiente informacion de sus trabajadores y productos: 

<table>
<tr><td>

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

### Análisis inicial de la información <a name=id2></a>

La aplicación del cliente necesitará que en su desarrollo se tenga en cuenta la creación de las funcionalidades descritas en el [apartado anterior](#idfunciones):

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

+ Para todo lo relacionado con los productos y los empleados el cliente en cuestión requerirá de una base de datos que pueda almacenar los datos anteriormente expuestos de los clientes y de los productos, además se deberá de crear una tercera tabla en la base de datos que almacene la clave primaria de las 2 tablas anteriores, esta tabla servirá para almacenar la cantidad de productos vendidos por cada empleado. Se creará una vista que lleve un recuento de los items vendidos en el día para que a final de este se reste esa cantidad a los productos totales de la tienda. La vista sería algo así:

+ Los Items totales equivaldría al resultado de una consulta a la Tabla de productos en la columna de Cantidad.

+ Los Items vendidos sería un **count()** de la tabla que se debe crear de productos vendidos por los empleados.

+ El tercer campo de la tabla sería una resta de los Items totales - los Items vendidos.

Además se tendrá un **trigger o procedimiento** que después de cada día reemplace el valor **Cantidad** de la tabla **Productos** con el valor de **Items Restantes** de la **Vista Items**

+ Para poder operar con códigos de barras se tendría que aplicar algún tipo de lector de códigos de barras.

+ Para poder operar con los precios de los artículos de la tienda habría que construir algún tipo de función que obtenga los valores del precio de cada artículo para que se pueda operar con ellos, a continuación se muestra un ejemplo de 2 productos cullo precio ha sido multiplicado:

```

operaciones_precios(productoA,productoB):
        multiplicacion = productoA * ProductoB
        return multiplicacion

```

+ Para que la aplicación tenga el menor tiempo de respuesta posible debe estár lo mayor optimizada posible. 

+ Para que no se puedan realizar 2 peticiones a la vez se deberá de tener algún tipo de administrador de sesiones para que cuando uno de los usuarios esté realizando algún tipo de petición el otro no pueda.

### Diseño y modelo de vida de la aplicación <a name=id3></a>

A la hora de actualizar o programar la aplicación se debe de hacer a 

### Codificación de la aplicación <a name=id4></a>

###  <a name=id5></a>
