from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Train a basic decision tree classifier with simulated data
# Features: mean, variance, latest value
# Label: 0 (normal) or 1 (risk)

# Example training data (to be improved with real data)
train_data = np.array([
    [70, 10, 72],  # Normal example
    [110, 15, 115],  # Risk example
])
train_labels = np.array([0, 1])  # 0 = normal, 1 = risk

classifier = DecisionTreeClassifier()
classifier.fit(train_data, train_labels)

def classify_vital_sign(ring_buffer):
    data = ring_buffer.get_data()
    values = [d['value'] for d in data if d is not None]
    
    if len(values) < 2:
        return "Not enough data"

    # Calculate features
    mean_value = np.mean(values)
    variance_value = np.var(values)
    latest_value = values[-1]
    
    # Prepare the feature vector for classification
    feature_vector = np.array([[mean_value, variance_value, latest_value]])
    prediction = classifier.predict(feature_vector)
    
    return "Risk" if prediction[0] == 1 else "Normal"
