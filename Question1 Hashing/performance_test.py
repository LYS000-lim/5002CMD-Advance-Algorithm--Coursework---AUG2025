# Compare Linked list in hash table vs one-dimensional array performance

import time
from hash_table import HashTable
from product import BabyProduct


def performance_test():
    print("\n⚙️ PERFORMANCE TEST: Linked list in hash table vs. a one-dimensional array ⚙️")

    # Create hash table and list
    hash_table = HashTable(50)
    product_list = []

    # Insert 10,000 products
    print("Generating 10,000 sample products...")
    for i in range(10000):
        product = BabyProduct(i, f"Product-{i}", "General", price=i * 0.5, quantity=10)
        hash_table.put(i, product)
        product_list.append(product)

    # Ask user for target ID to search
    target_id = int(input("Enter the product ID number you want to test (e.g., 9999): "))

    # --- Hash Table Search ---
    start_time = time.time()
    hash_result = hash_table.get(target_id)
    hash_duration = time.time() - start_time

    # --- List Search ---
    start_time = time.time()
    list_result = None
    for product in product_list:
        if product.product_id == target_id:
            list_result = product
            break
    list_duration = time.time() - start_time

    print(f"\n🔍 Search target: ID {target_id}")
    print(f"✅ Linked list in hash table result: {hash_result}")
    print(f"✅ one-dimensional array result: {list_result}")

    print("\n📊 Performance Comparison:")
    print(f"Linked list in hash table search time: {hash_duration:.8f} seconds")
    print(f"one-dimensional array search time:      {list_duration:.8f} seconds")

    improvement = (list_duration / hash_duration) if hash_duration > 0 else 0
    print(f"\n⚡ Linked list in hash table is approximately {improvement:.2f}× faster than one-dimensional array search.")


if __name__ == "__main__":
    performance_test()
