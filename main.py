from db_class import MySQLDatabase

db = MySQLDatabase("python")
db.connection()

while True:
    print("\n--- Management System ---")
    print("1. Add User")
    print("2. List Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    
    try:
        choice = int(input("Select an option (1-5): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 1:
        name = input("Enter a name: ")
        lastname = input("Enter a lastname: ")
        age = int(input("Enter an age: "))
        values = {"user_name": name, "user_lastname": lastname, "user_age": age}
        db.insert_record("users", values)

    elif choice == 2:
        result = db.getRows("SELECT * FROM users WHERE user_active=%s", (1,))
        if result:
            print("\nID\tName\tLastname\tAge")
            for item in result:
                print(f"{item[0]}\t{item[1]}\t{item[2]}\t\t{item[3]}")
        else:
            print("No active users found!")

    elif choice == 3:
        user_id = int(input("Enter id number you want to update: "))
        name_update = input("Enter a name: ")
        lastname_update = input("Enter a lastname: ")
        age_update = int(input("Enter an age: "))
        
        columns = {"user_name": name_update, "user_lastname": lastname_update, "user_age": age_update}
        conditions = {"user_id": user_id}
        db.update("users", columns, conditions)

    elif choice == 4:
        user_id = int(input("Enter id number you want to delete: "))
        columns={"user_active":0}
        conditions={"user_id":user_id}
        db.update("users",columns,conditions)
    elif choice == 5:
        print("Exiting.. Goodbye")
        break 

    else:
        print("Invalid choice! Please select between 1 and 5.")

db.disconnect()