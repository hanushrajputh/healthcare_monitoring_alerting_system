import random

def generate_vital_sign_data():
    # Generate synthetic heart rate data between 60 and 120 bpm
    heart_rate = random.randint(60, 120)
    return {'value': heart_rate}
