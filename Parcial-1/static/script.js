/**
 * script.js
 * ---------
 * Maneja el teclado numérico del cajero, llama a la API /api/cambio
 * (que ejecuta el algoritmo Greedy en el backend) y pinta el
 * desglose de billetes/monedas entregado.
 */

const montoInput = document.getElementById("monto");
const errorEl = document.getElementById("error");
const btnDispensar = document.getElementById("btn-dispensar");

const resultEmpty = document.getElementById("result-empty");
const resultBody = document.getElementById("result-body");
const billsList = document.getElementById("bills-list");
const tallyTotal = document.getElementById("tally-total");
const tallyRemainderRow = document.getElementById("tally-remainder-row");
const tallyRemainder = document.getElementById("tally-remainder");

const COINS = new Set([500, 200, 100, 50]);

function formatCOP(n) {
  return "$" + Number(n).toLocaleString("es-CO");
}

// --- Teclado numérico ---
document.querySelectorAll(".key[data-key]").forEach((btn) => {
  btn.addEventListener("click", () => {
    const key = btn.dataset.key;
    if (key === "clear") {
      montoInput.value = "";
    } else {
      montoInput.value = (montoInput.value + key).replace(/^0+(?=\d)/, "");
    }
    hideError();
  });
});

// --- Montos rápidos ---
document.querySelectorAll(".quick").forEach((btn) => {
  btn.addEventListener("click", () => {
    montoInput.value = btn.dataset.amount;
    hideError();
  });
});

montoInput.addEventListener("input", () => {
  montoInput.value = montoInput.value.replace(/[^\d]/g, "");
});

btnDispensar.addEventListener("click", dispensar);
montoInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") dispensar();
});

function hideError() {
  errorEl.hidden = true;
}

function showError(msg) {
  errorEl.textContent = msg;
  errorEl.hidden = false;
}

async function dispensar() {
  const monto = montoInput.value;

  if (!monto || Number(monto) <= 0) {
    showError("Ingresa un monto mayor a cero.");
    return;
  }

  btnDispensar.disabled = true;
  btnDispensar.textContent = "Calculando…";

  try {
    const res = await fetch("/api/cambio", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ monto: Number(monto) }),
    });

    const data = await res.json();

    if (!res.ok) {
      showError(data.error || "No se pudo calcular el cambio.");
      return;
    }

    hideError();
    renderResultado(data);
  } catch (err) {
    showError("No se pudo conectar con el servidor.");
  } finally {
    btnDispensar.disabled = false;
    btnDispensar.textContent = "Dispensar";
  }
}

function renderResultado(data) {
  billsList.innerHTML = "";

  const maxCantidad = Math.max(...data.detalle.map((d) => d.cantidad), 1);

  data.detalle.forEach((item) => {
    const li = document.createElement("li");
    const isCoin = COINS.has(item.denominacion);
    li.className = "bill-row" + (isCoin ? " bill-row--coin" : "");

    const pct = Math.max(8, Math.round((item.cantidad / maxCantidad) * 100));

    li.innerHTML = `
      <span class="bill-row__denom">${formatCOP(item.denominacion)}</span>
      <span class="bill-row__bar-track">
        <span class="bill-row__bar-fill" style="width:${pct}%"></span>
      </span>
      <span class="bill-row__qty">x${item.cantidad}</span>
    `;
    billsList.appendChild(li);
  });

  tallyTotal.textContent = data.total_piezas;

  if (data.monto_no_cubierto > 0) {
    tallyRemainder.textContent = formatCOP(data.monto_no_cubierto);
    tallyRemainderRow.hidden = false;
  } else {
    tallyRemainderRow.hidden = true;
  }

  resultEmpty.hidden = true;
  resultBody.hidden = false;
}
