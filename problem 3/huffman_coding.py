# Here is one type of pseudocode for this coding schema:
#
# Take a string and determine the relevant frequencies of the characters.
# Build and sort a list of tuples from lowest to highest frequencies.
# Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
# Trim the Huffman Tree (remove the frequencies from the previously built tree).
# Encode the text into its compressed form.
# Decode the text from its compressed form.
# You then will need to create encoding, decoding, and sizing schemas.

import sys

class Node(object):
    def __init__(self, letter=None, freq=None, left_child=None, right_child=None):
        self.letter = letter
        self.freq = freq
        self.left_child = left_child
        self.right_child = right_child
        self.code = ''

class Tree:
    def __init__(self, node, single):
        self.root = node
        self.single = single
        self.codes = {}

    def create_binary(self, node):

        # check data is not single character, if yes binary = 0
        if self.single:
            node.code = '0'
            self.codes[node.letter] = node.code
            return

        # check if node contains left child, if yes binary code string + 0
        if node.left_child is not None:
            node.left_child.code = node.code + '0'
            self.create_binary(node.left_child)

        # check if node contains right child if yes binary code string + 1
        if node.right_child is not None:
            node.right_child.code = node.code + '1'
            self.create_binary(node.right_child)

        # if not single , left child , or right child binary code complete output {letter : binary code}
        if node.letter is not None and node.letter != '':
            self.codes[node.letter] = node.code


class PriorityQueue:

    # create queue and set length param to 0
    def __init__(self):
        self.queue = []
        self.length = 0

    # add the node to the queue increase length by 1
    def put(self, node):
        self.queue.append(node)
        self.length += 1

    # find least frequently used node, loop over the queue by index if the given node freq is less then the first
    # node in the queue set lfu to node value of that index once lfu found decrease len of queue by 1 and remove node
    # from priority queue
    def pop_lfu(self):
        lfu = self.queue[0]
        index = 0
        for i in range(self.length):
            if self.queue[i].freq < lfu.freq:
                lfu = self.queue[i]
                index = i

        self.length -= 1
        del self.queue[index]
        return lfu


def huffman_encoding(data):

    # ensure that data is a str, if no then return a none value
    if not isinstance(data, str) or len(data) == 0:
        return None, None

    # initialize a dict, loop over the letters in the provided data if letter is in the dict add 1 to the freq if not
    # yet in f set value to 1
    f = {}
    for letter in data:
        if letter in f:
            f[letter] += 1
        else:
            f[letter] = 1

    # set PriorityQueue class to priority_queue variable
    priority_queue = PriorityQueue()

    # loop over the letters in the frequency dict, create node objects with initialized values and add these nodes to
    # the priority queue
    for letter in f:
        node = Node(letter, f[letter])
        priority_queue.put(node)

    # while there're still nodes in the queue get the least frequently used (lfu) node and set it to a node variable
    # to be combined with the next lfu node in the queue if one exists. This creates a parent node with the freq equal
    # to the freq of the lfu_1 and lfu_2 combined and puts that combined node value back into the queue for further
    # iteration
    while priority_queue.length > 1:
        node_1 = priority_queue.pop_lfu()
        node_2 = priority_queue.pop_lfu()
        parent_node_freq = node_1.freq + node_2.freq
        parent_node = Node("", parent_node_freq, node_1, node_2)
        priority_queue.put(parent_node)

    # root is updated to first value in priority queue as it is now the first value in the huffman tree, check if length
    # of data is a single character or multiple if single add True value so iteration stops in decode action
    root = priority_queue.queue[0]
    if data == len(data) * data[0]:
        single = True
    else:
        single = False

    # create the binary tree, passing in the root and single boolean value if single True binary tree value will be set
    # to 0, else create the binary tree starting with the root node, setting the codes variable to the binary codes of
    # the branches
    binary_tree = Tree(root, single)
    binary_tree.create_binary(root)
    codes = binary_tree.codes

    # added codes to string return the string of binary data along with the binary tree
    encoded = ''
    for letter in data:
        encoded += codes[letter]

    return encoded, binary_tree


def huffman_decoding(encoded, tree):

    decoded = ''
    root = tree.root
    node = root
    index = 0

    # check if tree is only a single character if so return it
    if tree.single:
        decoded = root.letter * root.freq
        return decoded

    # while the index is not equal to the length of the encoded string, go through the endcoded data if the code is 0
    # traverse left, if node is 1 traverse right adding one to the index each iteration until left and right are none
    # once none add the letter of that last node to the decoded string
    while index != len(encoded):
        if encoded[index] == '0':
            node = node.left_child
        elif encoded[index] == '1':
            node = node.right_child
        if node.left_child is None and node.right_child is None:
            decoded += node.letter
            node = root
        index += 1

    return decoded


def testing(data):
    encoded, tree = huffman_encoding(data)

    if encoded is not None:
        print("------------------------------------------------------------")
        print("The size of the data is: {}\n".format(sys.getsizeof(data)))
        print("The content of the data is: {}\n".format(data))

        encoded, tree = huffman_encoding(data)

        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded))

        decoded = huffman_decoding(encoded, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded)))
        print("The content of the encoded data is: {}\n".format(decoded))


testing(1)  # return none
testing('')  # return none
testing('Z')  # original size: 50, content: Z, compressed size: 24, binary: 0, decoded size: 50, decoded content: Z
testing('ZZ')  # original size: 51, content: ZZ, compressed size: 24, binary: 00, decoded size: 51, decoded content: ZZ
testing("The bird is the word")  # original size: 69, content: The bird is the word, compressed size: 36,
                                 # binary: 0110111011111100111000001010110000100011010011110111111010101011001010
                                 # decoded size: 69, decoded content: The bird is the word

