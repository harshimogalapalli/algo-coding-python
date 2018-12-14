class Stack(list):
   def __init__(self):
       self.items=[]
   def isEmpty(self):
       return self.items==[]
   def isFull(self):
        return self.items>=5
   def push(self,item):
       self.items.append(item)
   def pop(self):
       if not self.isEmpty():
           return self.items.pop()
       else:
           print("STACK IS EMPTY")
def main():
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)

  print(stack.pop())
  print(stack.pop())
  print(stack.pop())
  print(stack.pop())
if __name__ == '__main__':
  main()
