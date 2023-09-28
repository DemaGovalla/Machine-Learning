# # import pandas as pd
# # import numpy as np
# # import matplotlib.pyplot as plt

# # # Generate random capacitive data
# # sensor1_data = np.random.rand(100) * 10  # Generating 100 random data points between 0 and 10
# # sensor2_data = np.random.rand(100) * 10  # Generating 100 random data points between 0 and 10

# # # Create a DataFrame
# # df = pd.DataFrame({'Sensor1_Capacitance': sensor1_data, 'Sensor2_Capacitance': sensor2_data})

# # # Create a time array for the FFT
# # time = np.arange(0, len(sensor1_data), 1)

# # # Calculate FFT for both sensors
# # fft_sensor1 = np.fft.fft(df['Sensor1_Capacitance'])
# # fft_sensor2 = np.fft.fft(df['Sensor2_Capacitance'])

# # # Create subplots
# # fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# # # Plot capacitive data
# # ax1.plot(df['Sensor1_Capacitance'], label='Sensor 1 Capacitance', color='blue')
# # ax1.plot(df['Sensor2_Capacitance'], label='Sensor 2 Capacitance', color='green')
# # ax1.set_xlabel('Data Point')
# # ax1.set_ylabel('Capacitance')
# # ax1.set_title('Sensor Capacitance Data')
# # ax1.legend()

# # # Plot FFT
# # ax2.plot(np.abs(fft_sensor1), label='Sensor 1 FFT', color='blue')
# # ax2.plot(np.abs(fft_sensor2), label='Sensor 2 FFT', color='green')
# # ax2.set_xlabel('Frequency')
# # ax2.set_ylabel('Amplitude')
# # ax2.set_title('Sensor FFT')
# # ax2.legend()

# # plt.tight_layout()
# # plt.show()


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Generate time array
# time = np.arange(0, 1, .01)  # 10 kHz sampling for 1 second

# # Generate sine waves
# sensor1_data = np.sin(2 * np.pi * 5000 * time)  # 5 kHz sine wave
# sensor2_data = np.sin(2 * np.pi * 10000 * time)  # 10 kHz sine wave

# # Create a DataFrame
# df = pd.DataFrame({'Sensor1_Capacitance': sensor1_data, 'Sensor2_Capacitance': sensor2_data})

# # Calculate FFT for both sensors
# fft_sensor1 = np.fft.fft(df['Sensor1_Capacitance'])
# fft_sensor2 = np.fft.fft(df['Sensor2_Capacitance'])

# # Create subplots
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# # Plot capacitive data
# ax1.plot(df['Sensor1_Capacitance'], label='Sensor 1 Capacitance', color='blue')
# ax1.plot(df['Sensor2_Capacitance'], label='Sensor 2 Capacitance', color='green')
# ax1.set_xlabel('Data Point')
# ax1.set_ylabel('Capacitance')
# ax1.set_title('Sensor Capacitance Data')
# ax1.legend()

# # Plot FFT
# ax2.plot(np.abs(fft_sensor1), label='Sensor 1 FFT', color='blue')
# ax2.plot(np.abs(fft_sensor2), label='Sensor 2 FFT', color='green')
# ax2.set_xlabel('Frequency')
# ax2.set_ylabel('Amplitude')
# ax2.set_title('Sensor FFT')
# ax2.legend()

# plt.tight_layout()
# plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate time array
time = np.arange(0, 1, 0.0001)  # 10 kHz sampling for 1 second

# Generate sine waves
sensor1_data = np.sin(2 * np.pi * 5000 * time)  # 5 kHz sine wave
sensor2_data = np.sin(2 * np.pi * 10000 * time)  # 10 kHz sine wave

# Create a DataFrame
df = pd.DataFrame({'Sensor1_Capacitance': sensor1_data, 'Sensor2_Capacitance': sensor2_data})

# Calculate FFT for both sensors
fft_sensor1 = np.fft.fft(df['Sensor1_Capacitance'])
fft_sensor2 = np.fft.fft(df['Sensor2_Capacitance'])

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot capacitive data
ax1.plot(df['Sensor1_Capacitance'], label='Sensor 1 Capacitance', color='blue')
ax1.plot(df['Sensor2_Capacitance'], label='Sensor 2 Capacitance', color='green')
ax1.set_xlabel('Data Point')
ax1.set_ylabel('Capacitance')
ax1.set_title('Sensor Capacitance Data')
ax1.legend()

# Plot FFT
ax2.plot(np.abs(fft_sensor1), label='Sensor 1 FFT', color='blue')
ax2.plot(np.abs(fft_sensor2), label='Sensor 2 FFT', color='green')
ax2.set_xlabel('Frequency')
ax2.set_ylabel('Amplitude')
ax2.set_title('Sensor FFT')
ax2.legend()

plt.tight_layout()
plt.show()
