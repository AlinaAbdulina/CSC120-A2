class Computer:

    # Attributes: 
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

   # Constructor for a new computer 
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, 
                 memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # Updates operating system for the computer
    def update_os(self, new_os: str):
        self.operating_system = new_os

    # Updates price for the computer
    def update_price(self, new_price: int):
        self.price = new_price