# Example of nonlinear programming using GEKKO
### Optimization Problem Formulation

The optimization problem is defined by the following variables, constraints, and objective function:

```math
\begin{aligned}
&\text{Variables and Bounds:} \\
&1 \le x_1 \le 5 \\
&1 \le x_2 \le 5 \\
&1 \le x_3 \le 5 \\
&1 \le x_4 \le 5 \\
\\
&\text{Constraints:} \\
&x_1 x_2 x_3 x_4 \ge 25 \\
&x_1^2 + x_2^2 + x_3^2 + x_4^2 = 40 \\
\\
&\text{Objective Function (Minimize):} \\
\min \quad &x_1 x_4 (x_1 + x_2 + x_3) + x_3
\end{aligned}
```
### Results
--- Optimization Results ---  
x1: 1.0000  
x2: 4.7430  
x3: 3.8212  
x4: 1.3794  
Objective: 17.0140
