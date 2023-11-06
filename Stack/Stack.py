class Stack:
    """
    Stack Implementation
    """
    def __init__(self):
        """
        Initialize empty stack
        """
        self.items = []

    def push(self,item):
        """
        add data to the stack
        """
        self.items.append(item)

    def pop(self):
        """
        remove data from the back of stack
        """
        if not self.is_empty():
            "it stack isnt empty then remove data at the end of stack"
            return self.items.pop()
        else:
            return 'Stack is empty'
    def is_empty(self):
        """
        Checking if the stack is empty and return boolean value
        """
        return len(self.items) == 0

    def get_stack(self):
        """
        Get all the items of the stack
        """
        return self.items

    def peek(self):
        """
        See the last item of the stack
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            return 'Stack is empty'

if __name__=='__main__':
    stack = Stack()
    stack.push('A')
    stack.push('B')
    print(stack.pop())
    stack.push('C')
    print(stack.peek())
    print(stack.get_stack())