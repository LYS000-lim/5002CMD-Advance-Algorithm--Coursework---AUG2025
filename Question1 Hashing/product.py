# Products of baby shop
class BabyProduct:
    """Base class representing a generic baby product."""
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"[{self.product_id}] {self.name} ({self.category}) - RM{self.price:.2f}, Stock: {self.quantity}"


# Subclasses for specific product types
class FeedingProduct(BabyProduct):
    def __init__(self, product_id, name, price, quantity):
        super().__init__(product_id, name, "Feeding", price, quantity)


class HygieneProduct(BabyProduct):
    def __init__(self, product_id, name, price, quantity):
        super().__init__(product_id, name, "Hygiene", price, quantity)


class SkinCareProduct(BabyProduct):
    def __init__(self, product_id, name, price, quantity):
        super().__init__(product_id, name, "SkinCare", price, quantity)


class BathProduct(BabyProduct):
    def __init__(self, product_id, name, price, quantity):
        super().__init__(product_id, name, "Bath", price, quantity)
