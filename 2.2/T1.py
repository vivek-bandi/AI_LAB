# Function to clean IoT sensor data
def clean_sensor_data(sensor_values):
    """
    Removes invalid negative sensor readings
    """
    return [value for value in sensor_values if value >= 0]


# Main program
if __name__ == "__main__":
    # Sample sensor data
    sensor_data = [25, -4, 18, 0, -12, 33, 7]

    print("Original Sensor Data:", sensor_data)

    # Clean the data
    cleaned_data = clean_sensor_data(sensor_data)

    print("Cleaned Sensor Data:", cleaned_data)