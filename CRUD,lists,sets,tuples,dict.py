import json

# CRUD operations for a list
def list_crud():
    my_list = []
    while True:
        print("\nList CRUD")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Save to file")
        print("6. Load from file")
        print("7. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            item = input("Enter item to add: ")
            my_list.append(item)
        elif choice == '2':
            print("List:", my_list)
        elif choice == '3':
            index = int(input("Enter index to update: "))
            if 0 <= index < len(my_list):
                new_item = input("Enter new item: ")
                my_list[index] = new_item
            else:
                print("Invalid index")
        elif choice == '4':
            index = int(input("Enter index to delete: "))
            if 0 <= index < len(my_list):
                my_list.pop(index)
            else:
                print("Invalid index")
        elif choice == '5':
            with open('list_data.json', 'w') as file:
                json.dump(my_list, file)
            print("List saved to list_data.json")
        elif choice == '6':
            with open('list_data.json', 'r') as file:
                my_list = json.load(file)
            print("List loaded from list_data.json")
        elif choice == '7':
            break
        else:
            print("Invalid choice")

# CRUD operations for a set
def set_crud():
    my_set = set()
    while True:
        print("\nSet CRUD")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Save to file")
        print("6. Load from file")
        print("7. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            item = input("Enter item to add: ")
            my_set.add(item)
        elif choice == '2':
            print("Set:", my_set)
        elif choice == '3':
            old_item = input("Enter item to update: ")
            if old_item in my_set:
                new_item = input("Enter new item: ")
                my_set.remove(old_item)
                my_set.add(new_item)
            else:
                print("Item not found")
        elif choice == '4':
            item = input("Enter item to delete: ")
            my_set.discard(item)
        elif choice == '5':
            with open('set_data.json', 'w') as file:
                json.dump(list(my_set), file)
            print("Set saved to set_data.json")
        elif choice == '6':
            with open('set_data.json', 'r') as file:
                my_set = set(json.load(file))
            print("Set loaded from set_data.json")
        elif choice == '7':
            break
        else:
            print("Invalid choice")

# CRUD operations for a tuple
def tuple_crud():
    my_tuple = ()
    while True:
        print("\nTuple CRUD")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Save to file")
        print("6. Load from file")
        print("7. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            item = input("Enter item to add: ")
            my_tuple += (item,)
        elif choice == '2':
            print("Tuple:", my_tuple)
        elif choice == '3':
            index = int(input("Enter index to update: "))
            if 0 <= index < len(my_tuple):
                new_item = input("Enter new item: ")
                my_tuple = my_tuple[:index] + (new_item,) + my_tuple[index+1:]
            else:
                print("Invalid index")
        elif choice == '4':
            index = int(input("Enter index to delete: "))
            if 0 <= index < len(my_tuple):
                my_tuple = my_tuple[:index] + my_tuple[index+1:]
            else:
                print("Invalid index")
        elif choice == '5':
            with open('tuple_data.json', 'w') as file:
                json.dump(my_tuple, file)
            print("Tuple saved to tuple_data.json")
        elif choice == '6':
            with open('tuple_data.json', 'r') as file:
                my_tuple = tuple(json.load(file))
            print("Tuple loaded from tuple_data.json")
        elif choice == '7':
            break
        else:
            print("Invalid choice")

# CRUD operations for a dictionary
def dict_crud():
    my_dict = {}
    while True:
        print("\nDictionary CRUD")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Save to file")
        print("6. Load from file")
        print("7. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value
        elif choice == '2':
            print("Dictionary:", my_dict)
        elif choice == '3':
            key = input("Enter key to update: ")
            if key in my_dict:
                new_value = input("Enter new value: ")
                my_dict[key] = new_value
            else:
                print("Key not found")
        elif choice == '4':
            key = input("Enter key to delete: ")
            if key in my_dict:
                del my_dict[key]
            else:
                print("Key not found")
        elif choice == '5':
            with open('dict_data.json', 'w') as file:
                json.dump(my_dict, file)
            print("Dictionary saved to dict_data.json")
        elif choice == '6':
            with open('dict_data.json', 'r') as file:
                my_dict = json.load(file)
            print("Dictionary loaded from dict_data.json")
        elif choice == '7':
            break
        else:
            print("Invalid choice")

def main():
    while True:
        print("\nCRUD Operations Menu")
        print("1. List CRUD")
        print("2. Set CRUD")
        print("3. Tuple CRUD")
        print("4. Dictionary CRUD")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            list_crud()
        elif choice == '2':
            set_crud()
        elif choice == '3':
            tuple_crud()
        elif choice == '4':
            dict_crud()
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()