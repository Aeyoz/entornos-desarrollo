## ETS <a name=id0></a>

**Nombre:** Ayoze Hernández Díaz.

**Curso:** 1º Desarrollo de Aplicaciones Web.

**Asignatura:** Entornos de desarrollo.

### ÍNDICE

+ [ETS](#id0)
+ [Descripción del problema](#id1)
+ [Análisis inicial de la información](#id2)
+ [Diseño y modelo de vida de la aplicación](#id3)
+ [](#id4)
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

+ Trabajadores:

    * DNI
    * Nombre
    * Apellidos
    * Nº de la seguridad social
    * Fecha de nacimiento
    * Teléfono
    * Localidad

+ Productos:

    * Código
    * Marca
    * Nombre
    * Precio
    * Cantidad

### Análisis inicial de la información <a name=id2></a>

La aplicación del cliente necesitará que en su desarrollo se tenga en cuenta la creación de las funcionalidades descritas en el [apartado anterior](#idfunciones):

El cliente en cuestión requerirá de una base de datos que pueda almacenar los datos anteriormente expuestos de los clientes y de los productos, además se deberá de crear una tercera tabla en la base de datos que almacene la clave primaria de las 2 tablas anteriores, esta tabla servirá para almacenar la cantidad de productos vendidos por cada empleado. Se creará una vista que lleve un recuento de los items vendidos en el día para que a final de este se reste esa cantidad a los productos totales de la tienda. La vista sería algo así:

|Items|
|----|
|Nº de Items totales|
|Nº de Items vendidos|
|Nº de Items restantes|

+ Los Items totales equivaldría al resultado de una consulta a la Tabla de productos en la columna de Cantidad.

+ Los Items vendidos sería un **count()** de la tabla que se debe crear de productos vendidos por los empleados.

+ El tercer campo de la tabla sería una resta de los Items totales - los Items vendidos.

Además se tendrá un **trigger o procedimiento** que después de cada día reemplace el valor **Cantidad** de la tabla **Productos** con el valor de **Items Restantes** de la **Vista Items**

Para poder operar con códigos de barras

### Diseño y modelo de vida de la aplicación <a name=id3></a>

### Codificación de la aplicación <a name=id4></a>

###  <a name=id5></a>
