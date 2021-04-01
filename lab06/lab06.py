from unittest import TestCase


################################################################################
# STACK IMPLEMENTATION (DO NOT MODIFY THIS CODE)
################################################################################
class Stack:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next  = next

    def __init__(self):
        self.top = None

    def push(self, val):
        self.top = Stack.Node(val, self.top)

    def pop(self):
        assert self.top, 'Stack is empty'
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.val if self.top else None

    def empty(self):
        return self.top == None

    def __bool__(self):
        return not self.empty()

    def __repr__(self):
        if not self.top:
            return ''
        return '--> ' + ', '.join(str(x) for x in self)

    def __iter__(self):
        n = self.top
        while n:
            yield n.val
            n = n.next

################################################################################
# CHECK DELIMITERS
################################################################################
def check_delimiters(expr):
    """Returns True if and only if `expr` contains only correctly matched delimiters, else returns False."""
    delim_openers = '{([<'
    delim_closers = '})]>'

    ### BEGIN SOLUTION
   
    s = Stack()
    for c in expr:
        if c in delim_openers:
            s.push(c)
        if c in delim_closers:
            if s.empty():
                return False
            else: #basically i am checking if the character "c" (which is a closing delimiter, by the way) is the pair of the delimiter being popped off the stack. So if c is "[" and popped is "]" then nothing happens (and we proceed.) However if c is "[" and p is ")" then we return False. 
                popped = s.pop()
                cindex = delim_closers.find(c)
                pindex = delim_openers.find(popped)
                if cindex != pindex:
                    return False
    return s.empty()
    ### END SOLUTION

################################################################################
# CHECK DELIMITERS - TEST CASES
################################################################################
# points: 5
def test_check_delimiters_1():
    tc = TestCase()
    tc.assertTrue(check_delimiters('()'))
    tc.assertTrue(check_delimiters('[]'))
    tc.assertTrue(check_delimiters('{}'))
    tc.assertTrue(check_delimiters('<>'))

# points:5
def test_check_delimiters_2():
    tc = TestCase()
    tc.assertTrue(check_delimiters('([])'))
    tc.assertTrue(check_delimiters('[{}]'))
    tc.assertTrue(check_delimiters('{<()>}'))
    tc.assertTrue(check_delimiters('<({[]})>'))

# points: 5
def test_check_delimiters_3():
    tc = TestCase()
    tc.assertTrue(check_delimiters('([] () <> [])'))
    tc.assertTrue(check_delimiters('[{()} [] (<> <>) {}]'))
    tc.assertTrue(check_delimiters('{} <> () []'))
    tc.assertTrue(check_delimiters('<> ([] <()>) <[] [] <> <>>'))

# points: 5
def test_check_delimiters_4():
    tc = TestCase()
    tc.assertFalse(check_delimiters('('))
    tc.assertFalse(check_delimiters('['))
    tc.assertFalse(check_delimiters('{'))
    tc.assertFalse(check_delimiters('<'))
    tc.assertFalse(check_delimiters(')'))
    tc.assertFalse(check_delimiters(']'))
    tc.assertFalse(check_delimiters('}'))
    tc.assertFalse(check_delimiters('>'))

# points: 5
def test_check_delimiters_5():
    tc = TestCase()
    tc.assertFalse(check_delimiters('( ]'))
    tc.assertFalse(check_delimiters('[ )'))
    tc.assertFalse(check_delimiters('{ >'))
    tc.assertFalse(check_delimiters('< )'))

# points: 5
def test_check_delimiters_6():
    tc = TestCase()
    tc.assertFalse(check_delimiters('[ ( ] )'))
    tc.assertFalse(check_delimiters('((((((( ))))))'))
    tc.assertFalse(check_delimiters('< < > > >'))
    tc.assertFalse(check_delimiters('( [] < {} )'))

################################################################################
# INFIX -> POSTFIX CONVERSION
################################################################################

def infix_to_postfix(expr):
    """Returns the postfix form of the infix expression found in `expr`"""
    # you may find the following precedence dictionary useful
    prec = {'*': 2, '/': 2,
            '+': 1, '-': 1}
    ops = Stack()
    postfix = []
    toks = expr.split()
    ### BEGIN SOLUTION
    def is_int(c):
        try:
            i = int(c)
        except ValueError:
            return False
        return True
    
    def is_parens(c):
        return c in '()'

    def is_op(c):
        return c in '+-*/'
    

    for c in toks:
        if is_int(c):
            postfix.append(c)

        elif is_parens(c):
            if c == '(':
                ops.push(c)
            elif c == ')':
                for elem in ops:
                    if elem == '(':
                        break
                    else:
                        postfix.append(elem)
                        ops.pop()
                ##now, the final remaining element in 'ops' should be '(', and I remove it from the stack.
                ops.pop()

        elif is_op(c):
            if ops.empty():
                ops.push(c)
            else:
                #compare precenedence between top of "ops" stack and "c"
                if ops.peek() != '(' and prec[c] <= prec[ops.peek()]:
                    for elem in ops:
                        if elem == '(' or prec[elem] < prec[c]:
                            break
                        else:
                            postfix.append(elem)
                            ops.pop()
                
                ops.push(c)
                
    for elem in ops:
        if not is_parens(elem):
            postfix.append(elem)

    ### END SOLUTION
    return ' '.join(postfix)

################################################################################
# INFIX -> POSTFIX CONVERSION - TEST CASES
################################################################################

# points: 10
def test_infix_to_postfix_1():
    tc = TestCase()
    tc.assertEqual(infix_to_postfix('1'), '1')
    tc.assertEqual(infix_to_postfix('1 + 2'), '1 2 +')
    tc.assertEqual(infix_to_postfix('( 1 + 2 )'), '1 2 +')
    tc.assertEqual(infix_to_postfix('1 + 2 - 3'), '1 2 + 3 -')
    tc.assertEqual(infix_to_postfix('1 + ( 2 - 3 )'), '1 2 3 - +')

# points: 10
def test_infix_to_postfix_2():
    tc = TestCase()
    tc.assertEqual(infix_to_postfix('1 + 2 * 3'), '1 2 3 * +')
    tc.assertEqual(infix_to_postfix('1 / 2 + 3 * 4'), '1 2 / 3 4 * +')
    tc.assertEqual(infix_to_postfix('1 * 2 * 3 + 4'), '1 2 * 3 * 4 +')
    tc.assertEqual(infix_to_postfix('1 + 2 * 3 * 4'), '1 2 3 * 4 * +')

# points: 10
def test_infix_to_postfix_3():
    tc = TestCase()
    tc.assertEqual(infix_to_postfix('1 * ( 2 + 3 ) * 4'), '1 2 3 + * 4 *')
    tc.assertEqual(infix_to_postfix('1 * ( 2 + 3 * 4 ) + 5'), '1 2 3 4 * + * 5 +')
    tc.assertEqual(infix_to_postfix('1 * ( ( 2 + 3 ) * 4 ) * ( 5 - 6 )'), '1 2 3 + 4 * * 5 6 - *')

################################################################################
# QUEUE IMPLEMENTATION
################################################################################
class Queue:
    def __init__(self, limit=10):
        self.len = limit
        self.data = [None] * limit
        self.head = -1
        self.tail = -1

    def enqueue(self, val):
        if (self.tail + 1) % self.len == self.head:
            raise RuntimeError
        elif self.head == -1:
            self.head = self.tail = 0
            self.data[self.tail] = val
        else:
            self.tail = (self.tail + 1) % self.len
            self.data[self.tail] = val

    def dequeue(self):
        if self.head == -1:
            raise RuntimeError
        elif self.head == self.tail:
            temp = self.data[self.head]
            self.data[self.head] = None
            self.head = self.tail = -1
            return temp
        else:
            temp = self.data[self.head]
            self.data[self.head] = None
            self.head = (self.head + 1) % self.len
            return temp

    def resize(self, newsize):
        assert(newsize > len(self.data))
        newarray = [None]
        for x in range(newsize-1):
            newarray.append([None])

        for i in range(self.len):
            newarray[i] = self.dequeue()
        
        self.data = newarray
        
        self.head = 0
        self.tail = self.len-1


        self.len = newsize

    def empty(self):
        for i in range(self.len):
            if self.data[i] != None:
                return False

        return True

    def __bool__(self):
        return not self.empty()

    def __str__(self):
        if not(self):
            return ''
        return ', '.join(str(el) for el in self)

    def __repr__(self):
        return str(self)

    def __iter__(self):
        for i in range(self.head, self.tail+1):
            yield self.data[i]


################################################################################
# QUEUE IMPLEMENTATION - TEST CASES
################################################################################

# points: 13
def test_queue_implementation_1():
    tc = TestCase()

    q = Queue(5)
    tc.assertEqual(q.data, [None] * 5)

   # print('got here')
    
    for i in range(5):
        #print(f' started {i}')
        q.enqueue(i)
       # print(f' finished {i} ')
    
    #print('f')
    
   
    

    with tc.assertRaises(RuntimeError): 
        q.enqueue(5)

    
    
    #print(f'q after enqueuing: {[ elem for elem in q.data ]}')
   # print(f'tail: {q.tail}')

    for i in range(5):
        #print(f'q: {[ elem for elem in q.data ]}')
        #print(f' being dequeued: {q.data[q.head + 1]}, i: {i}')
        tc.assertEqual(q.dequeue(), i)
        #print(f' finished {i}')

    #print(f'tail: {q.tail}, head: {q.head}')
    tc.assertTrue(q.empty())

# points: 13
def test_queue_implementation_2():
    tc = TestCase()

    q = Queue(10)

    for i in range(6):
        q.enqueue(i)

    tc.assertEqual(q.data.count(None), 4)

    for i in range(5):
        q.dequeue()

    tc.assertFalse(q.empty())
    tc.assertEqual(q.data.count(None), 9)
    tc.assertEqual(q.head, q.tail)
    tc.assertEqual(q.head, 5)

    for i in range(9):
        q.enqueue(i)

    with tc.assertRaises(RuntimeError):
        q.enqueue(10)

    for x, y in zip(q, [5] + list(range(9))):
        tc.assertEqual(x, y)

    tc.assertEqual(q.dequeue(), 5)
    for i in range(9):
        tc.assertEqual(q.dequeue(), i)

    tc.assertTrue(q.empty())

# points: 14
def test_queue_implementation_3():
	tc = TestCase()

	q = Queue(5)
	for i in range(5):
	    q.enqueue(i)
	for i in range(4):
	    q.dequeue()
	for i in range(5, 9):
	    q.enqueue(i)

	with tc.assertRaises(RuntimeError):
	    q.enqueue(10)

	q.resize(10)

	for x, y in zip(q, range(4, 9)):
	    tc.assertEqual(x, y)

	for i in range(9, 14):
	    q.enqueue(i)

	for i in range(4, 14):
	    tc.assertEqual(q.dequeue(), i)

	tc.assertTrue(q.empty())
	tc.assertEqual(q.head, -1)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "*" + "\n" + f.__name__)

def say_success():
    print("SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_check_delimiters_1,
              test_check_delimiters_2,
              test_check_delimiters_3,
              test_check_delimiters_4,
              test_check_delimiters_5,
              test_check_delimiters_6,
              test_infix_to_postfix_1,
              test_infix_to_postfix_2,
              test_infix_to_postfix_3,
              test_queue_implementation_1,
              test_queue_implementation_2,
              test_queue_implementation_3]:
        say_test(t)
        t()
        say_success()


if __name__ == '__main__':
    main()
