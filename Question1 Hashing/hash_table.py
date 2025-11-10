class Node:
    """Node class for linked list chaining inside hash table."""
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    """Hash Table implementation with linked list (chaining)."""
    def __init__(self, initial_capacity=8, load_threshold_factor=0.75):
        self.initial_capacity = initial_capacity  # keep original capacity
        self.bucket_number = initial_capacity
        self.bucket = [Node() for _ in range(self.bucket_number)]
        self.size = 0
        self.load_threshold_factor = load_threshold_factor

    def hash(self, key):
        return key % self.bucket_number

    def find(self, head, key):
        prev = head
        curr = head.next
        while curr and curr.key != key:
            prev = curr
            curr = curr.next
        return prev

    def rehash(self):
        old_bucket = self.bucket
        self.bucket_number *= 2
        self.bucket = [Node() for _ in range(self.bucket_number)]
        old_size = self.size
        self.size = 0

        for head in old_bucket:
            curr = head.next
            while curr:
                self.put(curr.key, curr.value, rehashing=True)
                curr = curr.next
        print(f"🔁 Rehashed {old_size} items into {self.bucket_number} buckets")

    def put(self, key, value, rehashing=False):
        """Insert new product. Warn if key exists, allow chaining."""
        index = self.hash(key)
        head = self.bucket[index]
        prev = self.find(head, key)

        if prev.next and not rehashing:
            print(f"⚠️ Product with ID {key} already exists. Use modify() to update it.")
            return

        # Optional: format name and category if present
        if hasattr(value, "name"):
            value.name = value.name.title()
        if hasattr(value, "category"):
            value.category = value.category.title()

        # Insert at head of chain
        new_node = Node(key, value)
        new_node.next = head.next
        head.next = new_node
        if not rehashing:
            self.size += 1
            print(f"✅ Added new product (ID {key})")

            # Rehash if load factor exceeded
            if self.size / self.bucket_number > self.load_threshold_factor:
                self.rehash()

    def get(self, key):
        index = self.hash(key)
        head = self.bucket[index]
        prev = self.find(head, key)
        return prev.next.value if prev.next else None

    def delete(self, key):
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
        index = self.hash(key)
        head = self.bucket[index]
        prev = self.find(head, key)
        if prev.next:
            product = prev.next.value
            for field, new_value in kwargs.items():
                if hasattr(product, field):
                    if field in ["name", "category"] and isinstance(new_value, str):
                        new_value = new_value.title()
                    setattr(product, field, new_value)
            print(f"✏️ Modified product (ID: {key}) successfully.")
        else:
            print("❌ Product not found for modification.")

    def display(self):
        """Display all buckets according to the original capacity."""
        print("\n📦 INVENTORY LIST:")
        for i in range(self.initial_capacity):
            print(f"Bucket Index {i}:")
            curr = self.bucket[i].next
            if curr:
                while curr:
                    print(f"    Key {curr.key} -> {curr.value}")
                    curr = curr.next
            else:
                print("    (empty)")
        print("-" * 50)
