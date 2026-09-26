// Catálogo del recomendador. Cada producto es un nodo del grafo,
// las tags y la categoría son las que usa grafo.js para armar las aristas.

const PRODUCTOS = [
  // ------- Electrónica -------
  { id: 1, nombre: "Audífonos inalámbricos", categoria: "Electrónica", precio: 129000, icono: "🎧", tags: ["tecnología", "música", "viaje"] },
  { id: 2, nombre: "Smartwatch fitness", categoria: "Electrónica", precio: 259000, icono: "⌚", tags: ["tecnología", "fitness", "running"] },
  { id: 3, nombre: "Teclado mecánico", categoria: "Electrónica", precio: 189000, icono: "⌨️", tags: ["tecnología", "gaming", "oficina"] },
  { id: 4, nombre: "Power bank 20000mAh", categoria: "Electrónica", precio: 89000, icono: "🔋", tags: ["tecnología", "viaje"] },
  { id: 5, nombre: "Cámara instantánea", categoria: "Electrónica", precio: 219000, icono: "📷", tags: ["tecnología", "viaje", "fotografía"] },

  // ------- Hogar -------
  { id: 6, nombre: "Cafetera de goteo", categoria: "Hogar", precio: 145000, icono: "☕", tags: ["cocina", "oficina"] },
  { id: 7, nombre: "Set de sábanas de algodón", categoria: "Hogar", precio: 98000, icono: "🛏️", tags: ["descanso", "relajación"] },
  { id: 8, nombre: "Difusor de aromas", categoria: "Hogar", precio: 76000, icono: "🕯️", tags: ["relajación", "decoración"] },
  { id: 9, nombre: "Organizador de escritorio", categoria: "Hogar", precio: 45000, icono: "🗂️", tags: ["oficina", "decoración"] },
  { id: 10, nombre: "Lámpara LED de lectura", categoria: "Hogar", precio: 62000, icono: "💡", tags: ["lectura", "oficina", "decoración"] },

  // ------- Deportes -------
  { id: 11, nombre: "Tenis para correr", categoria: "Deportes", precio: 249000, icono: "👟", tags: ["running", "fitness", "outdoor"] },
  { id: 12, nombre: "Botella térmica", categoria: "Deportes", precio: 54000, icono: "🧴", tags: ["running", "fitness", "outdoor", "viaje"] },
  { id: 13, nombre: "Colchoneta de yoga", categoria: "Deportes", precio: 68000, icono: "🧘", tags: ["fitness", "relajación"] },
  { id: 14, nombre: "Mochila de senderismo", categoria: "Deportes", precio: 175000, icono: "🎒", tags: ["outdoor", "viaje"] },
  { id: 15, nombre: "Banda de resistencia", categoria: "Deportes", precio: 32000, icono: "➰", tags: ["fitness"] },

  // ------- Moda -------
  { id: 16, nombre: "Chaqueta impermeable", categoria: "Moda", precio: 210000, icono: "🧥", tags: ["outdoor", "viaje"] },
  { id: 17, nombre: "Reloj clásico de cuero", categoria: "Moda", precio: 165000, icono: "⌚", tags: ["oficina", "decoración"] },
  { id: 18, nombre: "Gafas de sol polarizadas", categoria: "Moda", precio: 88000, icono: "🕶️", tags: ["viaje", "outdoor"] },
  { id: 19, nombre: "Zapatillas urbanas", categoria: "Moda", precio: 132000, icono: "👞", tags: ["moda", "viaje"] },
  { id: 20, nombre: "Bufanda de lana", categoria: "Moda", precio: 39000, icono: "🧣", tags: ["moda", "descanso"] },

  // ------- Libros -------
  { id: 21, nombre: "Novela de ciencia ficción", categoria: "Libros", precio: 52000, icono: "📘", tags: ["lectura", "relajación"] },
  { id: 22, nombre: "Algoritmos y estructuras de datos", categoria: "Libros", precio: 89000, icono: "📗", tags: ["lectura", "tecnología", "oficina"] },
  { id: 23, nombre: "Diario de gratitud", categoria: "Libros", precio: 34000, icono: "📓", tags: ["lectura", "relajación", "descanso"] },
  { id: 24, nombre: "Atlas de senderismo", categoria: "Libros", precio: 61000, icono: "🗺️", tags: ["lectura", "outdoor", "viaje"] },
  { id: 25, nombre: "Recetario internacional", categoria: "Libros", precio: 47000, icono: "📕", tags: ["lectura", "cocina"] },

  // ------- Belleza -------
  { id: 26, nombre: "Crema hidratante facial", categoria: "Belleza", precio: 58000, icono: "🧴", tags: ["relajación", "cuidado personal"] },
  { id: 27, nombre: "Set de brochas de maquillaje", categoria: "Belleza", precio: 72000, icono: "💄", tags: ["cuidado personal", "moda"] },
  { id: 28, nombre: "Aceite esencial de lavanda", categoria: "Belleza", precio: 41000, icono: "🌿", tags: ["relajación", "cuidado personal"] },
  { id: 29, nombre: "Cepillo de dientes eléctrico", categoria: "Belleza", precio: 96000, icono: "🪥", tags: ["cuidado personal", "tecnología"] },
  { id: 30, nombre: "Kit de manicura", categoria: "Belleza", precio: 38000, icono: "💅", tags: ["cuidado personal", "moda"] },
];
