import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

SENSOR_IDS = ['sensor_1', 'sensor_2', 'sensor_3']

while True:
    sensor_data = {
        "sensor_id": random.choice(SENSOR_IDS),
        "timestamp": int(time.time()),
        "temperature": round(random.uniform(20.0, 40.0), 2),
        "humidity": round(random.uniform(30.0, 90.0), 2)
    }
    producer.send("sensor-data", value=sensor_data)
    print("Sent:", sensor_data)
    time.sleep(1)
