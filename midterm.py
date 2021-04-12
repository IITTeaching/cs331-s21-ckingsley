class DoubleLinkedList:
    class Node: ##the equivalent of ListCell
        def __init__(self, val, prior=None, next=None):
            self.val = val
            self.prior = prior
            self.next  = next

    def __init__(self):
        self.count = 0
        self.head = self.Node(None)
        self.head.next = self.head
        self.head.prior = self.head

    def prepend(self, value): # O(1)
        self.count += 1
        newn = self.Node(value, prior = self.head, next = self.head.next)
        self.head.next.prior = newn
        self.head.next = newn


    def append(self, value): # O(1)
        self.count += 1
        newn = self.Node(value, prior = self.head.prior, next = self.head)
        self.head.prior.next = newn
        self.head.prior = newn

    def __getitem__(self, idx): # n = O(n), but we can do it in n/2
        # Write n/2 (first half access though next, second half access through prior)
        assert(idx >= 0 and idx < len(self))
        n = self.head.next
        for i in range(0,idx):
            n = n.next
        return n.val

    def __len__(self):
        return self.count

    def __iter__(self):
        n = self.head.next
        while n is not self.head:
            yield n.val
            n = n.next

    def __repr__(self):
        return '[' + ', '.join(str(x) for x in self) + ']'




def f(l):
    class listiter:
        def __init__(self, l): ##new
            self.lst = l
            self.cur = self.lst.head

        def __iter__(self):
            return self
                    
        def __next__(self):
            self.cur = self.cur.prior
            return self.cur.val

    return listiter(l)

lst = DoubleLinkedList()

#[0, 1, 2]
for i in range(3):
    lst.append(i)

itr = f(lst)

print(next(itr))
print(next(itr))
print(next(itr))






