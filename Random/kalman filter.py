import numpy as np
import matplotlib.pyplot as plt

# Define the system parameters
A = 1  # State transition matrix (constant)
H = 1  # Measurement matrix (constant)
Q = 0.01  # Process noise covariance (constant)
R = 1  # Measurement noise covariance (constant)

# Generate noisy measurements (simulated sensor data)
np.random.seed(0)  # For reproducibility
true_state = np.linspace(0, 20, 200)  # True state (e.g., position)
measurements = true_state + np.random.normal(0, np.sqrt(R), 200)  # Add measurement noise

# Initialize Kalman Filter variables
x_hat = 0  # Initial state estimate
P = 1  # Initial estimation error covariance

# Lists to store filter estimates
x_hat_list = []
P_list = []

# Kalman Filter loop
for z in measurements:
    # Prediction step
    x_hat_minus = A * x_hat
    P_minus = A**2 * P + Q

    # Update step (Kalman Gain calculation)
    K = P_minus * H / (H**2 * P_minus + R)

    # Correction step
    x_hat = x_hat_minus + K * (z - H * x_hat_minus)
    P = (1 - K * H) * P_minus

    # Store filter estimates
    x_hat_list.append(x_hat)
    P_list.append(P)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(true_state, label='True State', color='blue')
plt.plot(measurements, label='Measurements', color='red', alpha=0.7)
plt.plot(x_hat_list, label='Kalman Filter Estimate', color='green')
plt.fill_between(range(len(x_hat_list)), np.array(x_hat_list) - np.sqrt(P_list), np.array(x_hat_list) + np.sqrt(P_list), color='green', alpha=0.3)
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Kalman Filter Example')
plt.legend()
plt.show()
