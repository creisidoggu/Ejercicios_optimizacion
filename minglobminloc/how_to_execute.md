# Ejercicios de Optimización

_Ejercicios de optimización para MIA IABD24/25_


## Clonación del Proyecto

Para comenzar, clona el proyecto ejecutando el siguiente comando:

```bash
git clone https://github.com/creisidoggu/Ejercicios_optimizacion
```

Luego, accede a la carpeta raíz del proyecto:

```bash
cd Ejercicios_optimizacion
```

---

## Ejecución del Código

No requiere de ningún tipo de dependencia así que para ejecutar el código, utiliza el siguiente comando:

```bash
python minglobminloc.py
```

---

## Uso del Programa

Al ejecutar el programa, se te solicitará seleccionar un método de búsqueda. Las opciones disponibles son:

- Búsqueda mínima global:  
  Encuentra la mejor combinación de estaciones considerando el conjunto completo de opciones.

- Búsqueda mínima local:  
  Optimiza la selección de estaciones paso a paso sin garantizar la mejor solución global.

### Instrucciones de Uso

1. Escribe 1 para Búsqueda mínima global o 2 para Búsqueda mínima local y presiona Enter.
2. El programa mostrará la mejor combinación de estaciones para cubrir todos los estados dados.

Notas Adicionales:
- Si introduces una opción inválida, el programa utilizará por defecto la Búsqueda mínima global.
- Puedes modificar el número de iteraciones en el código de la Búsqueda mínima local ajustando el parámetro "iterations" en la función "random_search".
---
