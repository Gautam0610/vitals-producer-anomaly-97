import os
import time
import random
from kafka import KafkaProducer
from dotenv import load_dotenv

load_dotenv()

output_topic = os.getenv("OUTPUT_TOPIC")
bootstrap_servers = os.getenv("BOOTSTRAP_SERVERS").split(",")
sasl_username = os.getenv("SASL_USERNAME")
sasl_password = os.getenv("SASL_PASSWORD")
security_protocol = os.getenv("SECURITY_PROTOCOL")
sasl_mechanism = os.getenv("SASL_MECHANISM")
interval_ms = int(os.getenv("INTERVAL_MS"))

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    sasl_plain_username=sasl_username,
    sasl_plain_password=sasl_password,
    security_protocol=security_protocol,
    sasl_mechanism=sasl_mechanism,
    api_version=(0, 11, 5),
)


def generate_vitals():
    body_temp = round(random.uniform(36.5, 37.5), 1)  # Normal body temperature
    heart_rate = random.randint(60, 100)  # Normal heart rate
    systolic_pressure = random.randint(110, 130)  # Normal systolic pressure
    diastolic_pressure = random.randint(70, 90)  # Normal diastolic pressure
    breaths_per_minute = random.randint(12, 20)  # Normal breaths per minute
    oxygen_saturation = random.randint(95, 100)  # Normal oxygen saturation
    blood_glucose = random.randint(70, 140)  # Normal blood glucose

    return {
        "body_temp": body_temp,
        "heart_rate": heart_rate,
        "systolic_pressure": systolic_pressure,
        "diastolic_pressure": diastolic_pressure,
        "breaths_per_minute": breaths_per_minute,
        "oxygen_saturation": oxygen_saturation,
        "blood_glucose": blood_glucose,
    }


def generate_anomaly(vitals):
    vitals["heart_rate"] = random.randint(150, 220)  # Extremely high heart rate
    vitals["breaths_per_minute"] = random.randint(30, 50)  # Extremely high breaths per minute
    return vitals


def main():
    while True:
        if random.random() < 0.1:  # 10% chance of generating an anomaly
            vitals = generate_anomaly(generate_vitals())
            print("Generating anomaly")
        else:
            vitals = generate_vitals()
        print(f"Sending vitals: {vitals}")
        producer.send(output_topic, str(vitals).encode("utf-8"))
        producer.flush()
        time.sleep(interval_ms / 1000)


if __name__ == "__main__":
    main()
