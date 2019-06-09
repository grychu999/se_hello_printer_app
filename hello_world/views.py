from hello_world import app
from formater import get_formatted
from formater import SUPPORTED, PLAIN
from flask import request

moje_imie = "Grzegorz"
msg = "Hello World!"
#name = ""

@app.route('/')
def index():
    name = request.args.get ('name')
    if not name:
        name = moje_imie
    output = request.args.get('output')
    if not output:
        output = PLAIN
    return get_formatted(
        msg, name, output.lower())

@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
