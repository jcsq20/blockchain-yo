import json
from blockchain import Peer, Blockchain
from bloques import Bloques
from flask import Flask, jsonify, request
import urllib.request as urllib



Blockchain_block = Blockchain()


app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'Hello, word!'

@app.route('/peer', methods=['POST'])
def peer():
    global Blockchain_block
    record = json.loads(request.data)
    if "address"in record.keys() and "port" in record.keys():
        peer = Peer(record["address"], record["port"])
        Blockchain_block.register_peer(peer)
        return jsonify({"code":0, "message":"Peer Register"})
    else:
        return jsonify({"code":1, "message":"Error en la insercion de datos"})

@app.route('/getblocks/<lastknown>', methods=["GET"])
def getBlocks(lastknown):
    global Blockchain_block
    return jsonify(Blockchain_block.get_last_blocks(lastknown))

@app.route('/addblock', methods=['POST'])
def addblock():
    global Blockchain_block
    bl = Bloques("","","")
    bloque = bl.jsonToBlock(request.data)
    if bloque == True:
        Blockchain_block.bloks.append(bl)
        return jsonify({"code":0,"message":"Block Register"})
    else:
        return jsonify({"code":1,"message":"Block not Register"})


app.debug=True
app.run(port=5556)
