from computer import Computer

class ResaleShop:

    # Constructor for a new resale shop with an inventory 
    def __init__(self):
        self.inventory = []

    # Buys a computer and adds it to the inventory
    def buy(self, computer: Computer):
        self.inventory.append(computer)
        return len(self.inventory) - 1

    # Sells a computer and removes it from the inventory
    def sell(self, item_id: int):
        if 0 <= item_id < len(self.inventory) and self.inventory[item_id] is not None:
            self.inventory[item_id] = None
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    # Prints the current inventory of the resale shop
    def print_inventory(self):
        if self.inventory:
            for i, item in enumerate(self.inventory):
                if item is not None:
                    print(f'Item ID: {i} : {item}')
        else:
            print("No inventory to display.")

    # Refurbishes a computer in the inventory
    def refurbish(self, item_id: int, new_os=None):
        if 0 <= item_id < len(self.inventory) and self.inventory[item_id] is not None:
            computer = self.inventory[item_id]
            
            # Update price based on year made
            if computer.year_made < 2000:
                computer.update_price(0)
            elif computer.year_made < 2012:
                computer.update_price(250)
            elif computer.year_made < 2018:
                computer.update_price(550)
            else:
                computer.update_price(1000)
            
            # Update OS if provided
            if new_os is not None:
                computer.update_os(new_os)
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")