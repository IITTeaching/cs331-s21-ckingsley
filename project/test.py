"""
import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    arr = [b'cat',b'dog',b'car',b'darn', b'ale']
    
    def countIndex(element, digit):
        
        returns ascii value for the character at the given digit of element
        
        try:
            return element[digit]
        except: #short encountered! Treat this as a "null" ascii character (ascii value of 0)
            return 0
    
    #low and high are indecies. if [a, ab] is to be sorted and is at the front of arr, (low, high) = (0, 2)
    def rec_count_sort(arr, low, high, digit):
        sub_arr = arr[low:high]

        #create 128-indexed ASCII count array
        count = [0] * 128
        for i in range(len(sub_arr)):
            count[countIndex(sub_arr[i], digit)] += 1

        
        no_char_at_digit = count[0]
        if len(sub_arr) > no_char_at_digit: #otherwise the digit is not present in any of the words

            #create barriers array indicating each indecy in the array where the character at digit changes
            #also update count so each position in count holds total number of characters of that ASCII val or less
            barriers = []

            for i in range(len(count)): 
                temp = count[i]    
                count[i] += count[i-1]

                if temp > 0:
                    barriers.append(count[i])
                
            
            #update arr
            old_arr = arr[low:high]
            for i in range(low, high):
                n = countIndex(old_arr[i-low], digit)

                count[n] -= 1
                arr_index = count[n]

                arr[arr_index] = old_arr[i-low]
            
            #recursion
            for i in range(len(barriers)-1):
                low = barriers[i]
                high = barriers[i+1]
                if high - low > 1:
                    rec_count_sort(arr, low, high, digit + 1)

    rec_count_sort(arr, low = 0, high = len(arr), digit = 0)

    return arr
        
##TEST
arr = radix_a_book()

print(arr)


    """

b=False
if []:
    b = True

print(b)