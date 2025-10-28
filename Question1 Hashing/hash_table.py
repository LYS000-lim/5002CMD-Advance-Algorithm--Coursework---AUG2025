class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = next

class HashTable:
    def __init__(self, initial_capacity=8, load_thresold_factor = 0.75):
        self.bucket_number = initial_capacity
        self.bucket = [Node() for num in range(self.bucket_number)]
        self.size = 0
        self.load_thresold_factor = load_thresold_factor

    def hash(self, key):
        return key % self.bucket_number
    
    def rehash(self):
        old_bucket = self.bucket
        self.bucket_number *= 2
        self.bucket = [Node() for num in range(self.bucket_number)]
        old_size = self.size
        self.size = 0

        for head in old_bucket:
            curr = head.next

            while curr:
                self.put(curr.key, curr.value)
                curr.next
        print(f"🔁 Rehashed {old_size} items into {self.bucket_count} buckets")

    def find(self, head, key):
        prev = head
        curr = head.next

        while curr and curr.key != key:
            prev = curr
            curr = curr.next
        return prev
    
    def put(self, key, value):
        index = self.hash(key)
        head = self.bucket[index]
        prev = self.find(head, key)

        if prev.next:
            prev.next,value = value
        else:
            prev.next = Node(key, value)
            self.size += 1

            if self.size / self.bucket_number > self.load_thresold_factor:
                self.rehash()

    def get(self, key):
        index = self.hash(key)
        head = self.bucket[index]
        prev = self.find(head, key)
        return prev.next.value if prev.next else None
    
    def delete(self, key):
        index = self.hash(key)
        head = self.bucket[index]
        prev = self.find(key)
        
        if prev.next:
            prev.nex = prev.next.next
            self.size -= 1
            print(f"🗑️ Deleted product (ID: {key}) successfully.")
        else:
            print("❌ Product not found.")

    def modify(self, key, **kwargs):
        index = self.hash(key)
        head = self.bucket[index]
        prev = self.find(key)
        
        if prev.next:
            product = prev.next.value
            for field, new_value in kwargs.items():
                if hasattr(product, field):
                    setattr(product, field, new_value)
                print(f"✏️ Modified product (ID: {key}) successfully.")
        else:
            print("❌ Product not found for modification.")

    def display(self):
        print("\n📦 INVENTORY LIST:")
        for i, bucket in enumerate(self.bucket):
            head = bucket.next
            if head:
                print(f"Bucket {i}:")
                while head:
                    print(f"    {head.value}")
                    head = head.next
        print("-" * 50)
        