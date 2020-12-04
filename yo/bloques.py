import datetime
import hashlib
import json
import random as r
from transaccion import Transactions

class Bloques:
    def __init__(self,pre,src,dts):
        self.obj_trans = Transactions(src,dts)
        self.block_ = {}
        self.block_['header'] = {}
        self.block_['transactions'] = []
        self.nonce= 0
        self.time = 0
        self.prev_hash = pre
        self.transactions = []
        self.hash_tx0 = self.get_hash_trans()
        self.hash_header = ""
        self.proofofwords()

    def proofofwords(self):
        DificulBits_=10#20#32 se totea mi pc
        yess_= True
        while yess_:
            nonce = abs(r.getrandbits(32))
            self.nonce=nonce
            self.time = int(datetime.datetime.utcnow().timestamp())
            self.hash_header = self.get_hash_header()
            _bytes = json.dumps(self.block_).encode("utf-8")
            _hash = hashlib.sha256(_bytes).digest()
            int_hash = int.from_bytes(_hash,byteorder= 'big')
            if int_hash.bit_length() <= (256- DificulBits_):
                print("yesss!!")
                yess_=False


    def get_hash_trans(self):
        a=self.obj_trans.createTrans()
        self.block_['transactions'].append(a)
        jtrans_ = json.dumps(a)
        self.transactions.append(jtrans_)
        return hashlib.sha256(jtrans_.encode('utf-8')).hexdigest()

    def get_hash_header(self):
        self.block_['header']={
            "nonce":self.nonce,
            "time": self.time,
            "prevhash":self.prev_hash,
            "txhash":self.hash_tx0
        }
        #with open('./json/header.json', 'w') as file:json.dump(self.block_['header'], file, indent=5)
        jheader_= json.dumps(self.block_['header'])
        return hashlib.sha256(jheader_.encode('utf-8')).hexdigest()

    def block_toJson(self):
        with open('./json/block.json', 'w') as file:json.dump(self.block_, file, indent=5)
    
    def jsonToBlock(self):
        pass

# genesis='51d5664ef15bbad7e4f2acd595faf5a213980b4c274becd440911516312ea9ec'
# dts = "68fc76742406347377af7923e68ec877a89ad0c08079aeea65d933aa73309d48bccfdad8c100ff540c905cef8ec45ea3b940f4f4171def91d9ab218e6773c519"
# x = Bloques(genesis,"",dts)
# print("Nonce: ",str(x.nonce))
# print("Time: ",str(x.time))
# print("prev-hash: ",str(x.prev_hash))
# print("hash-trans: ",str(x.hash_tx0))
# print("transaciones: ",str(x.transactions))
# print("hash-header: ",str(x.hash_header))
# print("block-: ",str(x.block_['header']))
# x.block_toJson()
