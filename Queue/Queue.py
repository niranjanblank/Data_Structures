class Queue:
    """
    Queue Implementation
    """

    def __init__(self):
        """ initializing empty queue """
        self.items = []

    def enqueue(self, item):
        """ adding items to the queue"""
        self.items.append(item)

    def dequeue(self):
        """ remove item from the queue and return it"""
        item = self.items.pop(0)
        return item

    def is_empty(self):
        """ check if the queue is empty"""
        return len(self.items) == 0

    def get_queue(self):
        """ get all the items in the queue """
        return self.items

    def size(self):
        """ get the size of queue """
        return len(self.items)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('Max')
    queue.enqueue('Lewis')
    queue.enqueue('Lando')
    queue.enqueue('Perez')
    print(f'Items in Queue: {queue.get_queue()}')
    print(f"{queue.dequeue()} removed from the queue")
    print(f"{queue.dequeue()} removed from the queue")
    print(queue.get_queue())
