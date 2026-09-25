from datetime import datetime
from config import PROCESSING_MODE, DEFAULT_SHA, LOG_FILE

def log_event(validation_result, decision, reason, sha=DEFAULT_SHA):
    """
    Logs every privacy event into privacy_log.txt.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as log_file:
        log_file.write("=" * 50 + "\n")
        log_file.write(f"Timestamp      : {timestamp}\n")
        log_file.write(f"Validation     : {validation_result}\n")
        log_file.write(f"Decision       : {decision}\n")
        log_file.write(f"Processing     : {PROCESSING_MODE}\n")
        log_file.write(f"Reason         : {reason}\n")
        log_file.write(f"SHA-256        : {sha}\n")
        log_file.write("=" * 50 + "\n\n")