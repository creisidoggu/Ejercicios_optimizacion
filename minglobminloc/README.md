# Mínimo Global vs. Mínimo Local en Búsqueda de Cobertura con Radios

## Descripción del problema

Imagina que una compañía de radios desea optimizar la cobertura de sus estaciones de transmisión al menor costo posible. Dado un conjunto de estaciones de radio y los estados que cubren, queremos encontrar el subconjunto más pequeño de estaciones que cubra todos los estados.

## Algoritmos implementados

### 1. Mínimo Global: `exact_global_min`
Este algoritmo encuentra la solución óptima exacta mediante una búsqueda exhaustiva:

- Genera todas las combinaciones posibles de estaciones de radio.
- Verifica que cada combinación cubra todos los estados.
- Devuelve la combinación más pequeña que cubra todos los estados.

**Ventajas:**
- Encuentra la mejor solución posible.
- Garantiza la cobertura óptima con el menor número de estaciones.

**Desventajas:**
- Su complejidad es exponencial, lo que lo hace impráctico para un gran número de estaciones y estados.

### 2. Mínimo Local: `minimun_local_search`
Este algoritmo utiliza búsqueda local con reinicios aleatorios para encontrar una solución aceptable de manera eficiente:

- Se genera una selección aleatoria de estaciones.
- Se verifica cuántos estados quedan sin cobertura.
- Se repite el proceso con diferentes selecciones iniciales y se registra la mejor solución encontrada.

**Ventajas:**
- Es más rápido que el método exacto.
- Permite encontrar una solución cercana al óptimo en menos tiempo.

**Desventajas:**
- No siempre encuentra la mejor solución posible.
- Puede quedarse atrapado en un mínimo local.

## Referencias
- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach*. Pearson.
- Bhargava, A. (2016). Grokking Algorithms: An Illustrated Guide for Programmers and Other Curious People. Manning Publications.

[Guía de instalación y uso del proyecto](how_to_execute.md)