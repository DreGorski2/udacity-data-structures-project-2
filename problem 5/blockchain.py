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


class BlockNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class BlockChain:
    def __init__(self):
        self.head = None

    def add_block(self, data):

        if data is None or len(data) == 0:
            print("Cannot add empty block")
            return

        if self.head is None:
            self.head = BlockNode(data)
            return

        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = BlockNode(data)

    def __repr__(self):
        node = self.head
        blockchain = []
        while node is not None:
            blockchain.append(node.data)
            node = node.next

        return "["+"<-->".join(blockchain) + "]"


blockchain = BlockChain()
blockchain.add_block('cat')
blockchain.add_block('dog')
blockchain.add_block('duck')
print("Test 1:")
print("Should print block chain:")
pprint(blockchain)
print("\n")
print("Test 2:")
print("Should print: 'Cannot add empty block'")
blockchain.add_block('')
print("\n")
print("Test 3:")
print("Should print: 'Cannot add empty block'")
blockchain = BlockChain()
blockchain.add_block(None)



