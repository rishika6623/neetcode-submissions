class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.head, self.tail = None, None
        self.exists = {}


    def get(self, key: int) -> int:

        print("get")
        if key in self.exists:
            deleteNode = self.exists[key]

            if deleteNode != self.tail:
                if deleteNode != self.head:
                    deleteNode.prev.next = deleteNode.next
                elif self.length > 1:
                    self.head = deleteNode.next
                deleteNode.next.prev = deleteNode.prev

                deleteNode.next = None
                deleteNode.prev = self.tail
                self.tail.next = deleteNode
                self.tail = deleteNode

            return self.exists[key].data[1]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        print("put")

        if key in self.exists:
            deleteNode = self.exists[key]

            if deleteNode != self.tail:
                if deleteNode != self.head:
                    deleteNode.prev.next = deleteNode.next
                elif self.length > 1:
                    self.head = deleteNode.next
                deleteNode.next.prev = deleteNode.prev

                deleteNode.next = None
                deleteNode.prev = self.tail
                self.tail.next = deleteNode
                self.tail = deleteNode

            deleteNode.data = (key, value)

        else:
            if self.length == self.capacity:
                oldkey, oldvalue = self.head.data
                del self.exists[oldkey]
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                else:
                    self.tail = None
            else:
                self.length += 1
            
            newNode = Node((key, value))
            if not self.head:
                self.head = newNode
            self.exists[key] = newNode
            newNode.prev = self.tail
            if self.tail:
                self.tail.next = newNode
            self.tail = newNode