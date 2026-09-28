# Recomendador por grafo (PageRank)

Examen 2 - Análisis de Algoritmos

## Video de sustentación

**[AGREGAR AQUÍ EL LINK DEL VIDEO]**

## Problema

En una tienda con muchos productos, ¿cómo recomendar qué ver después de
un producto sin escribir reglas a mano? Este proyecto modela el catálogo
como un grafo y usa PageRank para calcular qué productos son más
relevantes.

## Solución

- Cada producto es un **nodo** del grafo (30 productos en 6 categorías).
- Dos productos se conectan con una **arista con peso** si comparten
  categoría o etiquetas. A más cosas en común, más peso.
- Sobre ese grafo se corre **PageRank** de dos formas:
  - **Global**: qué tan central es cada producto en todo el catálogo
    (sección "Tendencias generales").
  - **Personalizado**: qué tan relacionado está cada producto con el que
    el usuario está viendo (recomendación "porque viste X").

## Algoritmo: PageRank

Simula un recorrido aleatorio por el grafo: en cada paso se sigue una
arista hacia un vecino (con más probabilidad las de mayor peso) o se
reinicia en otro nodo. Los productos más visitados a la larga tienen mayor
puntaje. Se calcula iterando esta fórmula hasta que converge:

```
PR(v) = (1 - d) * teleport(v) + d * Σ PR(u) * peso(u,v) / pesoTotal(u)
```

- `d = 0.85` (factor de amortiguamiento).
- En el global, `teleport(v) = 1/N` para todos los nodos.
- En el personalizado, `teleport(v) = 1` solo en el producto elegido.

## Estructura

```
├── app.py               # servidor Flask
├── requirements.txt
├── templates/
│   └── index.html       # página principal
└── static/
    ├── productos.js     # catálogo de productos
    ├── grafo.js         # construcción del grafo
    ├── pagerank.js      # algoritmo PageRank
    ├── api.js           # capa que conecta el algoritmo con la interfaz
    ├── app.js           # lógica de la interfaz
    └── style.css        # estilos
```

## Cómo ejecutarlo

```bash
pip install -r requirements.txt
python app.py
```

Luego abrir `http://127.0.0.1:5000` en el navegador.
