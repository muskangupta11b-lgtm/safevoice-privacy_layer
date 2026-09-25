from network import NetworkMonitor
import time

monitor = NetworkMonitor()

print("Starting network monitoring...")
monitor.start()

# Simulate Privacy Layer execution
time.sleep(2)

network = monitor.stop()

print("\n------ Network Test ------")
print("Local Processing :", network.is_local)
print("Bytes Before     :", network.bytes_before)
print("Bytes After      :", network.bytes_after)
print("Bytes Sent       :", network.bytes_sent)