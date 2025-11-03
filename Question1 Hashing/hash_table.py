class Node:
    """Node class for linked list chaining inside hash table."""
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    """Hash Table implementation with linked list (chaining)."""
    def __init__(self, initial_capacity=8, load_threshold_factor=0.75):
        self.bucket_number = initial_capacity
        self.bucket = [Node() for _ in range(self.bucket_number)]  # create empty head nodes
        self.size = 0
        self.load_threshold_factor = load_threshold_factor

    def hash(self, key):
        """Hash function to find index."""
        return key % self.bucket_number

    def find(self, head, key):
        """Find the previous node before the key node (for insertion/deletion)."""
        prev = head
        curr = head.next
        while curr and curr.key != key:
            prev = curr
            curr = curr.next
        return prev

    def rehash(self):
        """Double bucket size when load factor is exceeded."""
        old_bucket = self.bucket
        self.bucket_number *= 2
        self.bucket = [Node() for _ in range(self.bucket_number)]
        old_size = self.size
        self.size = 0

        for head in old_bucket:
            curr = head.next
            while curr:
                self.put(curr.key, curr.value)  # reinserting
                curr = curr.next
        print(f"🔁 Rehashed {old_size} items into {self.bucket_number} buckets")

    def put(self, key, value):
        """Insert new item (or chain if same index)."""
        index = self.hash(key)
        head = self.bucket[index]
        prev = self.find(head, key)

        if prev.next:
            prev.next.value = value  # update existing
        else:
            prev.next = Node(key, value)
            self.size += 1

        # Check if rehashing needed
        if self.size / self.bucket_number > self.load_threshold_factor:
            self.rehash()

    def get(self, key):
        """Search product by key."""
        index = self.hash(key)
        head = self.bucket[index]
        prev = self.find(head, key)
        return prev.next.value if prev.next else None

    def delete(self, key):
        """Delete a product by key."""
        index = self.hash(key)
        head = self.bucket[index]
        prev = self.find(head, key)

        if prev.next:
            prev.next = prev.next.next
            self.size -= 1
            print(f"🗑️ Deleted product (ID: {key}) successfully.")
        else:
            print("❌ Product not found.")

    def modify(self, key, **kwargs):
        """Modify a product's details."""
        index = self.hash(key)
        head = self.bucket[index]
        prev = self.find(head, key)

        if prev.next:
            product = prev.next.value
            for field, new_value in kwargs.items():
                if hasattr(product, field):
                    setattr(product, field, new_value)
            print(f"✏️ Modified product (ID: {key}) successfully.")
        else:
            print("❌ Product not found for modification.")

    def display(self):
        """Display all products in hash table."""
        print("\n📦 INVENTORY LIST:")
        for i, bucket in enumerate(self.bucket):
            curr = bucket.next
            if curr:
                print(f"Bucket {i}:")
                while curr:
                    print(f"    {curr.value}")
                    curr = curr.next
        print("-" * 50)
