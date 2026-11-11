def get_positive_number(prompt_text, is_float=True):
    """
    Validates numeric inputs to ensure positive float or int entries.
    Returns: float or int
    """
    while True:
        try:
            val = float(input(prompt_text)) if is_float else int(input(prompt_text))
            if val < 0:
                print("Value cannot be negative. Try again.")
            else:
                return val
        except ValueError:
            print("Invalid entry! Please enter a valid number.")

def calculate_energy_kwh(power_watts, hours_per_day):
    """
    Calculates daily kWh consumed by a single machine.
    Formula: kWh = (Power in Watts * Hours) / 1000
    Returns: float
    """
    daily_kwh = (power_watts * hours_per_day) / 1000.0
    return daily_kwh

def assess_carbon_emission(total_kwh_monthly):
    """
    [Twist Feature] Estimates carbon emissions based on grid emission factor (~0.45 kg CO2/kWh).
    Returns: float
    """
    emission_factor = 0.45 
    return total_kwh_monthly * emission_factor

def main():
    print("==============================================")
    print("   WORKSHOP ENERGY & CARBON COST ESTIMATOR    ")
    print("==============================================")

    tariff_rate = get_positive_number("Enter your electricity tariff rate (Cost per kWh in ₦/kWh): ")
    monthly_budget = get_positive_number("Enter your total monthly energy budget (₦): ")
    num_machines = int(get_positive_number("How many machines are in the workshop? ", is_float=False))

    # Lists to hold machine data
    machine_names = []
    daily_kwh_list = []
    monthly_cost_list = []

    # Loop to capture details for each machine
    for i in range(1, num_machines + 1):
        print(f"\n--- Machine #{i} details ---")
        name = input("Enter machine name (e.g., Lathe, CNC Mill, Soldering Station): ").strip()
        watts = get_positive_number("Power rating in Watts (W): ")
        hours = get_positive_number("Operating hours per day (0-24 hrs): ")
        
        # Validate operating hours limits
        while hours > 24:
            print("Error: Operating hours cannot exceed 24 hours per day!")
            hours = get_positive_number("Operating hours per day (0-24 hrs): ")

        daily_kwh = calculate_energy_kwh(watts, hours)
        monthly_cost = daily_kwh * 30.0 * tariff_rate

        # Store in lists
        machine_names.append(name)
        daily_kwh_list.append(daily_kwh)
        monthly_cost_list.append(monthly_cost)

    # Calculate Totals
    total_daily_kwh = sum(daily_kwh_list)
    total_monthly_kwh = total_daily_kwh * 30.0  # Assuming 30 days per month
    total_daily_cost = total_daily_kwh * tariff_rate
    total_monthly_cost = sum(monthly_cost_list)

    # Output Breakdown
    print("\n==============================================")
    print("            WORKSHOP ENERGY REPORT            ")
    print("==============================================")
    print(f"{'Machine Name':<20} | {'Daily Energy (kWh)':<18} | {'Monthly Cost (₦)':<15}")
    print("-" * 60)
    
    for i in range(len(machine_names)):
        print(f"{machine_names[i]:<20} | {daily_kwh_list[i]:<18.2f} | ₦{monthly_cost_list[i]:<15.2f}")

    print("-" * 60)
    print(f"Total Daily Energy Consumption  : {total_daily_kwh:.2f} kWh")
    print(f"Total Monthly Energy Consumption: {total_monthly_kwh:.2f} kWh")
    print(f"Estimated Daily Operating Cost  : ₦{total_daily_cost:,.2f}")
    print(f"Estimated Monthly Operating Cost: ₦{total_monthly_cost:,.2f}")
    
    # Budget Evaluation Section
    print("\n---------------- [BUDGET ANALYSIS] ----------------")
    print(f"Allocated Monthly Budget       : ₦{monthly_budget:,.2f}")
    
    budget_variance = monthly_budget - total_monthly_cost
    
    if budget_variance >= 0:
        print(f"Status                           : UNDER BUDGET ✅")
        print(f"Remaining Surplus                : ₦{budget_variance:,.2f}")
    else:
        overspend = abs(budget_variance)
        percentage_exceeded = (overspend / monthly_budget) * 100
        print(f"Status                           : OVER BUDGET 🚨")
        print(f"Amount Exceeded                  : ₦{overspend:,.2f} ({percentage_exceeded:.1f}% over budget)")

    # Twist Feature: Highest Energy Consumer Identification & Carbon Impact
    print("\n---------------- [TWIST FEATURES] ----------------")
    max_kwh = max(daily_kwh_list)
    highest_consumer_index = daily_kwh_list.index(max_kwh)
    highest_consumer_name = machine_names[highest_consumer_index]
    
    co2_emissions = assess_carbon_emission(total_monthly_kwh)

    print(f" Top Energy Consumer: [{highest_consumer_name}] using {max_kwh:.2f} kWh/day")
    print(f" Carbon Footprint Estimator: Workshop emits ~{co2_emissions:.2f} kg of CO2 monthly.")

    if total_monthly_cost > monthly_budget:
        print("\n Energy Efficiency & Budget Tip: Budget limit exceeded! Consider lowering daily operating hours for high-wattage equipment like the " + f"[{highest_consumer_name}].")
    elif total_monthly_kwh > 500:
        print("\n Energy Efficiency Tip: High energy consumption detected! Consider scheduling heavy machinery operations off-peak.")
    else:
        print("\n Energy Efficiency Tip: Workshop energy consumption and costs are within budget and efficient operational bounds.")

if __name__ == "__main__":
    main()
