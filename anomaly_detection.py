import numpy as np

def detect_anomaly(ring_buffer, threshold=2.5):
    data = ring_buffer.get_data()
    values = [d['value'] for d in data if d is not None]
    if len(values) < 2:
        return False  # Not enough data to detect anomalies

    mean = np.mean(values)
    std_dev = np.std(values)
    
    # Check the latest value for anomaly
    latest_value = values[-1]
    z_score = (latest_value - mean) / std_dev if std_dev > 0 else 0
    
    return abs(z_score) > threshold
