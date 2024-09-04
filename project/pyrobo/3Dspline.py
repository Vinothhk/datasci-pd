import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Define the 3D points (Point A, Point B, and Point C)
point_A = np.array([1, 2, 3])  # Starting point (x1, y1, z1)
point_B = np.array([4, 6, 8])  # Intermediate point (x2, y2, z2)
point_C = np.array([7, 10, 5]) # Ending point (x3, y3, z3)

# Create an array for the parameter t (e.g., time or position)
t = np.array([0, 0.5, 1])  # 0 corresponds to Point A, 0.5 to Point B, 1 to Point C

# Interpolate for x, y, and z separately using cubic splines
cs_x = CubicSpline(t, [point_A[0], point_B[0], point_C[0]])
cs_y = CubicSpline(t, [point_A[1], point_B[1], point_C[1]])
cs_z = CubicSpline(t, [point_A[2], point_B[2], point_C[2]])

# Generate intermediate points along the spline (e.g., 100 points)
t_fine = np.linspace(0, 1, 1000)
x_spline = cs_x(t_fine)
y_spline = cs_y(t_fine)
z_spline = cs_z(t_fine)

# Combine x, y, and z into a single array of waypoints
waypoints = np.vstack((x_spline, y_spline, z_spline)).T

# Print the waypoints
print("Spline Interpolated Waypoints:")
print(waypoints)

# Plot the interpolated curve in 3D space
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original points
ax.scatter(point_A[0], point_A[1], point_A[2], color='red', label='Point A')
ax.scatter(point_B[0], point_B[1], point_B[2], color='green', label='Point B')
ax.scatter(point_C[0], point_C[1], point_C[2], color='blue', label='Point C')

# Plot the spline interpolated curve
ax.plot(x_spline, y_spline, z_spline, label='Spline Curve', color='purple')

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
plt.show()
