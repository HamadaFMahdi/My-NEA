print("Hello World!")

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def __len__(self):
        return len(self.stack)
    
    def __iter__(self):
        return self.stack.__iter__()
    
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None

    def __len__(self):
        return len(self.queue)