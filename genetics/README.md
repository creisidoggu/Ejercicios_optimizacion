# Algoritmo Genético para el Problema de la Mochila 🎒

Este README explica la implementación de un algoritmo genético para resolver el clásico problema de la mochila. El código utiliza técnicas de evolución para encontrar la mejor combinación de objetos que maximice el valor total sin exceder el peso máximo permitido.

## 🧬 Descripción del Algoritmo

El algoritmo genético sigue estos pasos principales:

1. **Inicialización de la población**: Se crea una población inicial de soluciones aleatorias.
2. **Evaluación de aptitud**: Se calcula el valor de cada individuo (solución) en la población.
3. **Selección**: Se eligen los individuos más aptos para la reproducción.
4. **Cruce**: Se combinan pares de individuos para crear nuevos descendientes.
5. **Mutación**: Se introducen pequeños cambios aleatorios en algunos individuos.
6. **Reemplazo**: La nueva generación reemplaza a la anterior.
7. **Repetición**: Los pasos 2-6 se repiten durante un número determinado de generaciones.

## 🚀 Características Principales

- Utiliza selección por ruleta para elegir individuos para la reproducción.
- Implementa cruce de un punto para combinar soluciones.
- Aplica mutación para mantener la diversidad genética.
- Visualiza la evolución de la aptitud a lo largo de las generaciones.

## 📊 Visualización de Resultados

El algoritmo genera un gráfico que muestra la evolución de la mejor aptitud en cada generación. Este gráfico se guarda como `fitness_evolution.png` en la carpeta `img/`.

## 🛠️ Cómo Usar

1. Asegúrate de tener Python y las bibliotecas necesarias instaladas.
2. Coloca tu archivo `items.json` en la carpeta `data/`.
3. Ejecuta el script principal:

```bash
python genetics.py
```

4. El algoritmo se ejecutará y mostrará la mejor aptitud obtenida.

## 📝 Parámetros Ajustables

Puedes modificar los siguientes parámetros en la función `run_ga`:

- `population_size`: Tamaño de la población.
- `number_of_generations`: Número de generaciones a ejecutar.
- `knapsack_capacity`: Capacidad máxima de la mochila.

## 🧪 Experimentación

Te animamos a experimentar con diferentes parámetros y ver cómo afectan al rendimiento del algoritmo. Algunas ideas:

- Ajusta el tamaño de la población y el número de generaciones.
- Modifica la tasa de mutación o implementa diferentes tipos de mutación.
- Prueba con diferentes conjuntos de datos en el archivo `items.json`.

## 📈 Mejoras Futuras

Algunas posibles mejoras para el algoritmo incluyen:

- Implementar elitismo para preservar las mejores soluciones.
- Añadir más tipos de operadores de cruce y mutación.
- Implementar una condición de parada basada en la convergencia.