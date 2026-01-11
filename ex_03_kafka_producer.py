import time
import random
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode()  #convert to JSON and then to bytes
)

while True:
    data = {
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(30, 60), 1)
    }
    producer.send("sensorwerte", data)
    print("Gesendet:", data)
    time.sleep(1)
