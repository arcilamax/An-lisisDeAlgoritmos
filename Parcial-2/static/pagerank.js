// PageRank sobre el grafo de productos, con iteración de potencias:
// PR(v) = (1-d)*teleport(v) + d * suma( PR(u)*peso(u,v)/pesoTotal(u) )
//
// Lo usamos de dos formas, cambiando el vector de teleportación:
// - global: teleport uniforme (1/N) -> qué tan central es cada producto
// - personalizado: teleport = 1 solo en el producto semilla -> qué tan
//   relacionado está cada producto CON ese producto puntual

const PageRank = (function () {
  const DAMPING_POR_DEFECTO = 0.85;
  const MAX_ITERACIONES = 100;
  const TOLERANCIA = 1e-8;

  function calcular(grafo, opciones = {}) {
    const damping = opciones.damping ?? DAMPING_POR_DEFECTO;
    const nodos = grafo.nodos;
    const n = nodos.length;

    // uniforme si no hay semilla, o todo concentrado en el nodo semilla
    const teleport = new Map();
    if (opciones.semilla !== undefined && opciones.semilla !== null) {
      nodos.forEach((id) => teleport.set(id, id === opciones.semilla ? 1 : 0));
    } else {
      nodos.forEach((id) => teleport.set(id, 1 / n));
    }

    // para normalizar la probabilidad de pasar de un nodo a sus vecinos
    const pesoTotal = new Map();
    nodos.forEach((id) => {
      const vecinos = grafo.adyacencia.get(id) || [];
      pesoTotal.set(id, vecinos.reduce((acc, e) => acc + e.peso, 0));
    });

    let rank = new Map(teleport);

    for (let iter = 0; iter < MAX_ITERACIONES; iter++) {
      const nuevoRank = new Map();
      nodos.forEach((id) => nuevoRank.set(id, (1 - damping) * teleport.get(id)));

      nodos.forEach((u) => {
        const total = pesoTotal.get(u);
        if (total === 0) return; // nodo aislado, no reparte nada
        const vecinos = grafo.adyacencia.get(u);
        const rankU = rank.get(u);
        vecinos.forEach(({ destino, peso }) => {
          nuevoRank.set(destino, nuevoRank.get(destino) + damping * rankU * (peso / total));
        });
      });

      // si casi no cambió respecto a la iteración anterior, ya convergió
      let diferencia = 0;
      nodos.forEach((id) => (diferencia += Math.abs(nuevoRank.get(id) - rank.get(id))));

      rank = nuevoRank;
      if (diferencia < TOLERANCIA) break;
    }

    return rank; // Map(id -> score)
  }

  function calcularGlobal(grafo, damping) {
    return calcular(grafo, { damping });
  }

  function calcularPersonalizado(grafo, semilla, damping) {
    return calcular(grafo, { damping, semilla });
  }

  return { calcular, calcularGlobal, calcularPersonalizado };
})();
