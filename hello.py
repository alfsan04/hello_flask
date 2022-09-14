from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hola")
def primeraentrada():
    return "Hola, mundo"

@app.route("/adios")
def salida():
    return "Hasta luego, Mari Carmen"

@app.route("/doble/<int:numero>")
def doble(numero):
    return "el doble de número es " + str(numero*2)

@app.route("/primerhtml")
def primerhtml():
    return render_template("hola.html")