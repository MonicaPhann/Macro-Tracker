\* MacroTracker *\
Minimize
Total_Minimum_Cost: 0.015 Avocado + 0.005 Broccoli + 0.008 Chicken
 + 0.003 Rice
Subject To
CarbShare: - 0.25 Avocado - 0.25 Broccoli - 0.25 Chicken + 0.75 Rice >= 0
CarbsMin: 0.09 Avocado + 0.07 Broccoli + 0.28 Rice >= 150
FatMin: 0.15 Avocado + 0.003 Broccoli + 0.035 Chicken + 0.002 Rice >= 50
MaxFoodMass: Broccoli + Chicken + Rice <= 2000
ProteinMin: 0.02 Avocado + 0.028 Broccoli + 0.31 Chicken + 0.026 Rice >= 112.5
ProteinShare: - 0.25 Avocado - 0.25 Broccoli + 0.75 Chicken - 0.25 Rice >= 0
VeggieShare: 0.5 Avocado + 0.5 Broccoli - 0.5 Chicken - 0.5 Rice >= 0
Bounds
 0 <= Avocado
 0 <= Broccoli
 0 <= Chicken
 0 <= Rice
Generals
Avocado
Broccoli
Chicken
Rice
End
