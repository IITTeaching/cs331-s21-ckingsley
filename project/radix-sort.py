import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    arr = book_to_words(book_url)
    

    
    def countVal(element, digit):
        """
        returns a number [0, 129] inclusive. 0 if the element (ex: b"cow")
        does not have a character at digit (called a "short"). 
        Otherwise returns 1 + the ASCII value of the character at the digit.

        The returned value serves the index in the count array for "element".
        """
        try:
            ascVal = element[digit]
            return ascVal + 1
        except: #short encountered!
            return 0
    
    #low and high are indecies. if [a, ab] is to be sorted and is at the front of arr, (low, high) = (0, 2)
    def rec_count_sort(arr, low, high, digit):
        if (high - low) == 1:
            pass

        else:

            count = [0] * 129 ##128 ASCII + first spot for shorts
            
            for i in range(low, high):
                word = arr[i]
                index = countVal(word, digit)
                count[index] += 1


            ######################################## -->
            groups = []
            g_low = -1
            g_high = -1
                
            for i in range(len(count)):
                if count[i] != 0:
                    if g_low == -1:    
                        g_low = None
                        g_high = i
                        groups.append((g_low, g_high))
                        g_low = i
                        g_high = -1
                    elif g_low != -1:
                        g_high = i
                        groups.append((g_low, g_high))
                        g_low = i
                        g_high = -1

            if g_low != -1 and g_high == - 1:
                groups.append((g_low,None))
            ########################################## //



            
            for i in range(1, len(count)): #update count - each position of count sums itself and all other positions earlier in count
                count[i] += count[i-1]


            ######################################## -->
            for i in range(len(groups)):
                lh = groups[i]
                old_low = lh[0]
                old_high = lh[1]

                if old_low == None:
                    new_low = low
                else:
                    new_low = count[old_low]
    
                if old_high == None:
                    new_high = high
                else:
                    new_high = count[old_high]

                

                new_lh = (new_low, new_high)

                groups[i] = new_lh
            ########################################## //
                
            new_arr = [None] * (high-low)
            for i in range(low, high):
                
                word = arr[i]
                c_index = countVal(word, digit)
                arr_index = count[c_index] + low
                
                ### update count -->
                count[c_index] -= 1
                ### //

                new_arr[arr_index - 1] = arr[i]
            
            for i in range(low, high):
                arr[i] = new_arr[i-low]

            for group in groups:
                low = group[0]
                high = group[1]
                rec_count_sort(arr, low, high, digit + 1)
    
    
    low = 0
    high = len(arr)
    digit = 0
    rec_count_sort(arr, low, high, digit)

    return arr
        



        

radix_a_book()


    