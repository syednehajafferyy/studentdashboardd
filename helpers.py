# helpers.py

students = []


def calculate_percentage(obtained, total_marks):
    try:
        return (obtained / total_marks) * 100
    except ZeroDivisionError:
        return 0


def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def add_student(name, roll, age, gender, marks, total_marks):
    obtained = sum(marks)
    percentage = calculate_percentage(obtained, total_marks)
    grade = assign_grade(percentage)

    student = {
        "name": name.title(),
        "roll": roll,
        "age": age,
        "gender": gender.capitalize(),
        "marks": marks,
        "obtained": obtained,
        "total_marks": total_marks,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)


def search_student(roll):
    for student in students:
        if student["roll"] == roll:
            return student
    return None


def show_stats():
    if not students:
        print("No records available.")
        return

    highest = max(students, key=lambda s: s["obtained"])

    print("\nHighest Scorer")
    print("Name:", highest["name"])
    print("Obtained Marks:", highest["obtained"])

    print("\nSubject Averages:")
    for i in range(5):
        avg = sum(s["marks"][i] for s in students) / len(students)
        print(f"S{i + 1}: {avg:.2f}")


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)