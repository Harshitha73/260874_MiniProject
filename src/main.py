import os
import platform


def show_elements():
    print("Student List\n")
    f = open('studentList.txt', 'r')
    print(f.read())
    f.close()
    # print(student_list)
    # print(rollNo)


def add_element():
    # c = len(student_list)
    r = len(roll_no)
    f = open('studentList.txt', 'a')
    # print(c)
    # print(r)
    # s="Student"+str(c+1)+":"
    print("Enter Student Name: ")
    name1 = input()
    student_list.append(name1)
    name = "Name:" + name1
    if r == 0:
        roll_no.append(str(101))
    else:
        roll_no.append(str(int(roll_no[r - 1]) + 1))
    num = "Roll.No:" + roll_no[r]
    f.write("\n")
    # f.write(s)
    # f.write("\n")
    f.write(num)
    f.write("\n")
    f.write(name)
    f.write("\n")
    # print(rollNo)
    # print(student_list)
    f.close()


def search_element():
    student_searching = input("Choose Student Number To Search: ")
    c = 1
    with open('studentList.txt') as file:
        for line in file:
            if student_searching in line:
                print("Record Found")
                print("Roll.No: " + student_searching)
                print(next(file))
                # student_index=rollNo.index(student_searching)
                # print(student_list[student_index]+" "+rollNo[student_index])
                c = 0
        if c == 1:
            print("\nThere is No Record Found Of this Student {}".format(student_searching))


def delete_element():
    student_delete = input("Choose a Student Number To Delete: ")
    if student_delete in roll_no:
        student_index = roll_no.index(student_delete)
        with open('studentList.txt', 'r') as file:
            data = file.readlines()
        with open('studentList.txt', 'w') as file:
            for line in data:
                if not (student_delete in line or str(student_list[student_index]) in line):
                    file.write(line)
                else:
                    continue
        del roll_no[student_index]
        del student_list[student_index]
        print(roll_no)
        print(student_list)
        with open('studentList.txt') as file:
            print(file.read())
    else:
        print("\n There is No Record Found of This Student {} ".format(student_delete))


def initialize():
    global student_list
    global roll_no
    student_list = []
    roll_no = []
    with open('studentList.txt', 'r') as file:
        for line in file:
            if "Name:" in line:
                stu_name = line.split(':')
                student_list.append(stu_name[1].rstrip())
            elif "Roll.No:" in line:
                stu_no = line.split(':')
                roll_no.append(stu_no[1].rstrip())


def student_management():
    initialize()
    print("\n.......... Welcome to Student Management System ...........\n")
    print("[Choice 1: Showing the List of Student]")
    print("[Choice 2: Add New Student]")
    print("[Choice 3: Searching Student]")
    print("[Choice 4: Deleting a Student]\n")

    try:
        x = int(input("Enter a choice: "))
    except ValueError:
        exit("\nThis is not a Number")
    else:
        print("\n")

    if x == 1:
        show_elements()
    elif x == 2:
        add_element()
    elif x == 3:
        search_element()
    elif x == 4:
        delete_element()
    elif x < 1 or x > 4:
        print("Please Enter Valid Choice")


def continue_again():
    running_again = input("\nWant to continue the process yes/no?: ")
    if running_again.lower() == 'yes':
        if platform.system() == "Windows":
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        student_management()
        continue_again()
    else:
        quit()


if __name__ == "__main__":
    initialize()
    student_management()
    continue_again()
