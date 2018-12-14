import sys
import stack
def reverse_string_with_stack(str1):
   s = stack.Stack()
   revStr = ''
   for c in str1:
     s.push(c)
   while not s.isEmpty():
     revStr += s.pop()
   print(revStr)  
   
  
if __name__ == '__main__':
    str1 = "python is the best language"
    reverse_string_with_stack(str1)
