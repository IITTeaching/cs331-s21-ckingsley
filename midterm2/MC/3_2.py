def g(l): # l is a python list of integers of length n
       pairs = [ (i,j) for i in range(len(l)) for j in range(len(l)) if i < j ]
       result = []
       for (i,j) in pairs:
           if l[i] == l[j]:
              result.append((i,j))
       return result





#pairs = [ (i,j) for i in range(3) for j in range(3) ]
#print(pairs)