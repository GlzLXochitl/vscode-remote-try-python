#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

opciones = ['piedra', 'papel', 'tijera']

eleccion_usuario = input("Elige piedra, papel o tijera: ")
eleccion_computadora = random.choice(opciones)

print("La computadora eligió: " + eleccion_computadora)

if eleccion_usuario == eleccion_computadora:
    print("Es un empate")
elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijera') or \
     (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
     (eleccion_usuario == 'tijera' and eleccion_computadora == 'papel'):
    print("¡Ganaste!")
else:
    print("Perdiste")