# Part B - Shopping List Manager

shopping_list = []

while True:
    choice = input("\nOptions - add / remove / show / done: ").strip().lower()
    
    if choice == "add":
        item = input("Enter item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' has been added to your list.")
        
    elif choice == "remove":
        item = input("Enter item to remove: ").strip()
        # Check if it is actually in the list with 'in' before calling .remove()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from your list.")
        else:
            print("That item is not on your list.")
            
    elif choice == "show":
        print("\nCurrent Shopping List:")
        if not shopping_list:
            print("List is empty.")
        else:
            for item in shopping_list:
                print(f"- {item}")
                
    elif choice == "done":
        print("Goodbye! Happy shopping.")
        break
    else:
        print("Invalid option. Please choose add, remove, show, or done.")