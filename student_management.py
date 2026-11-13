
# Student Record Management System

# 1. Store student information using a list of dictionaries

students = [
    {
        "name": "Dass",
        "age": None,
        "department": "CSE",
        "marks": [78, 85, 72],
        "attendance": 91
    },
    {
        "name": "Chandra",
        "age": None,
        "department": "CSE",
        "marks": [65, 71, 68],
        "attendance": 84
    },
    {
        "name": "Parvathi",
        "age": None,
        "department": "ECE",
        "marks": [45, 52, 48],
        "attendance": 72
    }
]


# 2. Calculate average marks
def calculate_average(student):
    return sum(student["marks"]) / len(student["marks"])


# 3. Check pass or fail
def check_result(student, passing_marks=40):
    if calculate_average(student) >= passing_marks:
        return "PASS"
    else:
        return "FAIL"


# 4. Display all students
def display_students():
    print("\n--- ALL STUDENT RECORDS ---")

    for student in students:
        print("\nName:", student["name"])
        print("Age:", student["age"] if student["age"] else "Not provided")
        print("Department:", student["department"])
        print("Marks:", student["marks"])
        print("Attendance:", str(student["attendance"]) + "%")
        print("Average:", round(calculate_average(student), 1))
        print("Result:", check_result(student))


# 5. Find the highest-performing student
def find_topper():
    topper = max(students, key=calculate_average)

    print("\n--- TOP PERFORMER ---")
    print("Name:", topper["name"])
    print("Average:", round(calculate_average(topper), 1))


# 6. Filter students by attendance
def filter_by_attendance(limit):
    print(f"\n--- ATTENDANCE BELOW {limit}% ---")

    found = False

    for student in students:
        if student["attendance"] < limit:
            print(student["name"], "-", str(student["attendance"]) + "%")
            found = True

    if not found:
        print("No students found.")


# 7. Filter students by average marks
def filter_by_marks(minimum):
    print(f"\n--- STUDENTS WITH AVERAGE ABOVE {minimum} ---")

    for student in students:
        if calculate_average(student) >= minimum:
            print(student["name"], "-", round(calculate_average(student), 1))


# 8. Display class summary
def class_summary():
    total_students = len(students)

    all_marks = [
        mark
        for student in students
        for mark in student["marks"]
    ]

    class_average = sum(all_marks) / len(all_marks)

    print("\n========== CLASS SUMMARY ==========")
    print("Total Students:", total_students)
    print("Average Class Mark:", round(class_average, 1))

    find_topper()
    filter_by_attendance(75)


# 9. Display final results
def display_results():
    print("\n--- STUDENT RESULTS ---")

    for student in students:
        print(student["name"], "-", check_result(student))


# 10. Main program
display_students()
class_summary()
filter_by_marks(70)
display_results()

display_students()
class_summary()
filter_by_marks(70)
display_results()

print("PROGRAM STARTED SUCCESSFULLY!")