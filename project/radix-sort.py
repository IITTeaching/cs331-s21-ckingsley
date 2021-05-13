import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    arr = book_to_words(book_url)
    #arr = [b"clean", b"car", b"house", b"darl", b"apple", b"new", b"dee", b"eat"]
    
    def rec_sort(arr, digit):
        asciis = []
        for i in range(128):
            asciis.append([])

        digit_valid = False
        for i in range(len(arr)):
            try:
                ascii_digit = arr[i][digit]
                val = arr[i]
                asciis[ascii_digit].append(val)
                digit_valid = True
            except:
                pass

        if digit_valid:
            asciis_clean = []
            for lst in asciis:
                if lst:
                    asciis_clean.append(lst)

            for i in range(len(asciis_clean)):
                if len(asciis_clean[i]) > 1:
                    asciis_clean[i] = rec_sort(asciis_clean[i], digit + 1)

            return asciis_clean
        
    nested_arr = rec_sort(arr = arr, digit = 0)

    def rec_flatten(nested_lst):
        flat_lst = []
        for elem in  nested_lst:
            if isinstance(elem, list):
                flat_lst.extend(rec_flatten(elem))
            else:
                flat_lst.append(elem)    
        return flat_lst

    return rec_flatten(nested_arr)
    
##test
print(radix_a_book())


    