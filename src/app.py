from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import random
import time

from hivemind.state import *
from hivemind.hive import *
from hivemind.insect import *
from hivemind.hex import *

app = Flask(__name__)
socketio = SocketIO(app)

# In future threading/async

state = State()

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def test_connect():
    print("Server Connected")
    emit("my response", {"data": "Connected"})

@socketio.on("disconnect")
def test_disconnect():
    print("Server Disconnected")
    emit("disconnect_ack", {"data": "Disconnected"})

@socketio.on("test")
def test_move(message):
    print("Move requested from client")
    global state
    state = state.next_state()
    json_state = state.to_json()
    print(json_state)
    emit("sendstate", json_state)

@socketio.on("auto_move")
def auto_move(message):
    print("AutoMove requested from client")
    global state
    for i in range(100):
        state = state.next_state()
        json_state = state.to_json()
        print(json_state)
        emit("sendstate", json_state)
        time.sleep(.5)

@socketio.on("selecthex")
def select_hex(hex):
    print(hex)
    hex = Hex(hex["data"]["q"], hex["data"]["r"])
    print(hex)
    print(state.possible_actions)
    print("Server sending move options", hex)
    opts = list(state.possible_actions_for_hex(hex))
    print(state.bee_move)
    print(opts)
    emit("moveoptions", {"options": [[h.q, h.r] for h in opts]})



if __name__ == '__main__':
    socketio.run(app)
