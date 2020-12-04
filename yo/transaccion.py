import datetime
import hashlib
import json
import random as r
class Transactions:

    def __init__(self,source,destiny):
        self.nonce = abs(r.getrandbits(32))
        self.src = source
        self.dst = destiny
        self.amount = 50000000000000
        self.signature= ""

    def createTrans(self):
        trans_ = {
            #"Nonce": str(abs(r.randint(-2**31,(2**31)-1))),
            "nonce":self.nonce,
            "src":self.src,
            "dst":self.dst,
            "amount": self.amount,
            "signature": self.signature
        }
        return trans_
    