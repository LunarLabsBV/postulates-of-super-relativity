import numpy as np
import matplotlib.pyplot as plt

# Values of L from 1 to 10
L_values = np.arange(1, 11)

# Values of the derivative for each L
derivative_values = [
    0.3769942894460652,
    -0.151111504310964,
    0.09479860644227443,
    -0.0015150532909259436,
    0.0015149218565185572,
    -0.007575548754339321,
    -0.009725139642140273,
    -0.02467122830727323,
    -0.009759643375978265,
    -0.11074352593242188
]

# Plot
plt.figure(figsize=(8, 6))
plt.plot(L_values, derivative_values, marker='o', linestyle='-')
plt.title('Derivative of Psi with respect to time')
plt.xlabel('L')
plt.ylabel('Derivative of Psi')
plt.grid(True)
plt.show()
