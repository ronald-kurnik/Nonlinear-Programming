from gekko import GEKKO

m = GEKKO(remote=False) # Use remote=False to solve locally if you prefer
m.options.IMODE = 3 # Steady-state optimization

# Initialize variables with initial values and bounds
x1 = m.Var(value=1, lb=1, ub=5)
x2 = m.Var(value=5, lb=1, ub=5)
x3 = m.Var(value=5, lb=1, ub=5)
x4 = m.Var(value=1, lb=1, ub=5)

# Define constraints (equations)
m.Equation(x1 * x2 * x3 * x4 >= 25)
m.Equation(x1**2 + x2**2 + x3**2 + x4**2 == 40)

# Define objective function (Minimize by default)
m.Obj(x1 * x4 * (x1 + x2 + x3) + x3)

# Solve
m.solve(disp=False)

# Print results
print("\n--- Optimization Results ---")
print(f"x1: {x1.value[0]:.4f}")
print(f"x2: {x2.value[0]:.4f}")
print(f"x3: {x3.value[0]:.4f}")
print(f"x4: {x4.value[0]:.4f}")
print(f"Objective: {m.options.objfcnval:.4f}")