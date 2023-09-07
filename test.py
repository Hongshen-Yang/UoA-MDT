import matplotlib.pyplot as plt
import random
import datetime
import time

# Initialize empty data lists
timestamps = []
closing_prices = []

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()

# Function to update the line chart
def update_chart(i):
    # Generate random closing price data
    now = datetime.datetime.now()
    timestamps.append(now)
    closing_prices.append(random.uniform(100, 200))
    
    # Limit the data to show only the last 10 data points
    if len(timestamps) > 10:
        timestamps.pop(0)
        closing_prices.pop(0)

    ax.clear()
    ax.plot(timestamps, closing_prices, label='Closing Price')
    
    ax.set_xlabel('Time')
    ax.set_ylabel('Closing Price')
    ax.legend()

# Continuously update the chart every second
while True:
    update_chart(0)
    plt.pause(1)  # Pause for 1 second before updating again
