from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__():
        pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    def buy(self):
    
    def print_inventory():
    # If the inventory is not empty
    if inventory:
        # For each item
        for item in inventory:
            # Print its details
            print(f'Item ID: {inventory.index(item)} : {item}')
    else:
        print("No inventory to display.")

    def sell(item_id: int):
    if inventory[item_id] is not None:
        inventory.pop(item_id)
        print("Item", item_id, "sold!")
    else: 
        print("Item", item_id, "not found. Please select another item to sell.")
    
    def update_price(item_id: int, new_price: int):
    if inventory[item_id] is not None:
        inventory[item_id]["price"] = new_price
    else:
        print("Item", item_id, "not found. Cannot update price.")

    def buy(computer: Dict):
    inventory.append(computer)
    return inventory.index(computer)
        