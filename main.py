from utils import Store, Storage, Shop


def main():
    warehouse = Shop(100)
    warehouse.add("cookies", 3)
    warehouse.add("doggie", 4)
    warehouse.add("boxes", 5)

    store = Store(100)
    store.add("doggie", 2)
    store.add("cookies", 5)

    while True:
        print("What would you like to do?")
        print("1. Take items from warehouse")
        print("2. Deliver items to store")
        print("3. Check warehouse contents")
        print("4. Check store contents")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("What item do you want to take? ")
            quantity = int(input("How many do you want to take? "))
            try:
                warehouse.remove(item, quantity)
                print("The courier took", quantity, item, "from the warehouse")
                print("The courier carries", quantity, item, "from the warehouse to the store")
                store.add(item, quantity)
                print("The courier delivered", quantity, item, "to the store")
            except ValueError:
                print("Not enough", item, "in stock, try to order less")

        elif choice == "2":
            item = input("What item do you want to deliver? ")
            quantity = int(input("How many do you want to deliver? "))
            try:
                store.remove(item, quantity)
                print("The courier took", quantity, item, "from the store")
                print("The courier carries", quantity, item, "from the store to the warehouse")
                warehouse.add(item, quantity)
                print("The courier delivered", quantity, item, "to the warehouse")
            except ValueError:
                print("Not enough", item, "in stock, try to order less")

        elif choice == "3":
            print("Stored in the warehouse:")
            for item, quantity in warehouse.get_items().items():
                print(quantity, item)

        elif choice == "4":
            print("The store is stored:")
            for item, quantity in store.get_items().items():
                print(quantity, item)

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":main()


