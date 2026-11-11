# Anthony_workshop_energy_cost_estimator
Workshop Energy Cost & Carbon Estimator
What it does
This program calculates the daily and monthly energy consumption (in kWh) and operating costs for various machines in a mechatronics workshop. It uses custom functions to handle user inputs, perform calculations, and format financial figures.
How to run it
Install Python 3, then run:
python energy_estimator.py

Sample output
==============================================   WORKSHOP ENERGY & CARBON COST ESTIMATOR    ==============================================Enter your electricity tariff rate (Cost per kWh in ₦/kWh): 120How many machines are in the workshop? 2--- Machine #1 details ---Enter machine name: CNC LathePower rating in Watts (W): 1500Operating hours per day (0-24 hrs): 8--- Machine #2 details ---Enter machine name: Soldering StationPower rating in Watts (W): 60Operating hours per day (0-24 hrs): 5==============================================            WORKSHOP ENERGY REPORT            ==============================================Machine Name         | Daily Energy (kWh) | Monthly Cost (₦)------------------------------------------------------------CNC Lathe            | 12.00              | ₦43200.00      Soldering Station    | 0.30               | ₦1080.00       ------------------------------------------------------------Total Daily Energy Consumption  : 12.30 kWhTotal Monthly Energy Consumption: 369.00 kWhEstimated Daily Operating Cost  : ₦1,476.00Estimated Monthly Operating Cost: ₦44,280.00---------------- [TWIST FEATURES] ----------------Top Energy Consumer: [CNC Lathe] using 12.00 kWh/dayCarbon Footprint Estimator: Workshop emits ~166.05 kg of CO2 monthly.

My own twist
I added a top energy consumer identification feature to pinpoint the highest power-draining machine, along with an environmental carbon footprint calculator that estimates total monthly CO_2 emissions.
What I learned
I learned how to manage multiple related data points using lists, calculate cumulative totals inside loops, and apply formatted string literals for clean tabular output.
Author
Ajibolade Olaniyi, ND2 Mechatronics Engineering, YabaTech.
