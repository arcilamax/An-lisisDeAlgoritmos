// Arma el grafo (no dirigido, ponderado) a partir de la lista de productos.
// Nodo = producto. Arista = comparten categoría y/o tags. El peso indica
// qué tan relacionados están.

const GrafoProductos = (function () {
  const PESO_MISMA_CATEGORIA = 1.0;
  const PESO_POR_TAG_COMPARTIDO = 1.5;

  // Peso de la arista entre dos productos (0 si no van conectados)
  function calcularPeso(a, b) {
    let peso = 0;

    if (a.categoria === b.categoria) {
      peso += PESO_MISMA_CATEGORIA;
    }

    const tagsA = new Set(a.tags);
    const compartidos = b.tags.filter((t) => tagsA.has(t)).length;
    peso += compartidos * PESO_POR_TAG_COMPARTIDO;

    return peso;
  }

  // Lista de adyacencia: { nodos: [...], adyacencia: Map(id -> [{destino, peso}]) }
  function construir(productos) {
    const nodos = productos.map((p) => p.id);
    const adyacencia = new Map(nodos.map((id) => [id, []]));

    for (let i = 0; i < productos.length; i++) {
      for (let j = i + 1; j < productos.length; j++) {
        const a = productos[i];
        const b = productos[j];
        const peso = calcularPeso(a, b);

        if (peso > 0) {
          adyacencia.get(a.id).push({ destino: b.id, peso });
          adyacencia.get(b.id).push({ destino: a.id, peso });
        }
      }
    }

    return { nodos, adyacencia };
  }

  // Vecinos directos de un nodo (se usa para resaltar el recorrido en la UI)
  function vecinosDe(grafo, id) {
    return grafo.adyacencia.get(id) || [];
  }

  return { construir, vecinosDe };
})();
