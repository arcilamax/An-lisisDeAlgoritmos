// pagerank.js
// Calcula PageRank sobre el grafo de productos usando iteración de potencias
// (power iteration): se arranca con un vector inicial y se va actualizando
// hasta que los valores casi no cambian entre una vuelta y la siguiente.
//
// Fórmula para cada nodo v:
//
//   PR(v) = (1 - d) * teletransporte(v) + d * Σ_u  PR(u) * peso(u,v) / pesoTotal(u)
//
// - "teletransporte" es el vector de reinicio: la probabilidad de que el
//   paseo aleatorio "salte" directo a v en vez de seguir una arista desde
//   donde estaba. Con este mismo código calculamos dos variantes, cambiando
//   solo ese vector:
//     · PageRank GLOBAL: teletransporte uniforme (1/N en cada nodo) -> mide
//       qué tan central es un producto en TODO el grafo (para "Tendencias").
//     · PageRank PERSONALIZADO: toda la probabilidad de reinicio se concentra
//       en un único nodo semilla -> mide qué tan relacionado está cada
//       producto CON ESE nodo puntual (para "elige un producto y te recomiendo").
// - d (damping / factor de amortiguación) es la probabilidad de seguir una
//   arista en vez de teletransportarse. El valor clásico (el que usaba
//   Google) es 0.85, y es el que usamos por defecto.

const PageRank = (function () {
  const DAMPING_POR_DEFECTO = 0.85;
  const MAX_ITERACIONES = 100;
  const TOLERANCIA = 1e-8;

  // Vector de teletransporte: uniforme si no hay semilla, o concentrado
  // 100% en el nodo semilla si la hay (ver explicación arriba).
  function _vectorTeletransporte(nodos, semilla) {
    const n = nodos.length;
    const teleport = new Map();

    if (semilla === undefined || semilla === null) {
      nodos.forEach((id) => teleport.set(id, 1 / n));
    } else {
      nodos.forEach((id) => teleport.set(id, id === semilla ? 1 : 0));
    }

    return teleport;
  }

  // Suma de pesos de las aristas que salen de cada nodo, para poder repartir
  // proporcionalmente el rank entre los vecinos (normalizar por nodo).
  function _pesoTotalSaliente(grafo) {
    const pesoTotal = new Map();
    grafo.nodos.forEach((id) => {
      const vecinos = grafo.adyacencia.get(id) || [];
      const suma = vecinos.reduce((acc, arista) => acc + arista.peso, 0);
      pesoTotal.set(id, suma);
    });
    return pesoTotal;
  }

  function calcular(grafo, opciones = {}) {
    const damping = opciones.damping ?? DAMPING_POR_DEFECTO;
    const nodos = grafo.nodos;

    const teleport = _vectorTeletransporte(nodos, opciones.semilla);
    const pesoTotal = _pesoTotalSaliente(grafo);

    // Punto de partida: el propio vector de teletransporte
    let rank = new Map(teleport);

    for (let iteracion = 0; iteracion < MAX_ITERACIONES; iteracion++) {
      const nuevoRank = new Map();

      // Parte de "reinicio": (1 - d) * teleport(v)
      nodos.forEach((id) => nuevoRank.set(id, (1 - damping) * teleport.get(id)));

      // Parte que "fluye" por las aristas: cada nodo u reparte su rank
      // actual entre sus vecinos, proporcional al peso de cada arista
      nodos.forEach((u) => {
        const total = pesoTotal.get(u);
        if (total === 0) return; // nodo aislado: no tiene a quién repartirle

        const rankU = rank.get(u);
        const vecinos = grafo.adyacencia.get(u);

        vecinos.forEach(({ destino, peso }) => {
          const aporte = damping * rankU * (peso / total);
          nuevoRank.set(destino, nuevoRank.get(destino) + aporte);
        });
      });

      // Criterio de parada: si el rank ya casi no cambió, convergió
      let diferencia = 0;
      nodos.forEach((id) => {
        diferencia += Math.abs(nuevoRank.get(id) - rank.get(id));
      });

      rank = nuevoRank;
      if (diferencia < TOLERANCIA) break;
    }

    return rank; // Map(id producto -> score de PageRank)
  }

  // PageRank global: qué tan central/popular es cada producto en todo el grafo
  function calcularGlobal(grafo, damping) {
    return calcular(grafo, { damping });
  }

  // PageRank personalizado: qué tan relacionado está cada producto con "semilla"
  function calcularPersonalizado(grafo, semilla, damping) {
    return calcular(grafo, { damping, semilla });
  }

  return { calcular, calcularGlobal, calcularPersonalizado };
})();
