"""
app.py
------
Servidor web (Flask) que expone el algoritmo Greedy de cambio de
cajero automático a través de una interfaz web y una API JSON.
"""

from flask import Flask, render_template, request, jsonify
from greedy import calcular_cambio_greedy, DENOMINACIONES

app = Flask(__name__)


@app.route("/")
def index():
    """Sirve la página principal del cajero."""
    return render_template("index.html", denominaciones=DENOMINACIONES)


@app.route("/api/cambio", methods=["POST"])
def api_cambio():
    """
    Recibe un monto en JSON: {"monto": 187650}
    Devuelve el detalle del cambio calculado con el algoritmo Greedy.
    """
    data = request.get_json(silent=True) or {}
    monto = data.get("monto")

    if monto is None:
        return jsonify({"error": "Debes enviar un campo 'monto'."}), 400

    try:
        monto = int(monto)
        if monto < 0:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({"error": "El monto debe ser un entero positivo."}), 400

    resultado = calcular_cambio_greedy(monto)
    return jsonify(resultado.to_dict())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
