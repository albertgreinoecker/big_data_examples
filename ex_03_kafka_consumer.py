from kafka import KafkaConsumer
import json
from datetime import datetime

consumer = KafkaConsumer(
    "sensorwerte",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",               # Start reading at the latest message, options: "earliest" or "latest"
    value_deserializer=lambda v: json.loads(v.decode()) #convert from bytes to JSON
)

for msg in consumer:
    print(
        "Empfangen:\n"
        f"  Topic:      {msg.topic}\n"
        f"  Partition:  {msg.partition}\n"
        f"  Offset:     {msg.offset}\n"
        f"  Timestamp:  {datetime.fromtimestamp(msg.timestamp / 1000)}\n"
        f"  Key:        {msg.key}\n"
        f"  Headers:    {msg.headers}\n"
        f"  Value:      {msg.value}\n"
        "----------------------------------------"
    )
