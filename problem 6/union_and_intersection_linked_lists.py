class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    union_list = LinkedList()
    s = set()
    current_1 = llist_1.head
    while current_1:
        s.add(current_1.value)
        current_1 = current_1.next

    current_2 = llist_2.head
    while current_2:
        s.add(current_2.value)
        current_2 = current_2.next

    for num in s:
        union_list.append(num)

    return union_list

def intersection(llist_1, llist_2):
    # Your Solution Her
    intersection_list = []
    s = set()
    current_1 = llist_1.head
    while current_1:
        s.add(current_1.value)
        current_1 = current_1.next

    current_2 = llist_2.head
    while current_2:
        if current_2.value in s:
            intersection_list.append(current_2.value)
            s.remove(current_2.value)

        current_2 = current_2.next

    return intersection_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)
for i in element_2:
    linked_list_2.append(i)


print(union(linked_list_1, linked_list_2))  # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_1, linked_list_2))  # [6, 4, 21]

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))  # 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print(intersection(linked_list_3, linked_list_4))  # no shared values so output = []


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))  # 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_5, linked_list_6))  # []