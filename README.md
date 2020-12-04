# Design a blockchain that works as follows:
- Proof of Work difficult is 32 bits
- Each block contains header and a list of transactions
- Transaction are organized using a merkle tree data structure
- TXs' Merkle tree root is included in the block header
- TX0 is known as the coinbase, it is a reward for the miner (not need to fill Src or Signature fields)
- The reward is always 5,000,000,000,000 (big interger = 5000000000000)
- Use JSON format for data communication
- Genesis block has is '51d5664ef15bbad7e4f2acd595faf5a213980b4c274becd440911516312ea9ec'

```
BLOCK N:
     +----------------------+  --+
     |        Nonce (uint32)|    |
     +----------------------+    |
     |         Time (uint32)|    |--[JSON]-->[HASH]
     +----------------------+    |             |
     |  Previous Block Hash |    |             |
     +----------------------+    |             |
     |       Hash_TX0       |    |             |
     ++++++++++++++++++++++++  --+             |
     |          TX0         |  ----------------|------->
     +----------------------+                  |          Transaction Tx0:
                                               |          +----------------------+
                                               |          |        Nonce         |
                                               |          +----------------------+
                                               |          |        Source        |
                                               |          +----------------------+
                                               |          |     Destination      |
                                               |          +----------------------+
BLOCK N+1:                                     |          |        Amount        |
     +----------------------+                  |          +----------------------+
     |        Nonce         |                  |          |       Signature      |
     +----------------------+                  |          +----------------------+
     |         Time         |                  |
     +----------------------+                  |
     |  Previous Block Hash |  <---------------+
     +----------------------+
     |       Hash_TX0       |  
     ++++++++++++++++++++++++  
     |          TX0         |  
     +----------------------+  

```

# Example of a block
```json
{
  "header": {
    "nonce": 1762106678,
    "time": 1605529418,
    "prevhash": "00000007d0005a65f94f1ee2e574326f00efe9619fba9735dfa053defe72f583",
    "txhash": "30e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  },
  "transactions": [
    {
      "nonce": 1526871401,
      "src": "",
      "dst": "68fc76742406347377af7923e68ec877a89ad0c08079aeea65d933aa73309d48bccfdad8c100ff540c905cef8ec45ea3b940f4f4171def91d9ab218e6773c519",
      "amount": 50000000000000,
      "signature": ""
    }
  ]
}
```

# Example Oracle Working
![](oracle/screenshot.png)

# Wireshark Capture Two Oracles Working
![Click HERE](oracle/capture.pcapng)

