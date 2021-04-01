if '{' in '{([<':
    print('True')



def is_full(self):
        print(self.tail)
        print(self.head)
        if self.head == -1 and self.tail == -1:
            return False

        else:
            for elem in self.data:
                if elem == None:
                    return False    
            return True