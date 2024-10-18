#Inventory Management system for a market

# Define the inventory list
inventory = []


# Function to add a new item to the inventory
def add_item(name, price, quantity, category):
    item = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'category': category
    }
    inventory.append(item)
    print("Item added: " + name)


# Function to update details of an existing item
def update_item(name, price=None, quantity=None, category=None):
    for item in inventory:
        if item['name'] == name:
            if price is not None:
                item['price'] = price
            if quantity is not None:
                item['quantity'] = quantity
            if category is not None:
                item['category'] = category
            print("Item updated: " + name)
            return
    print("Item not found.")


# Function to view all items in the inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    for item in inventory:
        print("Name: " + item['name'] + ", Price: " + str(item['price']) +
              ", Quantity: " + str(item['quantity']) + ", Category: " + item['category'])


# Function to remove an item from the inventory
def remove_item(name):
    global inventory
    inventory = [item for item in inventory if item['name'] != name]
    print("Item removed: " + name)


# Function to search for items by category
def search_by_category(category):
    items_in_category = [item for item in inventory if item['category'] == category]
    if items_in_category:
        print("Items in category: " + category)
        for item in items_in_category:
            print("Name: " + item['name'] + ", Price: " + str(item['price']) +
                  ", Quantity: " + str(item['quantity']) + ", Category: " + item['category'])
    else:
        print("No items found in category: " + category)


# Main loop to get user input
def main():
    while True:
        print(
            "\nChoose an option: (1) Add Item (2) Update Item (3) View Inventory (4) Remove Item (5) Search by Category (6) Exit")
        Userchoice = input("Enter your choice: ")

        if Userchoice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            category = input("Enter item category: ")
            add_item(name, price, quantity, category)

        elif Userchoice == '2':
            name = input("Enter the name of the item to update: ")
            price = input("Enter new price: ")
            price = float(price) if price else None
            quantity = input("Enter new quantity: ")
            quantity = int(quantity) if quantity else None
            category = input("Enter new category: ")
            update_item(name, price, quantity, category)

        elif Userchoice == '3':
            view_inventory()

        elif Userchoice == '4':
            name = input("Enter the name of the item to remove: ")
            remove_item(name)

        elif Userchoice == '5':
            category = input("Enter category to search: ")
            search_by_category(category)

        elif Userchoice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main loop
main()
