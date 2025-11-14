from hash_table import HashTable
from product import HygieneProduct, BathProduct, FeedingProduct, SkinCareProduct, BabyProduct

def run_cli():
    inventory = HashTable(8)  

    # Predefined products
    inventory.put(1, FeedingProduct(1, "Baby Bottle", 15.00, 40))
    inventory.put(2, HygieneProduct(2, "Baby Diapers", 40.00, 100))
    inventory.put(3, SkinCareProduct(3, "Baby Lotion", 25.00, 60))
    inventory.put(4, SkinCareProduct(4, "Baby Shampoos", 15.00, 50))

    print("🍼 Welcome to Baby Shop Inventory System 🍼")

    categories = ["HygieneProduct", "BathProduct", "FeedingProduct", "SkincareProduct"]

    while True:
        print("\nMenu:")
        print("1. Insert new product")
        print("2. Search product")
        print("3. Modify product")
        print("4. Delete product")
        print("5. Display all")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n🧸 Available Categories: HygieneProduct, BathProduct, FeedingProduct, SkincareProduct or others (default General)")

            # Validate Product ID
            while True:
                try:
                    product_id = int(input("Enter Product ID: ").strip())
                    break
                except ValueError:
                    print("❌ Invalid ID. Please enter an integer.")

            product_name = input("Enter Product Name: ").strip().title()
            category = input("Enter Product Category: ").strip().title()

            # Validate price
            while True:
                try:
                    price = float(input("Enter Product Price: ").strip())
                    break
                except ValueError:
                    print("❌ Invalid price. Enter a number.")

            # Validate quantity
            while True:
                try:
                    quantity = int(input("Enter Product Quantity: ").strip())
                    break
                except ValueError:
                    print("❌ Invalid quantity. Enter an integer.")

            # Choose subclass
            category_lower = category.lower()
            if category_lower == "hygiene":
                product = HygieneProduct(product_id, product_name, price, quantity)
            elif category_lower == "bath":
                product = BathProduct(product_id, product_name, price, quantity)
            elif category_lower == "feeding":
                product = FeedingProduct(product_id, product_name, price, quantity)
            elif category_lower == "skincare":
                product = SkinCareProduct(product_id, product_name, price, quantity)
            else:
                product = BabyProduct(product_id, product_name, category, price, quantity)

            inventory.put(product_id, product)

        elif choice == "2":
            try:
                key = int(input("Enter the product ID to search: ").strip())
                result = inventory.get(key)
                if result:
                    print(f"🔍 Found: {result}")
                else:
                    print("❌ Product not found.")
            except ValueError:
                print("❌ Invalid ID.")

        elif choice == "3":
            try:
                key = int(input("Enter product ID to modify: ").strip())
            except ValueError:
                print("❌ Invalid ID.")
                continue

            new_name = input("Enter new name (leave blank to skip): ").strip()
            new_price = input("Enter new price (leave blank to skip): ").strip()
            new_quantity = input("Enter new quantity (leave blank to skip): ").strip()

            kwargs = {}
            if new_name: kwargs["name"] = new_name.title()
            if new_price:
                try:
                    kwargs["price"] = float(new_price)
                except ValueError:
                    print("❌ Invalid price. Skipping price update.")
            if new_quantity:
                try:
                    kwargs["quantity"] = int(new_quantity)
                except ValueError:
                    print("❌ Invalid quantity. Skipping quantity update.")

            inventory.modify(key, **kwargs)

        elif choice == "4":
            try:
                key = int(input("Enter product ID to delete: ").strip())
                inventory.delete(key)
            except ValueError:
                print("❌ Invalid ID.")

        elif choice == "5":
            inventory.display()

        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break

        else:1
            print("⚠️ Invalid choice, try again.")


if __name__ == "__main__":
    run_cli()
