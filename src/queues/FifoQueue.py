from source.queues.Node import Node


class FifoQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def enqueue(self, payload):
        self._count += 1
        node = Node(payload)
        if self._tail:
            last_node = self._tail
            last_node.next = node
            node.previous = last_node
            self._tail = node
        else:
            self._head = node
            self._tail = node
        return None

    def dequeue(self):
        if not self._head:
            return None
        self._count -= 1
        last_node = self._head
        if not last_node.next:
            self._head = None
            self._tail = None
            return last_node.payload
        next_node = last_node.next
        next_node.previous = None
        self._head = next_node
        last_node.next = None
        return last_node.payload

    def dequeue_multiple(self, amount):
        count = self._count if self._count < amount else amount
        return [self.dequeue() for i in range(count)]

    def count(self):
        return self._count
