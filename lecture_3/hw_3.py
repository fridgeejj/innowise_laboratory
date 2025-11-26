# List to store student data
# Each student will be represented as a dictionary with keys "name" and "grades"
students = []

# Function to find a student by name
# Returns the student dictionary if found, otherwise None
def find_student(name):
    for student in students:
        if student["name"].lower() == name.lower():  # Compare names case-insensitively
            return student
    return None

# Function to calculate the average grade
# Returns None if the grades list is empty
def calculate_average(grades):
    if len(grades) == 0:
        return None
    return sum(grades) / len(grades)

# Main program loop. The menu will repeat until the user chooses "Exit"
while True:
    # Display the menu
    print("--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add a grades for a student")
    print("3. Show report (all students)")
    print("4. Find top performer")
    print("5. Exit")
    
    # Handle invalid menu input (non-integer)
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue  # Go back to the start of the loop if input is invalid

    # Option 1: Add a new student
    if choice == 1:
        name = input("Enter student name: ").strip()  # Remove leading/trailing spaces
        if name == "":  # Check for empty name
            print("Name cannot be empty.")
        elif find_student(name):  # Check if student already exists
            print("Student already exists.")
        else:
            students.append({"name": name, "grades": []})  # Add new student

    # Option 2: Add grades for a student
    elif choice == 2:
        name = input("Enter student name: ").strip()
        if name == "":  # Check for empty name
            print("Name cannot be empty.")
            continue
        student = find_student(name)
        if not student:  # If student not found
            print("Student not found.")
            continue
        # Input grades until user enters 'done'
        while True:
            grade_input = input("Enter grade (or 'done'): ").strip()
            if grade_input.lower() == "done":
                break
            try:
                grade = int(grade_input)
                if 0 <= grade <= 100:  # Check grade range
                    student["grades"].append(grade)
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:  # If input is not a number
                print("Invalid input. Please enter a number.")

    # Option 3: Show report for all students
    elif choice == 3:
        if not students:  # If there are no students
            print("No students available.")
            continue
        print("\n--- Student Report ---")
        all_averages = []
        for student in students:
            try:
                avg = calculate_average(student["grades"])
                if avg is None:  # If student has no grades
                    print(f"{student['name']}'s average grade is N/A.")
                else:
                    print(f"{student['name']}'s average grade is {avg:.1f}.")  # Format average to 1 decimal
                    all_averages.append(avg)
            except ZeroDivisionError:  # Just in case
                print(f"{student['name']}'s average grade is N/A.")
        # If there are any grades, print summary
        if all_averages:
            print("--------------------------")
            print(f"Max Average: {max(all_averages):.1f}")
            print(f"Min Average: {min(all_averages):.1f}")
            print(f"Overall Average: {sum(all_averages) / len(all_averages):.1f}")
        else:
            print("No grades available to calculate summary.")

    # Option 4: Find the top performer
    elif choice == 4:
        # Only consider students who have at least one grade
        valid_students = [student for student in students if student["grades"]]
        if not valid_students:  # If no students have grades
            print("No students with grades available.")
        else:
            # Find student with the highest average
            top_student = max(valid_students, key=lambda s: calculate_average(s["grades"]))
            top_avg = calculate_average(top_student["grades"])
            print(f"The student with the highest average is {top_student['name']} with a grade of {top_avg:.1f}.")

    # Option 5: Exit the program
    elif choice == 5:
        print("Exiting program.")
        break

    # Handle invalid menu options
    else:
        print("Invalid option. Choose 1-5.")
