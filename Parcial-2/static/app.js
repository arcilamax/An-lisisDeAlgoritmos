// Toda la manipulación del DOM. Solo habla con RecommenderAPI, no le
// importa cómo se arma el grafo ni cómo se calcula PageRank por dentro.

const formateador = new Intl.NumberFormat("es-CO", { style: "currency", currency: "COP", maximumFractionDigits: 0 });

let productoSeleccionadoId = null;
let categoriaFiltro = "Todas";
let posicionesGrafo = null; // Map(id -> {x, y}) del grafo del héroe

document.addEventListener("DOMContentLoaded", async () => {
  RecommenderAPI.inicializar(PRODUCTOS);

  dibujarGrafoHero();
  await renderizarCatalogo();
  await renderizarTendencias();
  configurarFiltros();
});

// --- catálogo ---

async function renderizarCatalogo() {
  const contenedor = document.getElementById("grid-catalogo");
  const productos = await RecommenderAPI.obtenerCatalogo();
  const visibles = categoriaFiltro === "Todas" ? productos : productos.filter((p) => p.categoria === categoriaFiltro);

  contenedor.innerHTML = "";
  visibles.forEach((p) => {
    const tarjeta = document.createElement("button");
    tarjeta.className = "tarjeta" + (p.id === productoSeleccionadoId ? " seleccionada" : "");
    tarjeta.innerHTML = `
      <span class="icono">${p.icono}</span>
      <span class="categoria">${p.categoria}</span>
      <span class="nombre">${p.nombre}</span>
      <span class="precio">${formateador.format(p.precio)}</span>
    `;
    tarjeta.addEventListener("click", () => seleccionarProducto(p.id));
    contenedor.appendChild(tarjeta);
  });
}

function configurarFiltros() {
  const categorias = ["Todas", ...new Set(PRODUCTOS.map((p) => p.categoria))];
  const contenedor = document.getElementById("filtros-categoria");
  contenedor.innerHTML = "";

  categorias.forEach((cat) => {
    const btn = document.createElement("button");
    btn.className = "filtro" + (cat === categoriaFiltro ? " activo" : "");
    btn.textContent = cat;
    btn.addEventListener("click", async () => {
      categoriaFiltro = cat;
      document.querySelectorAll(".filtro").forEach((f) => f.classList.remove("activo"));
      btn.classList.add("activo");
      await renderizarCatalogo();
    });
    contenedor.appendChild(btn);
  });
}

// --- selección de producto + recomendaciones ---

async function seleccionarProducto(id) {
  productoSeleccionadoId = id;
  await renderizarCatalogo();

  const producto = RecommenderAPI.obtenerProducto(id);
  const panel = document.getElementById("panel-recomendacion");
  const titulo = document.getElementById("titulo-panel");
  const rail = document.getElementById("rail-recomendados");

  titulo.textContent = `Porque viste «${producto.nombre}»`;
  rail.innerHTML = `<p style="color:var(--text-muted)">Calculando PageRank personalizado…</p>`;
  panel.classList.add("visible");
  panel.scrollIntoView({ behavior: "smooth", block: "nearest" });

  const recomendaciones = await RecommenderAPI.obtenerRecomendaciones(id, 5);
  rail.innerHTML = "";
  recomendaciones.forEach(({ producto: p, score }) => {
    const el = document.createElement("div");
    el.className = "item-recomendado";
    el.innerHTML = `
      <span class="icono">${p.icono}</span>
      <span>
        <span class="nombre">${p.nombre}</span>
        <span class="score">score ${score.toFixed(4)}</span>
      </span>
    `;
    rail.appendChild(el);
  });

  const vecinos = RecommenderAPI.obtenerVecinos(id);
  resaltarEnGrafoHero(id, vecinos);
}

// --- tendencias (pagerank global) ---

async function renderizarTendencias() {
  const lista = document.getElementById("lista-tendencias");
  const top = await RecommenderAPI.obtenerTendencias(5);
  const scoreMax = top[0]?.score || 1;

  lista.innerHTML = "";
  top.forEach(({ producto: p, score }, i) => {
    const fila = document.createElement("div");
    fila.className = "fila-tendencia";
    const ancho = Math.max(8, (score / scoreMax) * 100);
    fila.innerHTML = `
      <span class="puesto">#${i + 1}</span>
      <span class="barra-fondo">
        <span class="barra" style="--ancho:${ancho}%"></span>
        <span class="etiqueta">${p.icono} ${p.nombre}</span>
      </span>
      <span class="valor-score">${score.toFixed(4)}</span>
    `;
    lista.appendChild(fila);
  });
}

// --- grafo visual del héroe ---

function dibujarGrafoHero() {
  const svg = document.getElementById("svg-grafo");
  const grafo = GrafoProductos.construir(PRODUCTOS);
  const centro = 210;
  const radio = 175;

  posicionesGrafo = new Map();
  PRODUCTOS.forEach((p, i) => {
    const angulo = (i / PRODUCTOS.length) * 2 * Math.PI;
    posicionesGrafo.set(p.id, {
      x: centro + radio * Math.cos(angulo),
      y: centro + radio * Math.sin(angulo),
    });
  });

  const nsSvg = "http://www.w3.org/2000/svg";
  const grupoAristas = document.createElementNS(nsSvg, "g");
  const grupoNodos = document.createElementNS(nsSvg, "g");

  const aristasDibujadas = new Set();
  grafo.nodos.forEach((id) => {
    grafo.adyacencia.get(id).forEach(({ destino }) => {
      const clave = [id, destino].sort((a, b) => a - b).join("-");
      if (aristasDibujadas.has(clave)) return;
      aristasDibujadas.add(clave);

      const a = posicionesGrafo.get(id);
      const b = posicionesGrafo.get(destino);
      const linea = document.createElementNS(nsSvg, "line");
      linea.setAttribute("x1", a.x);
      linea.setAttribute("y1", a.y);
      linea.setAttribute("x2", b.x);
      linea.setAttribute("y2", b.y);
      linea.setAttribute("class", "arista");
      linea.dataset.n1 = id;
      linea.dataset.n2 = destino;
      grupoAristas.appendChild(linea);
    });
  });

  PRODUCTOS.forEach((p) => {
    const pos = posicionesGrafo.get(p.id);
    const circulo = document.createElementNS(nsSvg, "circle");
    circulo.setAttribute("cx", pos.x);
    circulo.setAttribute("cy", pos.y);
    circulo.setAttribute("r", 4.5);
    circulo.setAttribute("class", "nodo");
    circulo.dataset.id = p.id;
    const titulo = document.createElementNS(nsSvg, "title");
    titulo.textContent = p.nombre;
    circulo.appendChild(titulo);
    grupoNodos.appendChild(circulo);
  });

  svg.innerHTML = "";
  svg.appendChild(grupoAristas);
  svg.appendChild(grupoNodos);
}

function resaltarEnGrafoHero(seedId, vecinosIds) {
  const vecinosSet = new Set(vecinosIds);

  document.querySelectorAll("#svg-grafo .nodo").forEach((nodo) => {
    const id = Number(nodo.dataset.id);
    nodo.classList.remove("nodo--activo", "nodo--vecino");
    if (id === seedId) nodo.classList.add("nodo--activo");
    else if (vecinosSet.has(id)) nodo.classList.add("nodo--vecino");
  });

  document.querySelectorAll("#svg-grafo .arista").forEach((linea) => {
    const n1 = Number(linea.dataset.n1);
    const n2 = Number(linea.dataset.n2);
    const tocaSemilla = n1 === seedId || n2 === seedId;
    const otro = n1 === seedId ? n2 : n1;
    linea.classList.toggle("arista--activa", tocaSemilla && vecinosSet.has(otro));
  });
}
