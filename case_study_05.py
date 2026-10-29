# Case Study 21: Traffic Violation Penalty Calculator

vehicle_number = input("Vehicle registration number: ")
print("Violations:")
print("1. No Helmet / No Seatbelt (Rs. 500)")
print("2. Signal Jumping (Rs. 1000)")
print("3. Overspeeding (Rs. 1500)")
print("4. Drunk Driving (Rs. 10000)")

violation_choice = input("Select violation (1-4): ").strip().lower()
is_repeat_offence = input("Is this a repeat offence? (yes/no): ").strip().lower()

if violation_choice == "1" or violation_choice == "helmet" or violation_choice == "seatbelt":
    offence_name = "No Helmet / Seatbelt"
    fine_amount = 500.0
elif violation_choice == "2" or violation_choice == "signal":
    offence_name = "Signal Jumping"
    fine_amount = 1000.0
elif violation_choice == "3" or violation_choice == "overspeeding" or violation_choice == "speeding":
    offence_name = "Overspeeding"
    fine_amount = 1500.0
elif violation_choice == "4" or violation_choice == "drunk driving":
    offence_name = "Drunk Driving"
    fine_amount = 10000.0
else:
    offence_name = "None"
    fine_amount = 0.0

if offence_name == "None":
    print("Invalid violation choice! Please select 1, 2, 3, or 4.")
else:
    repeat_status = "No"
    if is_repeat_offence == "yes" or is_repeat_offence == "y":
        fine_amount = fine_amount + (fine_amount * 0.5)  # Add 50% extra fine for repeat offence
        repeat_status = "Yes"

    print("\n--- Traffic E-Challan ---")
    print("Vehicle Number :", vehicle_number)
    print("Violation Type :", offence_name)
    print("Repeat Offender:", repeat_status)
    print("Total Fine Due : Rs.", round(fine_amount, 2))

    if fine_amount >= 5000:
        print("Action Notice  : LICENSE SUSPENDED FOR COURT REVIEW")
