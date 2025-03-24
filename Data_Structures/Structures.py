class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):

        if not self.front :
            return None

        removed_data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return removed_data

    def print_queue(self):
        current = self.front
        print("Queue", end="")
        while current:
            print(f" -> {current.data}", end="")
            current = current.next



class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        popped = self.top.data
        self.top = self.top.next

    def top_value(self):
        return self.top.data

    def print_stack(self):
        current = self.top
        while current:
            print(f"-> {current.data}")
            current = current.next



