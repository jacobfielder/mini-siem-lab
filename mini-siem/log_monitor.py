# log_monitor.py
from alert_engine import send_slack_alert
import re

# tracking failed attempts
failed_attempts = {}
THRESHOLD = 5

with open('test_logs/auth.log', 'r') as log_file:
    for line in log_file:
        if "Failed password" in line:
            # Try to match a pattern with optional "invalid user"
            match = re.search(r'Failed password for (invalid user )?(\w+) from ([\d.]+) port (\d+)', line)
            if match:
                username = match.group(2)
                ip_address = match.group(3)
                port = match.group(4)
                print(f"[ALERT] Failed login attempt → User: {username}, IP: {ip_address}, Port: {port}")

		# failed login logic
                failed_attempts[ip_address] = failed_attempts.get(ip_address, 0) + 1


                if failed_attempts[ip_address] == THRESHOLD:
                   print(f'ALERT!!!: {ip_address} has {THRESHOLD} failed login attempts!')
                   send_slack_alert(ip_address, failed_attempts[ip_address])
