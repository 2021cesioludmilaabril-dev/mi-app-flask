from flask import Flask, render_template, request, session, redirect
from random import shuffle

app = Flask(__name__)
app.secret_key = "trivia123"

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

    if "indice" not in session:
        session["indice"] = 0
        session["puntaje"] = 0

    if request.method == "POST":
        correcta = preguntas[session["indice"]][2]

        if request.form["respuesta"] == correcta:
            session["puntaje"] += 1

        session["indice"] += 1

    if session["indice"] >= len(preguntas):
        puntaje = session["puntaje"]
        session.clear()

        return render_template(
            "index.html",
            terminado=True,
            puntaje=puntaje,
            total=len(preguntas)
        )

    pregunta, opciones, correcta = preguntas[session["indice"]]

    opciones_mezcladas = opciones[:]
    shuffle(opciones_mezcladas)

    return render_template(
        "index.html",
        terminado=False,
        pregunta=pregunta,
        opciones=opciones_mezcladas
    )
@app.route("/reiniciar")
def reiniciar():
    session.clear()
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)
