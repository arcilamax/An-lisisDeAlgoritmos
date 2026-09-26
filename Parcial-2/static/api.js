// Capa que conecta el grafo + PageRank con el frontend. El frontend solo
// habla con este objeto, no le importa cómo se arma el grafo por dentro.
// Como todo corre en el navegador (sin servidor), las funciones son async
// y simulan un pequeño delay de red, como si fueran llamadas a una API real.

const RecommenderAPI = (function () {
  let productos = [];
  let grafo = null;
  let cacheTendencias = null;

  function inicializar(listaProductos) {
    productos = listaProductos;
    grafo = GrafoProductos.construir(productos);
    cacheTendencias = null;
  }

  function _productoPorId(id) {
    return productos.find((p) => p.id === id);
  }

  function _simularLatencia(datos, ms = 220) {
    return new Promise((resolve) => setTimeout(() => resolve(datos), ms));
  }

  function _ordenarPorScore(scoresMap) {
    return productos
      .map((p) => ({ producto: p, score: scoresMap.get(p.id) || 0 }))
      .sort((a, b) => b.score - a.score);
  }

  async function obtenerCatalogo() {
    return _simularLatencia(productos);
  }

  // pagerank global, se calcula una sola vez y se cachea
  async function obtenerTendencias(top = 5) {
    if (!cacheTendencias) {
      const scores = PageRank.calcularGlobal(grafo);
      cacheTendencias = _ordenarPorScore(scores);
    }
    return _simularLatencia(cacheTendencias.slice(0, top));
  }

  // pagerank personalizado tomando productoId como semilla
  async function obtenerRecomendaciones(productoId, top = 5) {
    const scores = PageRank.calcularPersonalizado(grafo, productoId);
    const ordenado = _ordenarPorScore(scores).filter((r) => r.producto.id !== productoId);
    return _simularLatencia(ordenado.slice(0, top));
  }

  // vecinos directos, solo se usa para resaltar el grafo en la UI
  function obtenerVecinos(productoId) {
    return GrafoProductos.vecinosDe(grafo, productoId).map((e) => e.destino);
  }

  function obtenerProducto(id) {
    return _productoPorId(id);
  }

  return {
    inicializar,
    obtenerCatalogo,
    obtenerTendencias,
    obtenerRecomendaciones,
    obtenerVecinos,
    obtenerProducto,
  };
})();
