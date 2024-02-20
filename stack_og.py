class stack:
    def __init__(self):
        self.item = []
        
    def is_emoty(self):
        return len(self.item) == 0
    
    def push(self,item):
        self.item.append(item)

    def delete(self):
        if not self.is_emoty():
            return self.item.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_emoty():
            return self.item[-1]
        else:
            return None
        
    def size(self):
        return len(self.item)
    
stack = stack()

stack.push(3)
stack.push(5)
stack.push(7)
stack.push(9)

print("stack size: ",stack.size())
print("Top item: ",stack.peek())
print("Pop item: ",stack.delete())
print("Stack size after popping: ",stack.size())
