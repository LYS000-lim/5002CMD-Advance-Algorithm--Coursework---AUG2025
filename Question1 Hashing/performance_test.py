# performance_test.py
# Compare HashTable vs. List search performance

import time
from hash_table import HashTable
from product import BabyProduct


def performance_test():
    print("\n⚙️ PERFORMANCE TEST: Hash Table vs. List Search ⚙️")

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
    print(f"✅ HashTable result: {hash_result}")
    print(f"✅ List result: {list_result}")

    print("\n📊 Performance Comparison:")
    print(f"HashTable search time: {hash_duration:.8f} seconds")
    print(f"List search time:      {list_duration:.8f} seconds")

    improvement = (list_duration / hash_duration) if hash_duration > 0 else 0
    print(f"\n⚡ HashTable is approximately {improvement:.2f}× faster than List search (for this run).")


if __name__ == "__main__":
    performance_test()
