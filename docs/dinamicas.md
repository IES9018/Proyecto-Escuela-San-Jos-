# Dinámicas de Pseudocódigo para Alumnos

Este documento detalla tres actividades prácticas diseñadas para introducir conceptos fundamentales de programación. El objetivo es que los alumnos comprendan que la lógica precede a la sintaxis.

---

## 1. El Robot Humano
**Objetivo:** Comprender que las computadoras son literales y carecen de "sentido común".

### Dinámica
Se selecciona un voluntario para actuar como "Robot". El resto del curso actúa como el "Equipo de Programadores". El Robot solo puede ejecutar órdenes atómicas escritas previamente por los alumnos.

### El Desafío: Preparar un Mate
Los alumnos deben escribir en el pizarrón el algoritmo para que el Robot cebe un mate.

* **Reglas para el Robot:**
    * Si una instrucción es ambigua (ej: "Poné el agua"), el Robot debe fallar de forma creativa (ej: tirar el agua con la pava cerrada).
    * Si se intenta ejecutar una acción sin un requisito previo (ej: `CEBAR()` sin haber hecho `DESTAPAR_TERMO()`), el Robot debe emitir un sonido de error.

### Conceptos Clave
* **Secuencialidad:** El orden de los factores sí altera el producto.
* **Abstracción:** Identificar qué pasos son necesarios y cuáles son redundantes.

---

## 2. Live Coding: PSeInt Interactivo
**Objetivo:** Visualizar el flujo de datos y las estructuras de control.

### Dinámica
Utilizar un proyector para mostrar la interfaz de **PSeInt**. Se plantea un problema de la vida cotidiana y se resuelve en conjunto.

### El Desafío: El Portero de Boliche
Crear un programa que solicite la edad del usuario y determine si puede ingresar, pero con condiciones extra:
1.  Si tiene menos de 18, rebota.
2.  Si tiene entre 18 y 21, pasa pero con pulsera (no toma alcohol).
3.  Si tiene más de 21, pasa libre.

### Herramientas de Enseñanza
* **Diagrama de Flujo:** Generar el diagrama con la herramienta nativa de PSeInt para mostrar los rombos de decisión.
* **Prueba de Escritorio:** Pedir a los alumnos que digan qué valor tomarán las variables en cada paso.

---

## 3. El Gran Bug (Debugging en Papel)
**Objetivo:** Desarrollar la capacidad analítica para encontrar errores lógicos.

### Dinámica
Se entregan fragmentos de pseudocódigo que tienen errores de lógica (no de sintaxis) y los alumnos deben encontrar qué está mal.

### El Desafío: "Cruce de Calle Seguro"
Analizar el siguiente código:

```text
Algoritmo CruceSeguro
    Escribir "Llegaste a la esquina"
    Mirar a la izquierda
    Mirar a la derecha
    Si NO viene ningun auto entonces
        Caminar hasta la otra vereda
    FinSi
    Escribir "Llegaste a destino"
FinAlgoritmo
