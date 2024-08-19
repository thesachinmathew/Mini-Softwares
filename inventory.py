import pandas as pd
import numpy as np

class InventoryItem:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class InventorySystem:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item):
        """Adds an item to the inventory."""
        self.inventory[item.product_id] = item

    def update_item(self, product_id, new_quantity, new_price=None):
        """Updates an item's quantity and optionally price."""
        if product_id in self.inventory:
            item = self.inventory[product_id]
            item.quantity = new_quantity
            if new_price:
                item.price = new_price
        else:
            print("Item not found")

    def delete_item(self, product_id):
        """Deletes an item from the inventory."""
        if product_id in self.inventory:
            del self.inventory[product_id]
        else:
            print("Item not found")

    def get_item(self, product_id):
        """Retrieves an item from the inventory."""
        if product_id in self.inventory:
            return self.inventory[product_id]
        else:
            return None

    def get_all_items(self):
        """Returns a list of all inventory items."""
        return list(self.inventory.values())

inventory_system = InventorySystem()

# Add items
item1 = InventoryItem(1, "Product A", 10.0, 100)
item2 = InventoryItem(2, "Product B", 15.0, 50)
inventory_system.add_item(item1)
inventory_system.add_item(item2)

# Update item
inventory_system.update_item(1, 120, 12.0)

# Delete item
inventory_system.delete_item(2)

# Get item
item = inventory_system.get_item(1)
print(item.name, item.price, item.quantity)

# Get all items
all_items = inventory_system.get_all_items()
for item in all_items:
    print(item.product_id, item.name)
