from pulp import *
import pandas as pd
import matplotlib.pyplot as plt

# Function to get valid user input for weight and goal
def get_valid_input():
    while True:
        try:
            weight_lb = float(input("Enter your weight in pounds: "))
            if weight_lb <= 0:
                raise ValueError("Weight must be a positive number.")
            
            goal = input("Enter your goal (lose, maintain, gain): ").strip().lower()
            if goal not in {"lose", "maintain", "gain"}:
                raise ValueError("Goal must be 'lose', 'maintain', or 'gain'.")
            
            return weight_lb, goal
        
        except ValueError as e:
            print(f"Input error: {e}")
            print("Please try again.\n")

# Function to calculate macros based on weight and goal
def macro_calc(weight_lb, goal):
    if goal == "lose":
        calories = 13 * weight_lb
        protein_g = (0.40 * calories) / 4
        carbs_g = (0.40 * calories) / 4
        fat_g = (0.20 * calories) / 9
        return calories,protein_g,carbs_g,fat_g
    
    elif goal == "maintain":
        calories = 15 * weight_lb
        protein_g = (0.30 * calories) / 4
        carbs_g = (0.40 * calories) / 4
        fat_g = (0.30 * calories) / 9
        return calories,protein_g,carbs_g,fat_g
    
    elif goal == "gain":
        calories = 17 * weight_lb
        protein_g = (0.30 * calories) / 4
        carbs_g = (0.45 * calories) / 4
        fat_g = (0.25 * calories) / 9
        return calories,protein_g,carbs_g,fat_g

# Now call it
weight_lb, goal = get_valid_input()

calories,protein_g, carbs_g, fat_g = macro_calc(weight_lb, goal)

prob = LpProblem("MacroTracker", LpMinimize)

# Define the decision variables
# Lp Variable(name, lowBound=0, upBound=None, cat='Continuous')

x1 = LpVariable("Chicken", 0, None, LpInteger)
x2 = LpVariable("Rice", 0, None, LpInteger)
x3 = LpVariable("Broccoli", 0, None, LpInteger)
x4 = LpVariable("Avocado", 0, None, LpInteger)

# Define the objective function
prob += 0.008 * x1 + 0.003 * x2 + 0.005 * x3 + 0.015 * x4, "Total Minimum Cost"

# Define the constraints
prob += 0.31 * x1 + 0.026 * x2 + 0.028 * x3 + 0.02 * x4>= protein_g, "ProteinMin"
prob += 0.035 * x1 + 0.002 * x2 + 0.003 * x3 + 0.15 * x4 >= fat_g, "FatMin"
prob += 0.0 * x1 + 0.28 * x2 + 0.07 * x3 + 0.09 * x4 >= carbs_g, "CarbsMin"

total_mass = x1 + x2 + x3 + x4

prob += x1 + x2 + x3 <= weight_lb * 20, "MaxFoodMass"  # 20g per lb body weight

prob += x1 >= 0.25 * total_mass, "ProteinShare"
prob += x2 >= 0.25 * total_mass, "CarbShare"
prob += x3 + x4>= 0.50 * total_mass, "VeggieShare"

prob.writeLP("MacroTracker.lp")

# Solving the problem
prob.solve()
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", str(v.varValue)+"g")

# Display the total cost and macro distribution
print(f"Total Cost = ${value(prob.objective):.2f}")
print("The Plate Distribution is: 1/2 Veggies, 1/4 Protein, 1/4 Carbs")
print(f"Calories: {calories:.2f}, Protein: {protein_g:.2f}g, Carbs: {carbs_g:.2f}g, Fat: {fat_g:.2f}g")

# Plotting the macro distribution
labels = ['Protein', 'Carbs', 'Fats']
values = [protein_g, carbs_g, fat_g]
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.show()

#test
