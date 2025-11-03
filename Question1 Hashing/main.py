from hash_table import HashTable
from product import HygieneProduct, BathProduct, FeedingProduct, SkinCareProduct, BabyProduct

def run_cli():
    inventory = HashTable(5)

    # Predefined products
    inventory.put(1, FeedingProduct(1, "Baby Bottle", 15.00, 40))
    inventory.put(2, HygieneProduct(2, "Baby Diapers", 40.00, 100))
    inventory.put(3, SkinCareProduct(3, "Baby Lotion", 25.00, 60))

    print("🍼 Welcome to Baby Shop Inventory System 🍼")

    while True:
        print("\nMenu:")
        print("1. Insert new product")
        print("2. Search product")
        print("3. Modify product")
        print("4. Delete product")
        print("5. Display all")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = int(input("Enter Product ID: "))
            product_name = input("Enter Product Name: ")
            category = input("Enter Product Category: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))

            # Choose subclass based on category
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
            print(f"✅ Product '{product_name}' added successfully!")

        elif choice == "2":
            key = int(input("Enter the product ID to search: "))
            result = inventory.get(key)
            if result:
                print(f"🔍 Found: {result}")
            else:
                print("❌ Product not found.")

        elif choice == "3":
            key = int(input("Enter product ID to modify: "))
            new_name = input("Enter new name (leave blank to skip): ")
            new_price = input("Enter new price (leave blank to skip): ")
            new_quantity = input("Enter new quantity (leave blank to skip): ")

            kwargs = {}
            if new_name: kwargs["name"] = new_name
            if new_price: kwargs["price"] = float(new_price)
            if new_quantity: kwargs["quantity"] = int(new_quantity)

            inventory.modify(key, **kwargs)

        elif choice == "4":
            key = int(input("Enter product ID to delete: "))
            inventory.delete(key)

        elif choice == "5":
            inventory.display()

        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("⚠️ Invalid choice, try again.")


if __name__ == "__main__":
    run_cli()
