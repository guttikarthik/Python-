# Case Study 18: Fuel Consumption and Route Comparison

distance = float(input("Enter trip distance (km): "))
fuel_price = float(input("Enter fuel price per liter (Rs.): "))
mileage_vehicle_a = float(input("Mileage of Vehicle A (km/liter): "))
mileage_vehicle_b = float(input("Mileage of Vehicle B (km/liter): "))

if distance <= 0 or fuel_price <= 0 or mileage_vehicle_a <= 0 or mileage_vehicle_b <= 0:
    print("Invalid input! All values must be positive and greater than zero.")
else:
    fuel_needed_vehicle_a = distance / mileage_vehicle_a
    total_cost_vehicle_a = fuel_needed_vehicle_a * fuel_price
    
    fuel_needed_vehicle_b = distance / mileage_vehicle_b
    total_cost_vehicle_b = fuel_needed_vehicle_b * fuel_price
    
    print("\n--- Route Comparison ---")
    print("Vehicle A - Fuel needed:", round(fuel_needed_vehicle_a, 2), "liters | Trip cost: Rs.", round(total_cost_vehicle_a, 2))
    print("Vehicle B - Fuel needed:", round(fuel_needed_vehicle_b, 2), "liters | Trip cost: Rs.", round(total_cost_vehicle_b, 2))
    
    if total_cost_vehicle_a < total_cost_vehicle_b:
        cost_difference = total_cost_vehicle_b - total_cost_vehicle_a
        print("Recommendation: Choose Vehicle A (Saves Rs.", round(cost_difference, 2), ")")
    elif total_cost_vehicle_b < total_cost_vehicle_a:
        cost_difference = total_cost_vehicle_a - total_cost_vehicle_b
        print("Recommendation: Choose Vehicle B (Saves Rs.", round(cost_difference, 2), ")")
    else:
        print("Both vehicles have identical fuel expenses.")
