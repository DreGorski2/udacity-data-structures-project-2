import hashlib
import sys
from pprint import pprint
import datetime


class Block:

    def __init__(self, data, previous_hash=0):
        self.timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S %m-%d-%y")
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        d = ''
        d += "Timestamp: " + self.timestamp + "\n"
        d += "Value: " + self.data + "\n"
        d += "Curr_Hash: " + str(self.hash) + "\n"
        d += "Prev_Hash: " + str(self.previous_hash) + "\n"
        return d


class BlockChain:
    def __init__(self):
        self.blockchain = []
        self.length = 0

    def add_block(self, data=None):
        if not data:
            print("Cannot add empty block")
            return

        elif self.length == 0:
            block = Block(data, 0)

        else:
            block = Block(data, self.blockchain[self.length - 1].hash)

        self.blockchain.append(block)
        self.length += 1

    def __repr__(self):

        if len(self.blockchain) == 0:
            return "Blockchain is empty"

        d = ''
        for i in range(len(self.blockchain)):
            d += "Block " + str(i) + ":" + "\n"
            d += str(self.blockchain[i]) + "\n"
        return d



blockchain = BlockChain()
blockchain.add_block('cat')
blockchain.add_block('dog')
blockchain.add_block('duck')
print("Test 1:")
print("Should print block chain:")
pprint(blockchain)
print("Test 2:")
print("Should print: 'Cannot add empty block'")
blockchain.add_block('')
print("\n")
print("Test 3:")
print("Should print: 'Blockchain is empty'")
blockchain = BlockChain()
print(blockchain)



