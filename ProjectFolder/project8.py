#grade manager
student={}
def load_student():
    with open("student.txt","r") as file:
        for line in file:
            line=line.strip()
            data=line.split(",")
            student[data[0]]=int(data[1])
def save_student():
    with open("student.txt","w") as file:
        for name,mark in student.items():
            file.write(f'{name},{mark}\n')
def add_student():
    name=input("Enter student name: ")
    if name in student:
        print("Student already exists")
    else:
        while True:
            mark=input("Enter mark: ")
            if mark.isdigit():
                mark=int(mark)
                student[name]=mark
                print("Student added successfully!")
                break
            else:
                print("Enter mark in digit")
def view_student():
    for name,mark in student.items():
        print(name,":",mark)
def search_student():
    search=input("Enter student name: ")
    for name in student:
        if search.lower()==name.lower():
            print(name,":",student[name])
            break
    else:
        print("Student not found")
def update_student():
    update=input("Enter student name: ")
    for name in student:
        if update.lower()==name.lower():
            while True:
                mark=input("Enter new mark: ")
                if mark.isdigit():
                    mark=int(mark)
                    student[name]=mark
                    print("Marks updated successfully")
                    break
                else:
                   print("Enter mark in digit")
            break
    else:
        print("Student not found")
def delete_student():
    del_name=input("Enter student name: ")
    for name in student:
        if del_name.lower()==name.lower():
            confirm=input('Are your sure(yes/no): ')
            if confirm=="yes":
                del student[name]
                print("Student deleted successfully")
            else:
                print("Not deleted")
            break
    else:
        print("Student not found")
def statistics():
    if student:
       highest=list(student.values())[0]
       lowest=list(student.values())[0]
       tot_marks=0
       for name,mark in student.items():
           if mark>highest:
               topper=name
               highest=mark
           if mark<lowest:
               lowest=mark
           tot_marks+=mark
       print(f'Highest Mark: {highest}')
       print(f'Lowest Mark: {lowest}')
       print(f'Average Mark: {tot_marks/len(student):.2f}')
       print(f'Total Student: {len(student)}')
       print(f'Topper: {topper}')
    else:
        print("Student record is empty")
def grade_report():
    for name,mark in student.items():
        if mark>=90 and mark<=100:
            print(f'{name} : {mark} : A')
        elif mark>=80 and mark<=89:
            print(f'{name} : {mark} : B')
        elif mark>=70 and mark<=79:
            print(f'{name} : {mark} : C')
        elif mark>=60 and mark<=69:
            print(f'{name} : {mark} : D')
        else:
            print(f'{name} : {mark} : F')
menu="\t\t====Student Grade Manager====\n1. Add Student\n2. View all students\n3. Search Student\n4. Update Marks\n5. Delete Student\n6. Statistics\n7. Grade Report\n8. Exit"
load_student()
while True:
    print(menu)
    choice=input("Enter your choice: ")
    if choice.isdigit():
        choice=int(choice)
        if choice==1:
            add_student()
            save_student()
        elif choice==2:
            view_student()
        elif choice==3:
            search_student()
        elif choice==4:
            update_student()
            save_student()
        elif choice==5:
            delete_student()
            save_student()
        elif choice==6:
            statistics()
        elif choice==7:
            grade_report()
        elif choice==8:
            break
        else:
            print("Unknown choice!")
    else:
        print("The choice should be of digit")