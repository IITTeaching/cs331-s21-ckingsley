class Stack:
    def __init__(self):
        self.data = []

    def push(self, val): # O(1) -- append is O(1). Prepending would be O(n) because have to shift all the other elements in the array to the right
        self.data.append(val)

        ##AMORTIZED RUNTIME -- it's ok to have a more expensive version of your operation (ex: whenever you have to double the array when appending) if the average runtime is faster. WORST case complexity is O(n) for inserting n elements. According to http://lcm.csa.iisc.ernet.in/dsa/node9.html, amortized runtime is described as such: "Amortized Running Time:  Here the time required to perform a sequence of (related) operations is averaged over all the operations performed. Amortized analysis can be used to show that the average cost of an operation is small, if one averages over a sequence of operations, even though a simple operation might be expensive. Amortized analysis guarantees the average performance of each operation in the worst case.'


    def pop(self):  # O(1) -- deleting at the end is O(1)
        assert not self.empty()
        val = self.data[-1]
        del self.data[-1]
        return val


    def peek(self):
        assert not self.empty()
        return self.data[-1]

    def empty(self):  #a boolean  
        return self.data == []

    def __bool__(self):
        return not self.empty()        

    def __repr__(self):
        return self.data.__repr__()

    def __str__(self):
        return self.__repr__()



def h(s):
    st = Stack()
    for c in s.split(" "):
        if c in '+*':
            lo = st.pop()
            ro = st.pop()
            if c == '+':
                st.push(lo + ro)
            elif c == '*':
                st.push(lo * ro)
        else:
            st.push(int(c))
    return st.pop()


v = h("* * * * *")
print(v)