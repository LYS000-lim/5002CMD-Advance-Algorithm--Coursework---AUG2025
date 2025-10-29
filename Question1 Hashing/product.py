class BabyProduct:
    def __init__(self, producy_id, name, category, price, quantity):
        self.product_id = producy_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"[{self.product_id}] {self.name} ({self.category}) - RM{self.price:.2f}, Stock: {self.stock}"
        
class FeedingProduct(BabyProduct):
    def __init__(self, producy_id, name, price, quantity):
        super().__init__(producy_id, name, "Feeding", price, quantity)

class HygieneProduct(BabyProduct):
    def __init__(self, producy_id, name, price, quantity):
        super().__init__(producy_id, name, "Hygience", price, quantity)

class SkinCareProduct(BabyProduct):
    def __init__(self, producy_id, name, price, quantity):
        super().__init__(producy_id, name, "SkinCare", price, quantity)
    
class BathProduct(BabyProduct):
    def __init__(self, producy_id, name, price, quantity):
        super().__init__(producy_id, name, "Bath", price, quantity)



