import urllib
import urllib.request
from unittest import TestCase



def to_ascii_bytes(words):
    """
    Helper method to condense code. Words --> ascii bytes (returned)
    """
    ascii_words = words.encode('ascii','replace')
    ascii_bytes = ascii_words.split()

    return ascii_bytes 

def max(lst):
    """
    Length of longest element in a given list
    """
    cur_max = 0
    for el in lst:
        if len(el) > cur_max:
            cur_max = len(el)
    return cur_max


def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    """
    Modified version of skelton code provided for project (same 
    functionality.) Takes a url of an online book as a parameter 
    and returns a list of ASCII-based bytes representing all words 
    in the book. 
    """
    booktxt = urllib.request.urlopen(book_url).read().decode()
    return to_ascii_bytes(booktxt)

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    """
    The primary method of the lab. Uses radix sort to return a SORTED
    list of bytes representing all characters in the book.
    """
    bytes = book_to_words()
    return radix_sort(bytes)


def radix_sort(book_bytes):
    """
    Sorts an unsorted list of bytes (the book's bytes) using radix sort
    and returns the sorted list.
    """
    longest = max(book_bytes)
    for i in range(longest):
        book_bytes = queuesToArray(toQueues(book_bytes, i, longest), len(book_bytes))
    return book_bytes

def get_digit(word, k, max_length):
    """
    Gets the numerical ASCII value associated with the character
    at max_length-k position in a byte where max_length is the greatest
    possible length of any "word" parameter.
    If word does not have a character at position max_length-k, "0" is returned.
    Otherwise, the character at said position is returned.
    """
    index = max_length - k - 1
    if index < len(word):
        return word[index]
    else:
        return 0

def toQueues(lst, i, high):
    """
    Calculates the ASCII-based index of each element in lst and then 
    places that element in the corresponding queuefor its ASCII value. 
    Returns queues a list containing all 256 queues.
    """
    queues = [[] for _ in range(256)]
    for elem in lst:
        index = get_digit(elem, i, high)
        queues[index].append(elem)
    return queues

def queuesToArray(queues, num_bytes):
    """
    Converts the 256 queues contained in the queues list into a singular
    array containing all elements from the queues in their original order.
    Uses "j" to guide the insertion of elements from 
    successive queues into "arr."
    """
    arr = [ [] for i in range(num_bytes) ]
    j = 0
    for i in range(len(queues)):
        queue = queues[i]
        while len(queue) > 0:
            arr[j] = queue.pop(0)
            j += 1
    
    return arr


##### TEST CASES ######
def test1():
    arr = [b"Zucchini", b"Zeugma", b"Yam", b"Yu", b"Xtreme", b"Baller", b"Doot", b"Spider", b"Hacc", b"Potato", b"Corn", b"Dublin", b"Daconvertible"]
    python_sorted = sorted(arr)
    radix_sorted = radix_sort(arr)
    
    tc = TestCase()
    tc.assertEqual(python_sorted, radix_sorted)

def test2():
    python_sorted = sorted(book_to_words())
    radix_sorted = radix_a_book()
    
    tc = TestCase()

    tc.assertEqual(python_sorted, radix_sorted)


def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

def main():
    for t in [test1, test2]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()