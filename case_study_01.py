# Case Study 12: Attendance Recovery Computation

student_name = input("Student name: ")
classes_attended = int(input("Total classes attended so far: "))
total_classes = int(input("Total classes conducted so far: "))

if classes_attended < 0 or total_classes <= 0 or classes_attended > total_classes:
    print("Invalid input.")
else:
    attendance_percentage = (classes_attended / total_classes) * 100
    print("\nStudent:", student_name)
    print("Current attendance:", round(attendance_percentage, 2), "%")
    
    if attendance_percentage >= 75.0:
        print("Status: Eligible (Attendance is already 75% or more)")
    else:
        # Simple loop: keep adding 1 class until attendance reaches 75%
        classes_needed = 0
        new_attended = classes_attended
        new_total = total_classes
        
        while (new_attended / new_total) * 100 < 75.0:
            new_attended = new_attended + 1
            new_total = new_total + 1
            classes_needed = classes_needed + 1
            
        print("Status: Shortage of attendance!")
        print("Minimum consecutive classes needed to reach 75%:", classes_needed)
