# import csv

# with open("students.csv", "w", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(["id", "name", "age", "grade", "subject_name", "mark"])

# N1

# def add_student(student_info):
#     with open("students.csv", "r", encoding="utf-8") as f:
#         reader = csv.reader(f)
#         data = list(reader)

#     header = data[0]
#     students = data[1:]

#     students.append(student_info)

#     students.sort(key=lambda x: int(x[0]))

#     with open("students.csv", "w", newline="", encoding="utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerow(header)
#         writer.writerows(students)

# user_input = input("Student information (id,name,age,grade,subject_name,mark): ")
# student_info = user_input.split(",")

# add_student(student_info)

# N2

# def read_students(student_id=None):
#     with open("students.csv", "r", encoding="utf-8") as f:
#         reader = csv.DictReader(f)
#         students = list(reader)

#     if student_id is None:
#         return students
#     else:
#         for s in students:
#             if s['id'] == student_id:
#                 return s
#         return "Not found"
    
# user_input = input("Input student id or a for all students: ")
# if user_input != "a":
#     print(read_students(user_input))
# else:
#     students = read_students()
#     for student in students:
#         print(student)
        
# N3
# def calculate_average_mark():
#     with open("students.csv", "r", encoding="utf-8") as f:
#         reader = csv.DictReader(f)
#         students = list(reader)

#     sum = 0
#     count = 0
#     for s in students:
#         sum += int(s["mark"]) 
#         count += 1

#     if count == 0:
#         return 0 

#     return sum / count
    

# print(calculate_average_mark())

# N4
# def update_mark(student_id, subject, new_mark):
#     with open("students.csv", "r", encoding="utf-8") as f:
#         reader = csv.DictReader(f)
#         students = list(reader)
#         fieldnames = reader.fieldnames

#     found = False
#     for s in students:
#         if s["id"] == student_id and s["subject_name"] == subject:
#             found = True
#             s["mark"] = new_mark
#     if found:
#         with open("students.csv", "w", newline="", encoding="utf-8") as f:
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(students)
#     else:
#         print("Not Found")
    
# student_id = input("Input student id: ")
# subject = input("Input subject: ")
# new_mark = input("Input new mark: ")

# update_mark(student_id, subject, new_mark)