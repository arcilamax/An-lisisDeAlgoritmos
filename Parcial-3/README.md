# Reserva óptima de aulas con Programación Dinámica

Parcial de Análisis de Algoritmos. Lenguaje: Python 3.8+ (sin dependencias externas).

## Cómo ejecutar
```bash
cd reservas_aulas
python main.py                      # todas las aulas
python main.py --aula "Aula 101"    # una sola aula
python -m unittest -v               # pruebas
```

## 1. Problema que se desea solucionar
Una universidad recibe solicitudes para reservar aulas. Cada solicitud tiene aula,
hora de inicio, hora de fin y un valor (ingreso). En una misma aula dos reservas no
pueden cruzarse. Se quiere elegir, para cada aula, el conjunto de reservas
compatibles que **maximice el ingreso total**.

## 2. Algoritmo de Programación Dinámica seleccionado
Planificación de intervalos con peso (*Weighted Interval Scheduling*).
Cada aula se resuelve de forma independiente.

## 3. Definición del estado / subproblemas
Con las reservas de un aula ordenadas por hora de fin (1..n):

`dp[i]` = máximo ingreso usando únicamente las primeras `i` reservas.

## 4. Relación de recurrencia
`p(i)` = número de reservas que terminan a la hora de inicio de la reserva `i` o antes
(la última compatible con `i`, calculada con búsqueda binaria).

```
dp[i] = max( dp[i-1],                 # no aceptar la reserva i
             ingreso[i] + dp[p(i)] )  # aceptar la reserva i
```

## 5. Casos base
`dp[0] = 0` (sin reservas no hay ingreso). Una reserva que termina justo cuando
empieza otra es compatible (intervalos `[inicio, fin)`).

## 6. Implementación
| Archivo | Contenido |
|---|---|
| `modelo.py` | `Reserva` y `Resultado` |
| `datos.py` | Caso real: solicitudes de 3 aulas |
| `algoritmo_pd.py` | Orden, `p(i)`, tabla `dp`, reconstrucción, `planificar_por_aula` |
| `voraz.py` | Estrategia voraz usada para comparar |
| `reportes.py` | Impresión de tablas y resultados |
| `main.py` | Programa de consola |
| `test_algoritmo.py` | Pruebas (incluye verificación contra fuerza bruta) |

Complejidad: O(n log n) por aula (ordenar + búsqueda binaria + un recorrido).

## 7. Resultados obtenidos
Ejecutar `python main.py` muestra, por aula, la tabla de PD, las reservas aceptadas y
la comparación con la estrategia voraz (aceptar siempre la más cara), que no siempre
es óptima.


## Link Video
https://www.youtube.com/watch?v=9xM9NeXjzBQ

