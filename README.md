# Mínimo global vs. Mínimo local en búsqueda de cobertura con radios

## Descripción del problema

Beyoncé quiere que su albúm country llegue a todo el mundo por el menor coste y dado un conjunto de radios y los estados que cubren, queremos encontrar el subconjunto más pequeño de radios que cubra todos los estados.

### Mínimo global: `exact_global_min`
Este algoritmo encuentra la solución óptima exacta. Su funcionamiento es:
1. Generar todas las combinaciones posibles de radios.
2. Verifique que cada combinación cubra todos los estados.
3. Devuelve la combinación más pequeña que cubra todos los estados.

Este método garantiza encontrar la mejor solución posible, pero es computacionalmente costoso debido a su complejidad exponencial.

### Mínimo local: `local_search_with_restarts`
Este algoritmo utiliza una búsqueda local para encontrar rápidamente una solución aceptable:
1. Comience con una solución aleatoria que cubra todos los estados.
2. Intentar mejorar eliminando radios, garantizando que se mantenga la cobertura total.
3. Si no puedes mejorar más, guarda la mejor solución encontrada.
4. Repita el proceso con un nuevo punto de partida varias veces para evitar quedarse estancado en un mínimo local.

Este enfoque es más eficiente que la búsqueda global exacta, aunque no garantiza encontrar siempre el óptimo global.

## Conclusión
- *Si queremos la solución exacta**, `exact_global_min` es el método apropiado, aunque es costoso.
- *Si buscamos eficiencia**, `local_search_with_restarts` proporciona una solución aproximada en mucho menos tiempo, con un bajo riesgo de quedarse atrapado en un mínimo local.

Al combinar técnicas de búsqueda local con reinicios, podemos encontrar soluciones cercanas al óptimo sin incurrir en altos costos computacionales.

Aún así en este problema tan sencillo la diferencia no es notable al usar cualquiera de los dos ya que son pocos datos.

[Guía de instalación y uso del proyecto](how_to_execute.md)