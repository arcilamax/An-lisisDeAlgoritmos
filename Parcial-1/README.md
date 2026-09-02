# Dispensa — Cajero automático con retiro óptimo (Algoritmo Greedy)

Proyecto para el Examen 1 de Análisis de Algoritmos — Opción 1 (Desarrollo).

## Problema

Un cajero automático debe entregar un monto solicitado por el usuario
usando el **menor número posible de billetes y monedas**, a partir de
las denominaciones disponibles en Colombia:

```
$100.000, $50.000, $20.000, $10.000, $5.000, $2.000,
$1.000, $500, $200, $100, $50
```

Por ejemplo, para entregar **$187.650**, el cajero no debería sacar 1.876
monedas de $100: debería sacar 9 piezas en total (1 billete de cada
denominación, más una moneda de $50).

## Algoritmo utilizado: Greedy (voraz)

En cada paso, el algoritmo toma la **denominación más grande disponible
que quepa en el monto restante**, la usa tantas veces como sea posible,
y continúa con la siguiente denominación más pequeña. Nunca reconsidera
una decisión ya tomada — de ahí el nombre "voraz": siempre toma la mejor
opción *local* disponible en el momento.

```
mientras el monto restante > 0:
    elegir la denominación más grande <= monto restante
    usarla tantas veces como sea posible
    restar ese valor del monto restante
```

### ¿Por qué funciona (y minimiza piezas) en este caso?

El sistema de denominaciones colombiano es un **sistema canónico**: cada
denominación es igual o múltiplo cercano de la inmediatamente menor
(100.000 → 50.000 → 20.000 → 10.000...). En este tipo de sistemas,
la estrategia greedy siempre produce el número mínimo de piezas — a
diferencia de sistemas de denominaciones "raros" (por ejemplo, monedas
de 1, 3 y 4), donde greedy puede no ser óptimo y se necesitaría
programación dinámica.

**Complejidad:** O(d), donde d es el número de denominaciones (11 en
este caso) — es prácticamente instantáneo sin importar el monto.


## Cómo ejecutarlo

```bash
pip install -r requirements.txt
python3 app.py
```

Abrir en el navegador: **http://127.0.0.1:5000**

Para correr las pruebas del algoritmo:

```bash
python3 -m unittest test_greedy.py -v
```

## Cómo se aplicó el algoritmo a la solución

1. El usuario ingresa un monto en la pantalla del cajero (interfaz web).
2. El frontend (`script.js`) envía ese monto al backend vía
   `POST /api/cambio`.
3. El backend (`app.py`) llama a `calcular_cambio_greedy()` en
   `greedy.py`, que ejecuta el algoritmo voraz descrito arriba.
4. El resultado (detalle de billetes/monedas, cantidad total de piezas)
   se devuelve como JSON y la interfaz lo dibuja como un desglose visual.


## Video de sustentación

[Enlace al video](AGREGAR-ENLACE-AQUI)
