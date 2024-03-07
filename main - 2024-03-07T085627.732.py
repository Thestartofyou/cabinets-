import matplotlib.pyplot as plt

class Cabinet:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def visualize(self):
        # Code to visualize the cabinet and items using Matplotlib

class Item:
    def __init__(self, name, length, width, height):
        self.name = name
        self.length = length
        self.width = width
        self.height = height

def main():
    # Input cabinet dimensions from the user
    cabinet_length = float(input("Enter cabinet length: "))
    cabinet_width = float(input("Enter cabinet width: "))
    cabinet_height = float(input("Enter cabinet height: "))

    # Create a cabinet object
    cabinet = Cabinet(cabinet_length, cabinet_width, cabinet_height)

    # Input items and their dimensions from the user
    num_items = int(input("Enter the number of items: "))
    for i in range(num_items):
        item_name = input(f"Enter name of item {i+1}: ")
        item_length = float(input(f"Enter length of item {i+1}: "))
        item_width = float(input(f"Enter width of item {i+1}: "))
        item_height = float(input(f"Enter height of item {i+1}: "))
        item = Item(item_name, item_length, item_width, item_height)
        cabinet.add_item(item)

    # Visualize the cabinet and items
    cabinet.visualize()

if __name__ == "__main__":
    main()

