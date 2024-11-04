# Healthcare Monitoring and Alerting System

## Overview

The Healthcare Monitoring and Alerting System leverages wearable devices and IoT sensors to continuously track vital signs and alert healthcare providers in the event of abnormalities. This system collects, processes, and analyzes data in real-time to detect unusual patterns, providing timely alerts for potential health risks.

## Features

- Continuous monitoring of vital signs (e.g., heart rate).
- Real-time anomaly detection using Z-score.
- Classification of vital signs using decision trees.
- Pre-populated initial data to enhance demonstration and usability.

## Data Structures and Algorithms Used

- **Time Series Database (TSDB)**: Simulated using a ring buffer to efficiently store and retrieve continuous streams of time-stamped data.
- **Ring Buffers**: Used to maintain the most recent data for quick processing and analysis.
- **Anomaly Detection Algorithms**: Implemented using Z-score to flag unusual values in real-time.
- **Decision Trees**: Applied for classification based on vital sign patterns to predict potential risks.

## Time Complexity

- **TSDB Retrievals**: O(log N) for indexed retrievals, where N is the number of entries.
- **Ring Buffer Operations**: O(1) for insertions and removals.
- **Anomaly Detection (e.g., Z-score)**: O(N) for calculating Z-scores, where N is the sample size.

## Setup Instructions

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation Steps

1. **Clone the Repository**

   Open your terminal and run:

   ```bash
   git clone https://github.com/hanushrajputh/healthcare_monitoring_alerting_system.git
   cd healthcare_monitoring_alerting_system
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**

   Create and activate a virtual environment:

   ```bash
   pip install virtualenv
   virtualenv venv
   source venv/bin/activate
   ```

3. **Install Required Packages**

   Install the necessary packages:

   ```bash
   pip install numpy scikit-learn
   ```

4. **Running the Application**

   Start the monitoring system:

   ```bash
   python main.py
   ```

   Observe the output in the terminal, which will display anomaly detection alerts and classification results for vital signs.

   To stop the application, press Ctrl + C.

## Code Structure

- `main.py`: Main entry point of the application that simulates data generation and monitors vital signs.
- `ring_buffer.py`: Implements a ring buffer to store the latest data readings.
- `anomaly_detection.py`: Contains the logic for detecting anomalies using Z-score.
- `classification.py`: Implements decision tree classification based on vital sign patterns.
- `data_generator.py`: Simulates sensor data for testing the system.

## Future Work

- Integrate real-time data from actual wearable devices.
- Enhance anomaly detection algorithms with more advanced methods.
- Implement a web interface for easier monitoring and alerts.
