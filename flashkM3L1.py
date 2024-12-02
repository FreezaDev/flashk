from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>Hello, World!</h1>
    <a href="/YEOEOEOOEOUCH"> 1-9Aleatorio   </a>
    <a href="/aleatorio"> |lista aleatoria   </a>
    <a href="/numeros"> |numeros   </a>
    <a href="/Money"> |Moneda   </a>
    <a href="/pwd"> |Contraseña </a>
    """
    
@app.route("/numeros")
def numeros():
    return "<h1>1, 2, 3, 4, 5</h1>"

@app.route("/YEOEOEOOEOUCH")
def random1():
    hola = random.randint(1,9)
    return f"<h2> {hola} </h2>"

@app.route("/aleatorio")
def aleatorio():
    datos = ["hola", "chau", "adios"]
    return f"<h1> {random.choice(datos)}</h1>"

@app.route("/Money")
def moneda():
    cara = random.choice(["Cara", "Sello"])
    return f"""
    <h1> {cara} </h1>
    <a href="/Money"> Volver a lanzar </a>
    <a href="/"> Volver </a>
    """
@app.route("/pwd")
def contra():
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.-/*+$%&!?"
    autopwd = ""
    for i in range(12):
        autopwd = autopwd + random.choice(caracteres)
    return f"""
    <h1>{autopwd}</h1>
    <a href="/pwd"> Regenerar </a>
    <a href="/"> Volver </a>

    """


app.run(debug=True)
