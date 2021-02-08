import time
import unittest
import sys
from contextlib import contextmanager
from io import StringIO

#################################################################################
# TESTING OUTPUTS
#################################################################################
@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

#################################################################################
# EXERCISE 3
#################################################################################
def integer_right_triangles(p):
    num = 0
    sidesfound = []
    for a in range(1, int(p/2)):
        b = ((p/2)-a)/(1-(a/p))
        if(b - int(b) < .00000001):
            if(a in sidesfound):
                pass
            else:
                sidesfound.append(b)
                num += 1
    return num

def test3():
    start_time = time.time()
    tc = unittest.TestCase()
    tc.assertEqual(integer_right_triangles(60), 2)
    tc.assertEqual(integer_right_triangles(100), 0)
    tc.assertEqual(integer_right_triangles(180), 3)
    print("Process finished --- %s seconds ---" % (time.time() - start_time))

##test3()


def gen_pattern(chars): 
    sofar = list()
    length = 4*len(chars) - 3
    reverse = list(chars[::-1])
    for i in range(len(reverse)):
        letters = reverse[i]
        for j in range(i-1, -1, -1):
            letters = reverse[j] + letters + reverse[j]
        line = ".".join(letters).center(length, ".")
        print(line)
        if(i!=len(reverse)-1):
            sofar.append(line)
    for st in sofar[::-1]:
        print(st)
    
        
print("test one: ")
print("\n")
gen_pattern('X')
print("test two: ")
print("\n")
gen_pattern('XY')
print("test three: ")
print("\n")
gen_pattern('WXYZ')
