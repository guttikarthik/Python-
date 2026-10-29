# Case Study 25: Progressive Water Tariff Analysis

consumer_id = input("Enter Consumer ID: ")
water_usage_units = float(input("Enter monthly water usage in kiloliters (kL): "))

if water_usage_units < 0:
    print("Invalid usage amount! Water usage cannot be negative.")
else:
    # Simple Slabs:
    # First 30 kL : Rs. 5 per kL
    # Above 30 kL : Rs. 10 per kL
    if water_usage_units <= 30:
        water_charge = water_usage_units * 5
    else:
        water_charge = (30 * 5) + ((water_usage_units - 30) * 10)
        
    meter_rent = 40.0
    total_bill_amount = water_charge + meter_rent
    
    print("\n--- Water Bill Statement ---")
    print("Consumer ID       :", consumer_id)
    print("Water Consumption :", water_usage_units, "kL")
    print("Water Charge      : Rs.", round(water_charge, 2))
    print("Fixed Meter Rent  : Rs.", meter_rent)
    print("Total Bill Amount : Rs.", round(total_bill_amount, 2))
    
    if water_usage_units > 50:
        print("Alert: High water consumption detected! Please conserve water.")
