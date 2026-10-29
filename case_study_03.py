# Case Study 15: Smart Parking Fee Management

print("Vehicle Types: 1. Two-Wheeler (Bike), 2. Four-Wheeler (Car)")
vehicle_choice = input("Select vehicle type (1 or 2): ").strip().lower()
parked_hours = float(input("Enter parked hours: "))

if parked_hours <= 0:
    print("Invalid parked duration! Hours must be greater than 0.")
elif vehicle_choice == "1" or vehicle_choice == "bike":
    vehicle_type_name = "Two-Wheeler"
    hourly_rate = 20.0
    maximum_daily_charge = 150.0
    
    base_parking_fee = parked_hours * hourly_rate
    if base_parking_fee > maximum_daily_charge:
        base_parking_fee = maximum_daily_charge
        
    overnight_surcharge = 0.0
    if parked_hours > 12.0:
        overnight_surcharge = 100.0
        
    total_parking_fee = base_parking_fee + overnight_surcharge
    
    print("\n--- Parking Fee Receipt ---")
    print("Vehicle Category   :", vehicle_type_name)
    print("Parked Duration    :", parked_hours, "hours")
    print("Base Parking Charge: Rs.", round(base_parking_fee, 2))
    print("Overnight Surcharge: Rs.", round(overnight_surcharge, 2))
    print("Total Amount Due   : Rs.", round(total_parking_fee, 2))
elif vehicle_choice == "2" or vehicle_choice == "car":
    vehicle_type_name = "Four-Wheeler"
    hourly_rate = 40.0
    maximum_daily_charge = 300.0
    
    base_parking_fee = parked_hours * hourly_rate
    if base_parking_fee > maximum_daily_charge:
        base_parking_fee = maximum_daily_charge
        
    overnight_surcharge = 0.0
    if parked_hours > 12.0:
        overnight_surcharge = 100.0
        
    total_parking_fee = base_parking_fee + overnight_surcharge
    
    print("\n--- Parking Fee Receipt ---")
    print("Vehicle Category   :", vehicle_type_name)
    print("Parked Duration    :", parked_hours, "hours")
    print("Base Parking Charge: Rs.", round(base_parking_fee, 2))
    print("Overnight Surcharge: Rs.", round(overnight_surcharge, 2))
    print("Total Amount Due   : Rs.", round(total_parking_fee, 2))
else:
    print("Invalid vehicle choice! Please select 1 (Two-Wheeler) or 2 (Four-Wheeler).")
