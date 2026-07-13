import tkinter as tk
from tkinter import messagebox
from helpers import *

window = tk.Tk()
window.title("Student Performance Dashboard")
window.geometry("700x650")
window.configure(bg="light pink")

# ---------- Labels and Entries ----------

tk.Label(window, text="Name", bg="light pink").grid(
    row=0, column=0, padx=10, pady=5
)
name_entry = tk.Entry(window, width=25)
name_entry.grid(row=0, column=1)

tk.Label(window, text="Roll Number", bg="light pink").grid(
    row=1, column=0, padx=10, pady=5
)
roll_entry = tk.Entry(window, width=25)
roll_entry.grid(row=1, column=1)

tk.Label(window, text="Age", bg="light pink").grid(
    row=2, column=0, padx=10, pady=5
)
age_entry = tk.Entry(window, width=25)
age_entry.grid(row=2, column=1)

tk.Label(window, text="Gender", bg="light pink").grid(
    row=3, column=0, padx=10, pady=5
)
gender_entry = tk.Entry(window, width=25)
gender_entry.grid(row=3, column=1)

tk.Label(window, text="Total Marks", bg="light pink").grid(
    row=4, column=0, padx=10, pady=5
)
total_marks_entry = tk.Entry(window, width=25)
total_marks_entry.grid(row=4, column=1)

# ---------- Subject Marks ----------

mark_entries = []

for i in range(5):
    tk.Label(
        window,
        text=f"S{i + 1}",
        bg="light pink"
    ).grid(row=i + 5, column=0, padx=10, pady=5)

    entry = tk.Entry(window, width=25)
    entry.grid(row=i + 5, column=1)
    mark_entries.append(entry)

# ---------- Output ----------

output = tk.Text(window, width=60, height=12)
output.grid(row=10, column=0, columnspan=3, padx=20, pady=20)


# ---------- Functions ----------

def submit():
    try:
        name = name_entry.get().strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        if not name.replace(" ", "").isalpha():
            raise ValueError("Name cannot contain numbers.")

        roll = int(roll_entry.get())
        age = int(age_entry.get())
        gender = gender_entry.get()

        total_marks = float(total_marks_entry.get())

        marks = []
        for entry in mark_entries:
            marks.append(float(entry.get()))

        add_student(
            name,
            roll,
            age,
            gender,
            marks,
            total_marks
        )

        output.delete("1.0", tk.END)

        for s in students:
            output.insert(
                tk.END,
                f"Name: {s['name']}\n"
                f"Roll No: {s['roll']}\n"
                f"Obtained Marks: {s['obtained']}/{s['total_marks']}\n"
                f"Percentage: {s['percentage']:.2f}%\n"
                f"Grade: {s['grade']}\n"
                f"{'-' * 40}\n"
            )

        messagebox.showinfo(
            "Success",
            "Student Added Successfully!"
        )

        clear()

    except ValueError as e:
        messagebox.showerror("Error", str(e))


def clear():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    total_marks_entry.delete(0, tk.END)

    for entry in mark_entries:
        entry.delete(0, tk.END)


# ---------- Buttons ----------

tk.Button(
    window,
    text="Submit",
    width=15,
    command=submit
).grid(row=11, column=0, pady=10)

tk.Button(
    window,
    text="Clear",
    width=15,
    command=clear
).grid(row=11, column=1, pady=10)

window.mainloop()
