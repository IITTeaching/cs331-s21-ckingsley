class Hashtable:
    def __init__(self, n_buckets):
        self.buckets = [[]] * n_buckets #list at each bucket

    def __setitem__(self, key, val):
        h = hash(key)
        bucket = self.buckets[h % len(self.buckets)]
        for k in bucket:
             if(k[0] == key): 
                 k[1] = val #override the existing value, see Notion notes
        bucket.append([key,val])

    def __getitem__(self, key):
        h = hash(key)
        for k in self.buckets[h % len(self.buckets)]:
            if(k[0] == key):
                 return k[1]
        raise Exception(f"key {key} not in hashtable")

    def __contains__(self, key):
        try:
            _ = self[key]

            return True
        except:
            return False


ht = Hashtable(10)
ht['spiderman'] = 'peter parker'
ht['batman'] = 'bruce wayne'
ht['superman'] = 'clark kent'


ht['superman'] = 'bob'
ht['superman']