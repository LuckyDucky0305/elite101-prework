#initializing arrays for the inventory and the user's cart.
inventory = []
cart = []

def action(choice):
    if choice == "1":
        print("Displaying inventory")
    elif choice == "2":
        print("Display shopping cart")
    elif choice == "3":
        print("Recommending you a craft related hobby")


print("-----Welcome to Caitlin's Craft Store Chatbot-----")
name = input("What is your name? ")
age = input("Hello " + name + ", how old are you? ")

while True:
    print("---Caitlin's Craft Store---")
    print("1. View the inventory")
    print("2. Add to shopping cart")
    print("3. Recommend me a craft related hobby")
    print("4. Exit")
    choice = input("How can I help? ")
    if choice == "4":
        print("Thank you! Please come again")
        break
    action(choice)
