import os
import platform

def initialize():
	global studentlist
	studentlist=[]
	global rollNo
	rollNo=[]
	with open('studentList.txt','r') as file:
		for line in file:
			if "Name:" in line:
				stu_name=line.split(':')
				studentlist.append(stu_name[1].rstrip())
			elif "Roll.No:" in line:
				stu_no=line.split(':')
				rollNo.append(stu_no[1].rstrip())

def studentmanagement():
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

	if x==1:
		print("Student List\n")
		f=open('studentList.txt','r')
		print(f.read())
		f.close()
		#print(studentlist)
		#print(rollNo)
	elif x==2:
		c = len(studentlist)
		r = len(rollNo)
		f=open('studentList.txt','a')
		#print(c)
		#print(r)
		#s="Student"+str(c+1)+":"
		print("Enter Student Name: ")
		name1=input()
		studentlist.append(name1)
		name="Name:"+name1
		if r==0:
			rollNo.append(str(101))
		else:
			rollNo.append(str(int(rollNo[r - 1]) + 1))
		num="Roll.No:"+rollNo[r]
		f.write("\n")
		#f.write(s)
		#f.write("\n")
		f.write(num)
		f.write("\n")
		f.write(name)
		f.write("\n")
		#print(rollNo)
		#print(studentlist)
		f.close()
	elif x==3:
		studentsearching = input("Choose Student Number To Search: ")
		c=1
		with open('studentList.txt') as file:
			for line in file:
				if studentsearching in line:
					print("Record Found")
					print("Roll.No: "+studentsearching)
					print(next(file))
					#student_index=rollNo.index(studentsearching)
					#print(studentlist[student_index]+" "+rollNo[student_index])
					c=0
			if c==1:
				print("\nThere is No Record Found Of this Student {}".format(studentsearching))

	elif x==4:
		studentdelete = input("Choose a Student Number To Delete: ")
		if studentdelete in rollNo:
			student_index = rollNo.index(studentdelete)
			with open('studentList.txt','r') as file:
				data=file.readlines()
			with open('studentList.txt','w') as file:
				for line in data:
					if not (studentdelete in line or str(studentlist[student_index]) in line):
						file.write(line)
					else:
						continue
			del rollNo[student_index]
			del studentlist[student_index]
			print(rollNo)
			print(studentlist)
			with open('studentList.txt') as file:
				print(file.read())
		else:
			print("\n There is No Record Found of This Student {} ".format(studentdelete))

	elif x < 1 or x > 4:
		print("Please Enter Valid Choice")



def continueAgain():
	runningagain = input("\nWant to continue the process yes/no?: ")
	if runningagain.lower() == 'yes':
		if platform.system() == "Windows":
			print(os.system('cls'))
		else:
			print(os.system('clear'))
		studentmanagement()
		continueAgain()
	else:
		quit()
if __name__=="__main__" :
	initialize()
	studentmanagement()
	continueAgain()
