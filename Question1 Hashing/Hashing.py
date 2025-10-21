class BabyProduct:
    def __init__(self, producy_id, name, category, price, quantity):
        self.product_id = producy_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        
class FeedingProduct(BabyProduct):
    def __init__(self, producy_id, name, price, quantity):
        super().__init__(producy_id, name, "Feeding", price, quantity)

class HygienceProduct(BabyProduct):
    def __init__(self, producy_id, name, price, quantity):
        super().__init__(producy_id, name, "Hygience", price, quantity)

class SkinCareProduct(BabyProduct):
    def __init__(self, producy_id, name, price, quantity):
        super().__init__(producy_id, name, "SkinCare", price, quantity)
    
class BathProduct(BabyProduct):
    def __init__(self, producy_id, name, price, quantity):
        super().__init__(producy_id, name, "Bath", price, quantity)

class Node:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    def __init__(self, inititial_capacity=8, load_factor_thresold=0.75):
        self.bucket_count = inititial_capacity
        self.bucket = [Node() for _ in range(self.bucket_count)]
        self.size = 0
        self.load_factor_thresold = load_factor_thresold