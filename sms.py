import csv
student_fields = ['Name' , 'Class' , 'Section' , 'Roll Number' , 'DOB' , 'Age' , 'Gender' , 'Email'  , 'Address', 'Phone Number']
student_database = 'students.csv'


def display_menu():
    print("--------------------------------------")
    print("Satwik Saurav College")
    print("---------------------------------------")
    print("1. Add Student Data")
    print("2. View Existing Student Data")
    print("3. Search Student by Name")
    print("4. Update Student Data")
    print("5. Delete Student Data")
    print("6. Kill Program")


def add_student():
    print("-------------------------")
    print("Add Student Data")
    print("-------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any button to continue")
    return


def view_students():
    global student_fields
    global student_database

    print("--- Student Records and Data ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def search_student():
    global student_fields
    global student_database

    print("Search Student")
    roll = input("Enter Name to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("----- Student Found -----")
                    print("Name: ", row[0])
                    print("Class: ", row[1])
                    print("Section:", row[2])
                    print("Roll Number: ", row[3])
                    print("DOB: ", row[4])
                    print("Age: ",row[5])
                    print("Gender: ",row [6])
                    print("Email: ",row [7])
                    print("Address: ",row [8])
                    print("Phone Number: ",row[9])
                    break
        else:
            print("Name not found in our database")
    input("Press any key to continue")


def update_student():
    global student_fields
    global student_database

    print("--- Update Student ---")
    roll = input("Enter Name to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1

    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Name not found in our database")

    input("Press any key to continue")


def delete_student():
    global student_fields
    global student_database

    print("--- Delete Student ---")
    roll = input("Enter Name to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Student data", roll, "deleted successfully")
    else:
        print("Name not found in our database")

    input("Press any key to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break

print("-------------------------------")
print(" End of program")
print("-------------------------------")
