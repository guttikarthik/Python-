# Case Study 39: Multi-Stage Examination Eligibility System

student_name = input("Student name: ")
attendance_percentage = float(input("Attendance percentage (%): "))
internal_marks = float(input("Internal marks (out of 50): "))
is_lab_record_completed = input("Is lab record completed? (yes/no): ").strip().lower()
is_college_fee_cleared = input("Are college fees cleared? (yes/no): ").strip().lower()

lab_ok = (is_lab_record_completed == "yes" or is_lab_record_completed == "y")
fee_ok = (is_college_fee_cleared == "yes" or is_college_fee_cleared == "y")

print("\n--- Exam Eligibility Result ---")
print("Student:", student_name)

if attendance_percentage >= 75.0 and internal_marks >= 20.0 and lab_ok and fee_ok:
    print("Status: ELIGIBLE FOR EXAMINATIONS (Hall ticket issued)")
else:
    print("Status: NOT ELIGIBLE (Hall ticket withheld)")
    print("Reasons for ineligibility:")
    if attendance_percentage < 75.0:
        print(" - Attendance is below 75%")
    if internal_marks < 20.0:
        print(" - Internal marks below passing score (20/50)")
    if not lab_ok:
        print(" - Lab record incomplete")
    if not fee_ok:
        print(" - College fees pending")
