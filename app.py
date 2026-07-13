from flask import Flask, render_template, request
from random import shuffle

app = Flask(__name__)

preguntas = [
    ("¿Dónde queda Río Gallegos?", ["Santa Fe", "Santa Cruz", "San Luis"], "Santa Cruz"),
    ("¿Cuál es el resultado de hacer 5+5x5+3?", ["53", "33", "80"], "33"),
    ("¿En qué fecha patria se conmemora la muerte de Manuel Belgrano? ¿Cómo se reconoce?",
     ["17 de agosto, Día de la Bandera",
      "25 de mayo, Día de la Independencia",
      "20 de junio, Día de la Bandera"],
     "20 de junio, Día de la Bandera")
]

@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = ""

    pregunta, opciones, correcta = preguntas[0]
    opciones_mezcladas = opciones[:]
    shuffle(opciones_mezcladas)

    if request.method == "POST":
        elegida = request.form["respuesta"]
        if elegida == correcta:
            resultado = "¡Correcto!"
        else:
            resultado = "Incorrecto."

    return render_template(
        "index.html",
        pregunta=pregunta,
        opciones=opciones_mezcladas,
        resultado=resultado
    )

if __name__ == "__main__":
    app.run(debug=True)
