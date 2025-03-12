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
python app.py
```

---

## Uso del Programa

Al ejecutar el programa, se te solicitará seleccionar un método de búsqueda. Las opciones disponibles son:

- Búsqueda Voraz:  
  Se selecciona la estación con mayor cobertura en cada paso.

- Búsqueda Aleatoria:  
  Se prueban combinaciones aleatorias de estaciones para optimizar la selección.

### Instrucciones de Uso

1. Escribe 1 para Búsqueda Voraz o 2 para Búsqueda Aleatoria y presiona Enter.
2. El programa mostrará la mejor combinación de estaciones para cubrir todos los estados dados.

Notas Adicionales:
- Si introduces una opción inválida, el programa utilizará por defecto la Búsqueda Voraz.
- Puedes modificar el número de iteraciones en el código de la búsqueda aleatoria ajustando el parámetro "iterations" en la función "random_search".
---
