# Apuntes Tema 1 ETS

## Ciclo de vida del software

Las fases del desarrollo del software son las siguientes:

+ Analisis:
  + Consiste en definir las necesidades del cliente y especifica los requisitos que se deberian de cumplir.
+ Diseño:
  + Se descomponen las necesidades del cliente en problemas más pequeños, se especifica la correlacion entre cada uno de ellos.
+ Codificación:
  + Se escribe el codigo fuente para cada componente, se pueden usar varios lenguages para varias funcionalidades.
+ Pruebas:
  + Su principal objetivo es conseguir que el programa funcione de manera incorrecta.
+ Documentación:
  + Se escribe una especie de manual de instrucciones de lo que hace una parte general del codigo (un comentario de lo que hace cada función por ejemplo)
+ Explotación:
  + 
+ Mantenimiento:

## Metodologías

+ Modelos clasicos:
  + Modelo en cascada:
    + Modelo más antiguo.
    + Identifica las fases del desarrollo del software.
    + Las fases se realizan en el orden indicado.
    + El resultado de una fase es la entrada de la siguiente.
    + Es un modelo rigido que no se adapta al cambio de necesidades y especificaciones.
    + Existen diferentes variantes con mayor o menor cantidad de actividades.

![](./img/metodología-cascada.png)
 
  + Modelo en V:
    + Modelo similar al modelo de cascada.
    + Visión jerarquizada con distintos niveles.
    + Los niveles superiores indican mayor abstracción.
    + Los niveles inferiores indican mayor nivel de detalle.
    + El resultado de una fase es la entrada de la siguiente.
    + Existen diferentes variantes con mayor o menor cantidad de actividades.

![](./img/metodología-v.png)

+ Modelo de construccion de prototipos:
  + Proceso:
    + Se crea un prototipo durante la fase de análisis y es probado por el cliente para refinar los requisitos del software a desarrollar, esto se repite las veces necesarias.
  + Tipos de prototipos:
    + Prototipos rápidos: 
      + El prototipo puede estar desarrollado usando otro lenguage y/o herramientas.
      + Este prototipo se desecha.
    + Prototipos evolutivos:
      + El prototipo está diseñado en el mismo lenguage y herramientas que el proyecto.
      + El prototipo se usa como base para el proyecto.
+ Modelos evolutivos o incrementales:
  + Modelo en espiral (Iterativos):
    + Desarrollado por Boehm en el año 1988.
    + La actividad de ingeniería corresponde a las fases de los modelos clasicos: análisis, diseño, codificación, ...

![](./img/metodología-espiral.png)

  + metodologías agiles (Adaptativos):
    + Son metodos de ingenieria del software basados en el desarrollo iterativo e incremental.
    + Los requisitos y soluciones evolucionan con el tiempo seun la necesidad del proyecto.
    + El trabajo es realizado mediante la colaboración de equipos auto-organizados y multidisciplinarios inmersos en un proceso compartido de toma de decisiones a corto plazo.
    + Las metodologías más conocidas son: 
      + Kanban
      + Scrum
      + XP (eXtreme Programming)

### Kanban

Kanban, también conocido como sistema de tarjetas fue desarrollado inicialmente por Toyota para la industria de fabricación de productos, esta metodología controla el tiempo y el estado en el que se encuentra cada fase, se enfoca en entregar el máximo valor para los clientes usando los recursos justos. Un ejemplo de herramienta que usa este sistema es [Trello](https://trello.com/es)

### Scrum

Es un modelo de metodología ágil que hace reuniones cada 2-4 semanas, al principio de cada iteración se establecen los objetivos y al finalizar cada iteración se obtiene una entrega parcial utilizable por el cliente.