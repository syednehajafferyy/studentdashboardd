# main.py

from helpers import *

print("===== Welcome to Student Performance Dashboard =====")

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Show Statistics")
    print("5. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            try:
                name = input("Enter Name: ").strip()

                if not name:
                    print("Name cannot be empty.")
                    continue

                if not name.replace(" ", "").isalpha():
                    print("Name cannot contain numbers.")
                    continue

                roll = int(input("Enter Roll Number: "))
                age = int(input("Enter Age: "))
                gender = input("Enter Gender: ").strip()

                total_marks = float(input("Enter Total Marks: "))

                marks = []

                print("Enter marks for S1 to S5:")

                for i in range(5):
                    mark = float(input(f"S{i + 1}: "))
                    marks.append(mark)

                add_student(
                    name,
                    roll,
                    age,
                    gender,
                    marks,
                    total_marks
                )

                print("Student Added Successfully!")

            except ValueError:
                print("Invalid input. Please enter correct data.")

        case "2":
            if not students:
                print("No student records available.")

            else:
                print("\n===== Student Records =====")

                for s in students:
                    print("\n--------------------------")
                    print("Name:", s["name"])
                    print("Roll Number:", s["roll"])
                    print("Age:", s["age"])
                    print("Gender:", s["gender"])
                    print("Marks:", s["marks"])
                    print(
                        f"Obtained Marks: "
                        f"{s['obtained']}/{s['total_marks']}"
                    )
                    print(
                        f"Percentage: "
                        f"{s['percentage']:.2f}%"
                    )
                    print("Grade:", s["grade"])

        case "3":
            try:
                roll = int(input("Enter Roll Number: "))
                student = search_student(roll)

                if student:
                    print("\nStudent Found")
                    print("Name:", student["name"])
                    print(
                        f"Obtained Marks: "
                        f"{student['obtained']}/"
                        f"{student['total_marks']}"
                    )
                    print(
                        f"Percentage: "
                        f"{student['percentage']:.2f}%"
                    )
                    print("Grade:", student["grade"])

                    print(
                        "Factorial of Roll Number:",
                        factorial(student["roll"])
                    )

                else:
                    print("Student not found.")

            except ValueError:
                print("Please enter a valid roll number.")

        case "4":
            show_stats()

        case "5":
            print("Thank you for using Student Performance Dashboard!")
            break

        case _:
            print("Invalid choice. Please try again.")
