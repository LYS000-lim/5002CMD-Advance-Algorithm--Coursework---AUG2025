from hash_table import HashTable
from product import HygieneProduct, BathProduct, FeedingProduct, SkinCareProduct, BabyProduct

def run_cli():
    inventory = HashTable(5)

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

        choice = input(int("Enter your choice"))

        if choice == 1:
            product_id = input(int("Enter Product ID"))
            product_name = input("Enter Product Name")
            category = input("Enter Product Category")
            price = input(float("Enter Product Price"))
            quantity = input("Enter Product Quantity")

            if category.lower == "hygience":
                product = HygieneProduct(product_id, product_name, price, quantity)
            elif category.lower == "bath":
                product = BathProduct(product_id, product_name, price, quantity)
            elif category.lower == "feeding":
                product = FeedingProduct(product_id, product_name, price, quantity)
            elif category.lower == "skincare":
                product = SkinCareProduct(product_id, product_name, price, quantity)
            else:
                product = BabyProduct(product_id, product_name, category, price, quantity)

            inventory.put(product_id, product)

        elif choice == 2:
            key = input(int("Enter the key number you want to search"))
            result = inventory.get(key)
            if result:
                print(result)
            else:
                print("Result no found")

        elif choice == 3:
            key = input("Enter Id you want to modify")
            new_name = input("Enter new name")
            new_price = input(float("Enter new price"))
            new_quantity = input(int("Enter new quantity"))

            kwargs = {}

            if new_name: kwargs["name"] = new_name
            if new_name: kwargs["price"] = new_price
            if new_name: kwargs["quantity"] = new_quantity

            inventory.modify(key, **kwargs)

        elif choice == 4:
            key = input("Enter Id you want to delete")
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