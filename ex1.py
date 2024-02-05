import pulp as plp


# Create a Linear Programming problem with the name "Beverage_production" and the objective of maximizing production.
model = plp.LpProblem(name="Beverage_production", sense=plp.LpMaximize)

# Define decision variables for the production of lemonade (A) and fruit juice (B).
A = plp.LpVariable(name="A", lowBound=0, cat='Integer')
B = plp.LpVariable(name="B", lowBound=0, cat='Integer')

# Set the objective function to maximize the total production of lemonade and fruit juice.
model += A + B, 'Production'

# material constraints
model += 2 * A + B <= 100, 'Water'
model += A <= 50, 'Sugar'
model += A <= 30, 'Lemon juice'
model += 2 * B <= 40, 'Fruit pree'

# Solve the linear programming problem.
model.solve()

# Display the optimal production quantities and the total production value.
print("Lemonade production А:", A.varValue)
print("Fruit juice production B:", B.varValue)
print(f"Total production = {plp.value(model.objective)}")
