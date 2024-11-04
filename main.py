import time
import random
from ring_buffer import RingBuffer
from anomaly_detection import detect_anomaly
from classification import classify_vital_sign
from data_generator import generate_vital_sign_data

# Initialize a ring buffer to store the latest data
buffer_size = 50  # Keep the last 50 readings
ring_buffer = RingBuffer(buffer_size)

def monitor_vital_signs():
    while True:
        # Generate example data
        data_point = generate_vital_sign_data()
        
        # Insert into ring buffer
        ring_buffer.insert(data_point)
        
        # Check for anomalies
        if detect_anomaly(ring_buffer):
            print("Anomaly detected:", data_point)
        
        # Classify the current pattern for potential risks
        classification = classify_vital_sign(ring_buffer)
        print("Current Classification:", classification)
        
        # Sleep to simulate real-time data stream
        time.sleep(1)

if __name__ == "__main__":
    monitor_vital_signs()
