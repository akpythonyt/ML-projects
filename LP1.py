from pulp import *
# declare your variables
A = LpVariable("A", 100, 200)   # 100 <= A <= 200
B = LpVariable("B", 80, 170) # 80 <= B <= 170
# defines the problem: optimization - Maximization
prob = LpProblem("problem", LpMaximize)


# defines the constraints
prob += A + B >=200
prob += A<=200
prob += A>=100
prob += B>=80
prob += B<=170


# defines the objective function to maximize
prob += 5000*B- 2000*A 


# solve the problem
status = prob.solve()
print('printing status of the LP problem: ', LpStatus[status])


# print the results A = 100, B = 170
print('Value of model A car: ', value(A))
print('Value of model B car: ', value(B))
print('the optimal solution or say maximum profit: $', value(prob.objective))