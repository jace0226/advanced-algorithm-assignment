# Contains the CLI menu & performance benchmarks

import time
from product import Product
from hash_table import HashTable
from utils import array_search, get_valid_int, get_valid_float

def main():
    # Initialize Hash Table and parallel Array
    hash_table = HashTable(capacity=2000)
    array_storage = []

    # Pre-defined records insertion
    initial_products = [
        Product(1010, "Panadol 500mg", 6.50, 100),
        Product(1025, "Amoxicillin 250mg", 15.00, 50),
        Product(1030, "Cough Syrup 100ml", 8.20,80)
    ]

    # Add 1,000 dummy products to array to simulate a realistic pharmacy database
    for i in range(1, 1000):
        dummy_prod = Product(i, f"Medicine {i}", 10.0, 50)
        array_storage.append(dummy_prod)
        hash_table.insert(dummy_prod)

    # Insert target products at the end of the array
    for prod in initial_products:
        hash_table.insert(prod)
        array_storage.append(prod)

    while True:
        print("\n=== Pharmacy Inventory System ===")
        print("1. Insert Product")
        print("2. Search Product")
        print("3. Edit Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            pid = get_valid_int("Enter product ID: ")
            name = input("Enter product name: ").strip()
            while not name:
                print("Product name cannot be empty!")
                name = input("Enter Product Name: ").strip()
            price = get_valid_float("Enter product price: ")
            stock = get_valid_int("Enter product stock: ")

            new_product = Product(pid, name, price, stock)

            # Insert into Hash Table and Array
            slot = hash_table.insert(new_product)
            if slot != -1:
                # Check if item exists in array to avoid duplicate array entries
                existing = array_search(array_storage, pid)
                if existing:
                    existing.name = name
                    existing.price = price
                    existing.stock = stock
                else:
                    array_storage.append(new_product)

                # Requirement output format matching sample brief
                print(f"Product inserted successfully into slot [{slot}]")
            else:
                # Clear error message when insertion fails
                print(
                    f"Insert unsuccessful! The Hash Table is full or no available slot could be found for Product ID {pid}.")

        elif choice == "2":
            pid = get_valid_int("Enter product ID to search: ")

            # Benchmark Hash Table Search
            start_hash = time.perf_counter_ns()
            prod_hash, slot = hash_table.search(pid)
            end_hash = time.perf_counter_ns()
            time_hash = (end_hash - start_hash) / 1e9 # seconds

            # Benchmark Array Search
            start_arr = time.perf_counter_ns()
            prod_arr = array_search(array_storage, pid)
            end_arr = time.perf_counter_ns()
            time_arr = (end_arr - start_arr) / 1e9 # seconds

            if prod_hash:
                print("\nProduct found!")
                print(f"ID: {prod_hash.product_id} | Name: {prod_hash.name} | Price: RM{prod_hash.price:.2f} | Stock: {prod_hash.stock}")
                print(f"Search completed in {time_hash:.6f} seconds (Hash Table)")
                print(f"Search completed in {time_arr:.6f} seconds (Array - same record)")
            else:
                print("\nProduct not found!")

        elif choice == "3":
            pid = get_valid_int("Enter Product ID to edit: ")
            prod, _ = hash_table.search(pid)
            if prod:
                print(f"Current details: {prod}")
                new_name = input("Enter new Name (leave blank to skip): ").strip()

                price_str = input("Enter new Price (leave blank to skip): ").strip()
                new_price = None
                if price_str:
                    while True:
                        try:
                            new_price = float(price_str)
                            break
                        except ValueError:
                            print("Invalid input! Please enter a valid price number.")
                            price_str = input("Enter new Price: ").strip()

                stock_str = input("Enter new Stock (leave blank to skip): ").strip()
                new_stock = None
                if stock_str:
                    while True:
                        try:
                            new_stock = int(stock_str)
                            break
                        except ValueError:
                            print("Invalid input! Please enter a valid integer for stock.")
                            stock_str = input("Enter new Stock: ").strip()

                new_name = new_name if new_name else None

                # Edit Hash Table & Parallel Array
                hash_table.edit(pid, new_name, new_price, new_stock)
                for p in array_storage:
                    if p.product_id == pid:
                        if new_name: p.name = new_name
                        if new_price: p.price = new_price
                        if new_stock: p.stock = new_stock

                print("Product updated successfully!")
            else:
                print("Product not found!")

        elif choice == "4":
            pid = get_valid_int("Enter Product ID to delete: ")
            success = hash_table.delete(pid)
            if success:
                array_storage[:] = [p for p in array_storage if p.product_id != pid]
                print(f"Product ID {pid} deleted successfully!")
            else:
                print("Product not found!")

        elif choice == "5":
            print("Exiting Inventory System. Goodbye!")
            break
        else:
            print("Invalid option! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()