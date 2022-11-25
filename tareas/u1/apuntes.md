# Apuntes Tema 1 ETS

## Ciclo de vida del software

Las fases del desarrollo del software son las siguientes:

+ Analisis:
  + Consiste en definir las necesidades del cliente y especifica los requisitos que se deberian de cumplir.

+ Diseño:
  + Se descomponen las necesidades del cliente en problemás más pequeños, se especifica la correlación entre cada uno de ellos.

+ Codificación:
  + Se escribe el codigo fuente para cada componente, se pueden usar varios lenguages para varias funcionalidades.

+ Pruebas:
  + Su principal objetivo es conseguir que el programa funcione de manera incorrecta.

+ Documentación:
  + Se escribe una especie de manual de instrucciones de lo que hace una parte general del codigo (un comentario de lo que hace cada función por ejemplo), este paso se debe realizar durante cada uno de los pasos anteriormente descritos y los siguientes.

+ Explotación:
  + Fase de entrega del producto al cliente, este mismo puede sugerir cambios o añadidos que deban ser incluidos en el programa.

+ Mantenimiento:
  + Con el tiempo las necesidades del cliente cambian, y el mundo también, por lo que el programa puede necesitar de parches de seguridad o mejoras del rendimiento del mismo.

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

+ Modelo de construcción de prototipos:
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

  + Metodologías agiles (Adaptativos):
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

+ Fases de una iteración:
  + Planificación de la iteración: Al iniciar cada iteración un equipo multifuncional seleciona los requisiitos del cliente de una lista priorizada y propone los equisitos más importantes a desarrollar en ella y se compormenten a terminar los elementos al final de la iteración en el transcurso de la iteración no se pueden cambiar los elementos elegidos.

  + Ejecución de la iteración: Todos los dias el equipo se reune brevemente para informar del progreso y se actualizan unas graficas sencillas que orientan al equipo sobre el trabajo restante. En esta reunion cada equipo responde las preguntas siguientes.

  + Tablero de tareas:

  + Demostración de requisitos completados

  + Retrospectiva de la iteración.

+ Roles en un proyecto Scrum.


## Lenguajes de programación

Definición de un lenguaje de programación: Instrucciones escritas de manera ordenada en código máquina o algún lenguaje que sera interpretado a este mismo.

+ Lenguage de alto nivel: Python
+ Lenguage de bajo nivel: Ensamblador