
import os
import datetime as dt
from flask import Flask, render_template, request, jsonify

current_directory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=current_directory)

class Cuenta:
    def __init__(self, numero, titular, saldo, contactos):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.contactos = contactos
        self.historial = []

BD = [
    Cuenta("21345", "Arnaldo", 200, ["123", "456"]),
    Cuenta("123", "Luisa", 400, ["456"]),
    Cuenta("456", "Andrea", 300, ["21345"])
]

def encontrar_cuenta(numero):
    for cuenta in BD:
        if cuenta.numero == numero:
            return cuenta
    return None

@app.route('/billetera/contactos')
def obtener_contactos():
    minumero = request.args.get('minumero')
    cuenta = encontrar_cuenta(minumero)
    if cuenta:
        contactos = {c.numero: c.titular for c in BD if c.numero in cuenta.contactos}
        return jsonify(contactos)
    else:
        return jsonify({"message": "Cuenta no encontrada"}), 404

@app.route('/billetera/pagar', methods=['POST'])
def pagar():
    minumero = request.form.get('minumero')
    numerodestino = request.form.get('numerodestino')
    valor = float(request.form.get('valor'))

    cuenta_origen = encontrar_cuenta(minumero)
    cuenta_destino = encontrar_cuenta(numerodestino)

    if cuenta_origen and cuenta_destino and cuenta_origen.saldo >= valor:
        cuenta_origen.saldo -= valor
        cuenta_destino.saldo += valor
        cuenta_origen.historial.append(f"Pago realizado de {valor} a {cuenta_destino.titular}")
        cuenta_destino.historial.append(f"Pago recibido de {valor} de {cuenta_origen.titular}")
        return f"Realizado en {dt.datetime.now().date()}"
    else:
        return "Transacción no válida", 400

@app.route('/billetera/historial')
def historial():
    minumero = request.args.get('minumero')
    cuenta = encontrar_cuenta(minumero)
    if cuenta:
        return jsonify({
            "Saldo": cuenta.saldo,  
            "Operaciones": cuenta.historial
        })
    else:
        return "Cuenta no encontrada", 404

@app.route('/')
def index():
    return render_template('billetera.html')


if __name__ == '__main__':
    app.run(debug=False, port=5000)
