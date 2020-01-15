import hashlib
import sys
from datetime import datetime


class Block:

    def __init__(self, temp,  timestamp, data, previous_hash):
        self.temp = temp
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


def create_block(prev_block):
    if prev_block is None:
        return None
    temp_now = prev_block.temp + 1
    timestamp_now = datetime.now()
    data_now = f"cat{temp_now}"
    prev_hash_now = prev_block.hash
    return Block(temp_now, timestamp_now, data_now, prev_hash_now)


if __name__ == '__main__':
    try:
        block_chain = [Block(0, datetime.now, 'cat', 0)]
    except TypeError as e:
        sys.exit(e)
    print("Data: " + block_chain[0].data + str(block_chain[0].temp) + "\n" + "Hash: " + block_chain[0].hash
          + "\n" + "Prev Hash: "+ str(block_chain[0].previous_hash) + "\n")
    for i in range(0, 5):
        block = create_block(block_chain[-1])
        if block is not None:
            block_chain.append(block)
        if len(block_chain) != 0:
            print("Data: " + block.data + "\n" + "Hash: " + block.hash + "\n" + "Prev Hash: " + block.previous_hash+"\n")
        else:
            print('end of chain')
