import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    limite = 100

    cont = 1
    numero = 3

    numprimos = "Sequência de Primos: 2 - "

    while cont < limite:
        primo = 1
        for i in range(2, numero):
            if numero % i == 0:
                primo = 0
                break
        if(primo):
            numprimos+=str(numero) + " - "
            cont +=1
        numero+=1

    return numprimos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
