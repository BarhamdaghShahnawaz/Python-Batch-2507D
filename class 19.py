name = input("Enter your name: ")
roll_no = input("Enter your roll number: ")

subjects = ["Maths","English","Science","History","Geography","Computer","Urdu"]

marks = {}

for subject in subjects:
    score = int(input("Enter your marks for {}: ".format(subject)))

    marks[subject] = score
    total = sum(marks.values())
    average = total / len(subjects)
    percentage = (total /(len(subjects)*100))*100

    if percentage >= 90:
        grade = "A+"

    elif percentage >= 80:
        grade = "A"

    elif percentage >=70:
        grade = "B"
    
    elif percentage >= 60:
        grade = "C"

    elif percentage >= 40:
        grade = "D"
    
    else:
        grade = "Fail"

    
    failed_subjects = [sub for sub,score in marks.items()if score < 40]

    status = "pass" if len(failed_subjects)== 0 else "fail"

    student_report = {
        "Name": name,
        "Roll No": roll_no,
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Percentage": percentage,
        "Grade": grade,
        "Status": status,
        "Failed Subjects": failed_subjects
    }

english = 76

print("\n=== Student Report Card ===")

print("Name:",student_report["Name"])
print("Roll No:",student_report["Roll No"])
print("Marks:")
for sub,score in student_report["Marks"].items():
        print("{sub}:{score}")
print("Total:",student_report["Total"])
print("Average:",(student_report["Average"],2))
print("percentage:",round(student_report["Percentage"],2),"%")
print("Grade:",student_report["Grade"])
print("Status:",student_report["Status"])
if student_report["Status"]=="fail":
 print("Failed Subjects:",student_report["Failed Subjects"])