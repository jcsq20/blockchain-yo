import datetime
import hashlib
import json
import random as r
import urllib
import threading
from bloques import Bloques

class Peer:

    def __init__(self, ip, port):
        self.addres = ip
        self.port = port

    def send_json(self,data:{},url):
        url="http://"+self.addres+":"+self.port+"/"+url
        req = urllib.request(url)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata= json.dumps(data)
        jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
        req.add_header('Content-Length', len(jsondataasbytes))
        req= urllib.urlopen(url=url,data=jsondataasbytes, timeout=1)
        return json.load(req)

class Blockchain:

    def __init__(self):
        self.peers = []
        self.genesis = '51d5664ef15bbad7e4f2acd595faf5a213980b4c274becd440911516312ea9ec'
        self.dts = "68fc76742406347377af7923e68ec877a89ad0c08079aeea65d933aa73309d48bccfdad8c100ff540c905cef8ec45ea3b940f4f4171def91d9ab218e6773c519"
        self.blok = Bloques(self.genesis,"",self.dts)
        self.bloks=[]
        self.bloks.append(self.blok)
        self.bandera= threading.Event()
        #minero=threading.Thread(target= self.Miner, args=())
        #minero.start()
        #print("----------------GOOOO!!!-------------")
    
    def get_last_blocks(self,lastknown:str):#preguntar
        blocks = []
        #pass_=False
        for bl in self.bloks:
            bl:Bloques
            if bl.hash_header == lastknown:
                blocks.append(bl)
            #     pass_=True
            # if pass_:
            #     blocks.append(bl)
        # loop blocks
        return blocks

    def append_block(self):#preguntar validacions
        add = True
        last_block = self.bloks[len(self.bloks)-1]
        block = Bloques(last_block.hash_header,last_block.obj_trans.dst,"")
        if add:
            self.bloks.append(block)
    
    def minero(self):
        yess_= True
        while yess_:
            self.bandera.set()
            last_block = self.bloks[len(self.bloks)-1]
            create_bl = Bloques(last_block.hash_header,last_block.obj_trans.dst,"")
            if self.bandera.is_set():
                self.bloks.append(create_bl)
            self.bandera.set()


    def blockchain_toJson(self):
        temp1 = []
        for re in range(0,len(self.bloks)):
            obj_=self.bloks[re]
            temp1.append(obj_.block_)
        with open('./json/blockchain.json', 'w') as file:json.dump(temp1, file, indent=6)

    def register_peer(self,peer):
            self.peers.append(peer)


a = Blockchain()
a.append_block()
a.blockchain_toJson()