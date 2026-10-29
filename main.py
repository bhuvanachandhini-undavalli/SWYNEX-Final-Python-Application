
def calculate_grade(average):
    """Calculate a grade based on average marks."""
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    return "F"


def get_marks():
    """Get and validate three subject marks."""
    marks = []

    for subject in range(1, 4):
        while True:
            try:
                mark = float(
                    input(f"Enter marks for subject {subject} (0-100): ")
                )

                if not 0 <= mark <= 100:
                    print("Error: Marks must be between 0 and 100.")
                    continue

                marks.append(mark)
                break

            except ValueError:
                print("Error: Enter a valid number.")

    return marks


def add_student(students):
    """Add a student and generate a report."""
    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Name cannot be empty.")
        return

    marks = get_marks()
    total = sum(marks)
    average = total / len(marks)

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": calculate_grade(average),
    }

    students.append(student)

    print("\n--- Student Report ---")
    print(f"Name: {name}")
    print(f"Total: {total:.2f}/300")
    print(f"Average: {average:.2f}%")
    print(f"Grade: {student['grade']}")
    print("Student report added successfully!")


def view_students(students):
    """Display all student reports."""
    if not students:
        print("No student reports available.")
        return

    for number, student in enumerate(students, start=1):
        print(f"\n--- Student {number} ---")
        print(f"Name: {student['name']}")
        print(f"Total: {student['total']:.2f}/300")
        print(f"Average: {student['average']:.2f}%")
        print(f"Grade: {student['grade']}")


def main():
    """Run the application."""
    students = []

    while True:
        print("\n=== Student Report Management System ===")
        print("1. Add student report")
        print("2. View student reports")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            print("Thank you for using the application!")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
