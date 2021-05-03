def char_freq(s): # s is a string of length n
       # BEGIN SOLUTION
        d = {}
        for c in s:
            try:
                d[c] = d[c] + 1
            except KeyError:
                d[c] = 1
        
        print(d)
       # END SOLUTION


char_freq("hello")