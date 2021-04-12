#class Heap:
#    def __init__(self, key=lambda x:x):
#        self.data = []
#        self.key  = key

#    def test(self):
#        print(self.key(0))
    
#h = Heap(lambda x:x+2)
#h.test()



def running_medians_naive(iterable):
    values = []
    medians = []
    for i, x in iterable:
        values.append(x)
        values.sort()
        if i%2 == 0:
            medians.append(values[i//2])
        else:
            medians.append((values[i//2] + values[i//2+1]) / 2)
    return medians

#print(running_medians_naive([3, 1, 9, 25, 12]))

doot = enumerate([8, 4, 11, 18])

print(running_medians_naive([8, 4, 11, 18]))

