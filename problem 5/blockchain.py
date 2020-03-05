import hashlib
import sys
from pprint import pprint
import datetime
from datetime import timedelta


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hashify = str(data) + str(datetime)
        self.hash = self.calc_hash(self.hashify)
        self.next = None

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        d = ''
        d += "Timestamp: " + str(self.timestamp) + "\n"
        d += "Value: " + str(self.data) + "\n"
        d += "Curr_Hash: " + str(self.hash) + "\n"
        d += "Prev_Hash: " + str(self.previous_hash) + "\n"
        return d


class BlockChain:
    def __init__(self):
        self.head = None

    def add_block(self,timestamp, data,):
        if data is None or len(data) == 0:
            print('Cannot add empty block')
            return

        if self.head is None:
            self.head = Block(timestamp, data, 0)
            return

        else:
            node = self.head
            while node.next:
                node = node.next
            previous_hash = node.hash
            node.next = Block(timestamp, data, previous_hash)
            if self.head.timestamp > node.next.timestamp:
                print('Block out of order')
                return
            return


blockchain = BlockChain()
blockchain.add_block(datetime.datetime.now(), 'cat')
blockchain.add_block(datetime.datetime.now(), 'dog')
blockchain.add_block(datetime.datetime.now(), 'duck')
print("Test 1:")
print("Should print block chain:")
print("\n")
print(blockchain.head)
print(blockchain.head.next)
print(blockchain.head.next.next)
print("\n")
print("Test 2:")
print("Should print: 'Cannot add empty block'")
blockchain.add_block(datetime.datetime.now(), '')
print("\n")
print("Test 3:")
print("Should print: " 'Block out of order')
blockchain.add_block(datetime.datetime.now(), "goose")
blockchain.add_block(datetime.datetime.now() - timedelta(minutes=10), "goat")







