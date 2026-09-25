from dataclasses import dataclass
import psutil
from config import NETWORK_THRESHOLD
@dataclass
class NetworkResult:
    is_local: bool
    bytes_before: int
    bytes_after: int
    bytes_sent: int
class NetworkMonitor:

    def __init__(self):
        self.bytes_before = 0
        self.bytes_after = 0
    def start(self):
        self.bytes_before = psutil.net_io_counters().bytes_sent
    def stop(self):
        self.bytes_after = psutil.net_io_counters().bytes_sent
        bytes_sent = self.bytes_after - self.bytes_before
        if NETWORK_THRESHOLD == 0:
            is_local = bytes_sent <= NETWORK_THRESHOLD

        return NetworkResult(
    is_local=is_local,
    bytes_before=self.bytes_before,
    bytes_after=self.bytes_after,
    bytes_sent=bytes_sent)