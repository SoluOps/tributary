import time
import requests

def measure_endpoint_latency():
    start_time = time.time()
    response = requests.get('http://127.0.0.1:8000/collect')
    end_time = time.time()
    
    latency = (end_time - start_time) * 1000  # Convert to milliseconds
    return latency

# Run multiple times and average
latencies = [measure_endpoint_latency() for _ in range(100)]
avg_latency = sum(latencies) / len(latencies)
print(f"Average latency: {avg_latency:.2f} ms")