import mysql.connector as sql
import re


HOST = "0.0.0.0"
PORT = "3306"
USERNAME = "root"
PASSWD = ""
DATABASE = "students"

mdb = sql.connect(
	host=HOST,
	port=PORT,
	user=USERNAME,
	passwd=PASSWD,
	database=DATABASE
	)
mycursor = mdb.cursor()
#mycursor.execute("CREATE TABLE student ( Id int  PRIMARY KEY AUTO_INCREMENT, roll_no VARCHAR (10) NOT NULL, name VARCHAR (50) NOT NULL, class VARCHAR (5) NOT NULL, aadhar_number VARCHAR (15) NOT NULL, father_name VARCHAR (50) NOT NULL, mother_name VARCHAR (50) NOT NULL, phone_number VARCHAR (20) NOT NULL, occupation VARCHAR (50) NOT NULL, address VARCHAR (600) NOT NULL);")
### validators ###

#mycursor.execute("DROP TABLE student")

def validate_name(name:str) -> bool :
	reg = re.match("[a-z ' ']*", name.lower() )
	if reg != None :
		return reg.span()[1] == len(name)
	return False

def recursion_def(function, data, **kwargs) :
	data = data
	if not function(data) :
		if kwargs.get("input") == True :
			data = input(str(kwargs.get("message", "Quit : "))+" : ")
			recursion_def(function, data, **kwargs)
	if not data :
		return ""
	return data

def max_size_exceeded(object) :
	if len(object[0]) > object[1] :
		return False
	return True

def is_number(num:str) -> bool :
	print(num)
	reg = re.match("[0-9]*", num )
	if reg != None :
		return reg.span()[1] == len(num)
	return False

def validate_all(data:dict) -> bool :
	if (not validate_name(data["name"]) or len(data["name"]) > 50 or len(data["name"]) < 1) :
		print("\nPlease enter a valid Characters (A-z) and length should be not greater than 50 and less than 1 characters...")
		data["name"] = input("Name : ")
		validate_all(data)
	if (not validate_name(data["father_name"]) or len(data["father_name"]) > 50 or len(data["father_name"]) < 1) :
		print("\nPlease enter a valid Characters (A-z) and length should be not greater than 50 and less than 1 characters...")
		data["father_name"] = input("Father Name : ")
		validate_all(data)
	if (not validate_name(data["mother_name"]) or len(data["mother_name"]) > 50 or len(data["mother_name"]) < 1) :
		print("\nPlease enter a valid Characters (A-z) and length should be not greater than 50 and less than 1 characters...")
		data["mother_name"] = input("Mother Name : ")
		validate_all(data)
	if (not validate_name(data["occupation"]) or len(data["occupation"]) > 50 or len(data["occupation"]) < 1) :
		print("\nPlease enter a valid Characters (A-z) and length should be not greater than 50 and less than 1 characters...")
		data["occupation"] = input("Occupation : ")
		validate_all(data)
	if (not is_number(data["roll_no"]) or len(data["roll_no"]) < 0) :
		print("\nPlease enter a valid Characters (0-9)...")
		data["roll_no"] = input("Roll no : ")
		validate_all(data)
	if (not is_number(data["aadhar_number"]) or len(data["aadhar_number"]) > 15 or len(num) < 0) :
		print("\nPlease enter a valid Characters (0-9) and length should be not greater than 15 and less than 1 numbers...")
		data["aadhar_number"] = input("Aadhar Number  : ")
		validate_all(data)
	if (not is_number(data["phone_number"]) or len(data["phone_number"]) > 20 or len(num) < 0):
		print("\nPlease enter a valid Characters (0-9) and length should be not greater than 20 and less than 1 numbers...")
		data["phone_number"] = input("Phone Number  : ")
		validate_all(data)
	if (len(data["address"]) > 600 or len(data["address"]) < 1):
		print("\nLength should be not greater than 600 and smaller than 1 characters...")
		data["address"] = input("Address : ")
		validate_all(data)
	if (len(data["class"]) > 600 or len(data["class"]) < 1):
		print("\nLength should be not greater than 600 and smaller than 1 characters...")
		data["class"] = input("Class : ")
		validate_all(data)
	return True

def validate_all_update(data:dict) -> bool :
	if (not validate_name(data["name"]) or len(data["name"]) > 50) :
		print("\nPlease enter a valid Characters (A-z) and length should be not greater than 50 and less than 1 characters...")
		data["name"] = input("Name : ")
		validate_all_update(data)
	if (not validate_name(data["father_name"]) or len(data["father_name"]) > 50) :
		print("\nPlease enter a valid Characters (A-z) and length should be not greater than 50 and less than 1 characters...")
		data["father_name"] = input("Father Name : ")
		validate_all_update(data)
	if (not validate_name(data["mother_name"]) or len(data["mother_name"]) > 50 ) :
		print("\nPlease enter a valid Characters (A-z) and length should be not greater than 50 and less than 1 characters...")
		data["mother_name"] = input("Mother Name : ")
		validate_all_update(data)
	if (not validate_name(data["occupation"]) or len(data["occupation"]) > 50 ) :
		print("\nPlease enter a valid Characters (A-z) and length should be not greater than 50 and less than 1 characters...")
		data["occupation"] = input("Occupation : ")
		validate_all_update(data)
	if (not is_number(data["roll_no"]) ) :
		print("\nPlease enter a valid Characters (0-9)...")
		data["roll_no"] = input("Roll no : ")
		validate_all_update(data)
	if (not is_number(data["aadhar_number"]) or len(data["aadhar_number"]) > 15 ) :
		print("\nPlease enter a valid Characters (0-9) and length should be not greater than 15 and less than 1 numbers...")
		data["aadhar_number"] = input("Aadhar Number  : ")
		validate_all_update(data)
	if (not is_number(data["phone_number"]) or len(data["phone_number"]) > 20 ):
		print("\nPlease enter a valid Characters (0-9) and length should be not greater than 20 and less than 1 numbers...")
		data["phone_number"] = input("Phone Number  : ")
		validate_all_update(data)
	if (len(data["address"]) > 600 ):
		print("\nLength should be not greater than 600 and smaller than 1 characters...")
		data["address"] = input("Address : ")
		validate_all_update(data)
	if (len(data["class"]) > 600 ):
		print("\nLength should be not greater than 600 and smaller than 1 characters...")
		data["class"] = input("Class : ")
		validate_all_update(data)
	return True

### end validators ###

help_cmd = """create --> to create a new student.
update --> to update a student.
filter --> to filter student
delete --> to delete a student.
exit --> to end program"""

print("#"*6 + " Welcome " + "#"*6)
print("\n\n"+ "*"*6 + " Usage " + "*"*6)
print(help_cmd)
print("*"*19 + "\n\n")


while (True) :
	cmd = input("s: ")
	if (cmd.lower() == "exit") :
		exit()
	else :
		if ("create" in cmd.lower()) :
			print("\n")
			data = {}
			print("*"*15 + "\n")
			data["roll_no"] = input("Roll no : ").strip().lower()
			data["name"] = input("Name: ").strip().lower()
			data["class"] = input("Class (ex -> 10th A): ").strip().lower()
			data["aadhar_number"] = input("Aadhar Number : ").strip().lower()
			data["father_name"] = input("Fathers Name : ").strip().lower()
			data["mother_name"] = input("Mothers Name : ").strip().lower()
			data["phone_number"] = input("Phone Number : ").strip().lower()
			data["occupation"] = input("Occupation : ").strip().lower()
			data["address"] = input("Address : ").strip().lower()
			
			validated_data = validate_all(data)
			if validated_data :
				query = f"INSERT INTO student (roll_no, name, class, aadhar_number, father_name, mother_name, phone_number, occupation, address) VALUES ({data['roll_no']}, '{data['name']}', '{data['class']}', '{data['aadhar_number']}', '{data['father_name']}', '{data['mother_name']}', {data['phone_number']}, '{data['occupation']}', '{data['address']}');"
				mycursor.execute(query)
				print("User created successfully\n")
		elif ("update" in cmd.lower()) :
			data = {}
			print("In Order to update students detail please provide 'Class' and 'Roll no' ...")
			data["class"] = input("Class ( ex -> 10th A) : ")
			data["roll_no"] = input("Roll no : ")
			
			mycursor.reset()
			query = f"SELECT * FROM student WHERE class='{data['class']}' and roll_no='{data['roll_no']}';"
			mycursor.execute(query)
			
			for student in mycursor :
				#print(student)
				data["Id"] = student[0]
				data["roll_no"] = student[1]
				data["name"] = student[2]
				data["class"] = student[3]
				data["aadhar_number"] = student[4]
				data["father_name"] = student[5]
				data["mother_name"] = student[6]
				data["phone_number"] = student[7]
				data["occupation"] = student[8]
				data["address"] = student[9]
			
			print("\n\n#---Students Information---#")
			for key, value in data.items():
				print(f"{key.replace('_', ' ').title()} : {str(value).title()}")
			
			if len(data.items()) > 3 :
				updates = {}
				print("\n\nUpdate Information : Press Enter for Default Value")
				updates["roll_no"] = input("Roll no : ").strip()
				updates["roll_no"] = recursion_def(is_number, updates["roll_no"], input=True, message="Roll no" )
				
				updates["name"] = input("Name: ").strip()
				updates["name"] = recursion_def(validate_name, updates["roll_no"], input=True, message="Name" )
				
				updates["class"] = input("Class (ex -> 10th A): ").strip()
				updates["class"] = recursion_def(max_size_exceeded, [updates["class"], 10], input=True, message="Class" )[0]
				
				updates["aadhar_number"] = input("Aadhar Number : ").strip()
				updates["aadhar_number"] = recursion_def(is_number, updates["aadhar_number"], input=True, message="Aadhar Number" )
				
				updates["father_name"] = input("Fathers Name : ").strip()
				updates["father_name"] = recursion_def(validate_name, updates["father_name"], input=True, message="Fathers Name" )
				
				updates["mother_name"] = input("Mothers Name : ").strip()
				updates["mother_name"] = recursion_def(validate_name, updates["mother_name"], input=True, message="Mothers Name" )
				
				updates["phone_number"] = input("Phone Number : ").strip()
				updates["phone_number"] = recursion_def(is_number, updates["phone_number"], input=True, message="Phone Number" )
				
				updates["occupation"] = input("Occupation : ").strip()
				updates["occupation"] = recursion_def(validate_name, updates["occupation"], input=True, message="Occupation" )
				
				updates["address"] = input("Address : ").strip()
				updates["address"] = recursion_def(max_size_exceeded, [updates["address"], 600], input=True, message="Address" )[0]
				
				validated_data = validate_all_update(updates)
				if validated_data :
					temp = []
					for key, value in updates.items() :
						if value.strip() != "" :
							mycursor.reset()
							query = f"UPDATE student SET {key}='{value}' WHERE class='{data['class']}' and roll_no='{data['roll_no']}';"
							mycursor.execute(query)
							temp.append(True)
						else :
							temp.append(False)
					if all(temp):
						print("Data Updated Successfully!\n")
			else :
				print("There is no student with these Crediantials")
		elif "delete" in cmd.lower():
			data = {}
			print("In Order to Delete students detail please provide 'Class' and 'Roll no' ...")
			data["class"] = input("Class ( ex -> 10th A) : ")
			data["roll_no"] = input("Roll no : ")
			
			mycursor.reset()
			query = f"SELECT * FROM student WHERE class='{data['class']}' and roll_no='{data['roll_no']}';"
			mycursor.execute(query)
			
			for student in mycursor :
				#print(student)
				data["Id"] = student[0]
				data["roll_no"] = student[1]
				data["name"] = student[2]
				data["class"] = student[3]
				data["aadhar_number"] = student[4]
				data["father_name"] = student[5]
				data["mother_name"] = student[6]
				data["phone_number"] = student[7]
				data["occupation"] = student[8]
				data["address"] = student[9]
			
			print("\n\n#---Students Information (verify to delete)---#")
			for key, value in data.items():
				print(f"{key.replace('_', ' ').title()} : {str(value).title()}")
			
			if len(data.items()) > 3 :
				delete = input("Delete student (yes/no) : ")
				if delete == "yes" :
					mycursor.reset()
					query = f"DELETE FROM student WHERE class='{data['class']}' and roll_no='{data['roll_no']}';"
					mycursor.execute(query)
				print(f"\n{data['name']} of Class {data['class']}, Roll no {data['roll_no']}, is being Kicked Out of School")
			else :
				print("There is no student with these Crediantials")
		elif "filter" in cmd.lower() :
			data = {}
			print("In Order to Filter students detail please provide 'Class' and 'Roll no' ...")
			data["class"] = input("Class ( ex -> 10th A) : ")
			data["roll_no"] = input("Roll no : ")
			
			mycursor.reset()
			query = f"SELECT * FROM student WHERE class='{data['class']}' and roll_no='{data['roll_no']}';"
			mycursor.execute(query)
			
			for student in mycursor :
				#print(student)
				data["Id"] = student[0]
				data["roll_no"] = student[1]
				data["name"] = student[2]
				data["class"] = student[3]
				data["aadhar_number"] = student[4]
				data["father_name"] = student[5]
				data["mother_name"] = student[6]
				data["phone_number"] = student[7]
				data["occupation"] = student[8]
				data["address"] = student[9]
			
			print("\n\n#---Students Information---#")
			for key, value in data.items():
				print(f"{key.replace('_', ' ').title()} : {str(value).title()}")
			print("\nSuccessfully filtered\n\n")
		elif "help" in cmd.lower() :
			print(help_cmd)
		elif cmd.replace(" ", "") == "":
			pass
		else :
			print("Please enter a valid command or type 'help' to get list of Commands...\n")