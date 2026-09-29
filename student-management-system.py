student_names = [
    "Amreen",
    "Eshrath",
    "Uma",
    "Pallavi",
    "Srilatha",
    "Manasa",
    "Vara Lakhsmi",
    "Bhavani",
    "Fareen",
    "Venkat Lakshmi",
    "Swathi"
]
marks = [78, 98, 67, 99, 87, 88, 72, 99, 28, 95, 93]

def display_students():
    for roll, names in enumerate(student_names, start=201):
        print(f"Roll No:{roll} | Name : {names} | Marks : {marks[roll-201]}")
        
def add_students():
    name = input("Add New Student Name : ")
    mark = int(input("Enter percentage of New Students  : "))
    student_names.append(name)
    marks.append(mark)
    return f"New Student {name} Added Successfully"


def delete_students():
    roll = int(input("Enter Roll Number to Delete Student :"))
    index = roll-201
    if 0 <= index < len(student_names):
        student_names.pop(index)
        marks.pop(index)
        return f"Deleted Successfully!"
    return "Invalid Roll Number.." 


def update_students():
    roll = int(input("Enter the Student Roll Number : "))
    index = roll-201
    if 0 <= index < len(student_names):
        print(f"1. Update Name\n2. Update Marks")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            student_names[index] = input("Student New Name : ")
            return "Name Updated Successfully"
        elif choice == 2:
            marks[index] = int(input("Enter Student New Marks : "))
            return "Marks Updated Successfully"
        else:
            return "Invalid Choice"
    return "Invalid Roll Number.."


def  search_by_name():
    name = input("Enter Student Name : ")
    
    found = False
    
    for i in range(len(student_names)):
        if student_names[i].lower() == name.lower():
            found = True
            return f"Student Found\nRoll No : {201+i}\nMarks : {marks[i]}"
            break
    if not found:
        return "Student Not Found.."
    
    
def search_by_rollno():
    roll = int(input("Enter Student Roll_Number : "))
    
    index = roll-201
    if 0 <= index < len(student_names):
        return f"""Student Found
              Name : {student_names[index]}
              Marks : {marks[index]}"""
    
    return "Student Not Found"

def topper():
    highest = max(marks)
    index = marks.index(highest)
    
    return f"""Topper Details
        Roll No: {201+index}
        Name: {student_names[index]}
        Marks: {highest}"""
    

def lowest_marks():
    lowest = min(marks)
    index = marks.index(lowest)
    
    return f"""Topper Details
        Roll No: {201+index}
        Name: {student_names[index]}
        Marks: {lowest}"""


def total_students():
    return f"Total Students: {len(student_names)}"


print("-" * 35)
print("Student Management System")
print("-" * 35)

while True:
    
    
    print("""
        1. Display All Students
        2. Add Student
        3. Delete Student
        4. Update Student Details
        5. Search Student by Name
        6. Search Student by Roll Number
        7. Find Topper
        8. Find Lowest Marks
        9. Count Students
        10. Exit
        """)
    print("-"*35)
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        print("Display function called")
        display_students()
    elif choice == 2:
        print(add_students())
    elif choice == 3:
        print(delete_students())
    elif choice == 4:
        print(update_students())
    elif choice == 5:
        print(search_by_name())
    elif choice == 6:
        print(search_by_rollno())
    elif choice == 7:
        print(topper())
    elif choice == 8:
        print(lowest_marks())
    elif choice == 9:
        print(total_students())
    elif choice == 10:
        print("ThankYou! for Visiting")
        break
    else:
        print("Invalid choice...")
    
