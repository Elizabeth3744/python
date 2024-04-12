from flask import Flask, request
app = Flask(__name__)
@app.route("/saludar")
def saludar():
    return "<h1>Hola Mundo<h1>"
@app.route("/verhora")
def hora():
    return "<h1>la hora es : <h1>"
@app.route("/factorial")
def factorial():
    fact = 1
    num = int(request.args.get('num'))
    for x in range(1, num + 1): #más 1 porque range no reconoce el último valor
        fact *= x
    return str(fact)