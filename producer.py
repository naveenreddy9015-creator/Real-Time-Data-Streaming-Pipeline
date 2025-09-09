import time
import random
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    event = {
        "order_id": random.randint(1000, 9999),
        "sku": f"SKU{random.randint(1,10)}",
        "quantity": random.randint(1,5),
        "timestamp": time.time()
    }
    producer.send('orders', event)
    print(f"Produced: {event}")
    time.sleep(1)
