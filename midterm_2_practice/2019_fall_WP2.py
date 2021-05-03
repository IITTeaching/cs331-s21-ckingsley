class Hashtable:
    class Node:
        def __init__(self, key, val, next=None):
            self.key = key
            self.val = val
            self.next = next
    
    def __init__(self, n_buckets=1000):
        self.buckets = [None] * n_buckets

    def __setitem__(self, key, val):
        bucket_idx = hash(key) % len(self.buckets)
        b = self.buckets[bucket_idx]
        while b:
            if b.key == key:
                b.val = val
                return
            b = b.next
        else:
            n = Hashtable.Node(key, val, next=self.buckets[bucket_idx])
            self.buckets[bucket_idx] = n

    def print(self):
        arr = []
        for x in self.buckets:
            arr.append(x.val)

        print(arr)

    def collision_ratio(self):
        collisions = 0
        filled = 0
        for b in self.buckets: 
            if b:
                filled += 1 
                if b.next: 
                    collisions += 1
        
        return collisions/filled



h = Hashtable(2)
h['one'] = 1
h['two'] = 2
h['two'] = 24

print(str(h.collision_ratio()))