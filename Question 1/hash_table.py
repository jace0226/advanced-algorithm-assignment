# Defines HashTable with linear probing
from product import Product

# Data Structure: Open Addressing Hash Table
class HashTable:
    # Hash table implementation using Open Addressing with Linear Probing
    # None: Slot has never been used. "DELETED": Slot previously held a product that was removed.
    def __init__(self, capacity: int = 2000):
        self.capacity = capacity
        # Pre-allocate array slots initialized to None
        self.table = [None] * self.capacity
        self.count = 0

    def _hash_function(self, key: int) -> int:
        # Modulo Hash Function: maps an integer key to an index slot
        return key % self.capacity

    # Insert function
    def insert(self, product: Product) -> int:
        # Insert a product using linear probing, returns the index where the ite, was stored, or -1 if full.
        if self.count >= self.capacity:
            print("Error: Hash Table is full")
            return -1

        index = self._hash_function(product.product_id)
        first_deleted_slot = -1

        # Probe sequentially through table slots
        for i in range(self.capacity):
            probe_idx = (index + i) % self.capacity
            slot = self.table[probe_idx]

            # Check for duplicate key (update instead of inserting duplicate)
            if slot is not None and slot != "DELETED" and slot.product_id == product.product_id:
                self.table[probe_idx] = product
                return probe_idx

            # Track first available tombstone slot
            if slot == "DELETED" and first_deleted_slot == -1:
                first_deleted_slot = probe_idx

            # Empty slot found
            if slot is None:
                target_idx = first_deleted_slot if first_deleted_slot != -1 else probe_idx
                self.table[target_idx] = product
                self.count += 1
                return target_idx

        # If table was full of DELETED slots
        if first_deleted_slot != -1:
            self.table[first_deleted_slot] = product
            self.count += 1
            return first_deleted_slot

        return -1

    # Search function
    def search(self, product_id: int):
        # Searches for a product by product_id using linear probing. Returns (Product, slot_index) if found, otherwise (None, -1)
        index = self._hash_function(product_id)

        for i in range(self.capacity):
            probe_idx = (index + i) % self.capacity
            slot = self.table[probe_idx]

            # Stop searching if an unallocated slot is reached
            if slot is None:
                return None, -1

            # Skip tombstone markers
            if slot != "DELETED" and slot.product_id == product_id:
                return slot, probe_idx

        return None, -1

    # Edit function
    def edit(self, product_id: int, new_name: str = None, new_price: float = None, new_stock: int = None) -> bool:
        # Edits fields of an existing product
        product, idx = self.search(product_id)
        if product is None:
            return False

        if new_name is not None:
            product.name = new_name
        if new_price is not None:
            product.price = new_price
        if new_stock is not None:
            product.stock = new_stock

        return True

    # Delete function
    def delete(self, product_id: int) -> bool:
        # Soft-deletes a product by placing a 'DELETED' tombstone marker so probe chains remain intact
        product, idx = self.search(product_id)
        if product is not None:
            self.table[idx] = "DELETED"
            self.count -= 1
            return True
        return False