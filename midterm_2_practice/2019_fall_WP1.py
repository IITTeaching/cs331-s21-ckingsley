##BASE IMPLEMENTATION
class Stack:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.top = None

    def push(self, val):
        self.top = Stack.Node(val, self.top)

    def pop(self):
        val = self.top.val
        self.top = self.top.next
        return val

    def print(self):
        arr = []
        cur = self.top
        while cur:
            arr.append(cur.val)
            cur = cur.next 
        print(arr)

    ##//BASE IMPLEMENTATION
    
    def remove_all(self, num):
        #removes any values of num that are DIRECTLY at the top, e.g. num = 1, [1,1,1,1,2,3,4] becomes [2,3,4]
        while self.top:
            if self.top.val == num:
                self.top = self.top.next
            else:
                break
        

        
        if self.top:
            cur = self.top
            while cur.next:
                if cur.next.val == num:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
    
    
s = Stack()
arr = [1, 1, 1, 1, 1, 2, 3, 4, 5, 6]
for i in arr:
    s.push(i)

s.remove_all(1)

s.print()

     