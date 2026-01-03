import subprocess
import re
from collections import defaultdict

# ===== CONFIG =====
THRESHOLD = 3
ALERT_LOG_FILE = "reports/alert.log"

# ==================

def get_ssh_logs():
    """
    Get today's failed SSH login attempts (raw, uncompressed)
    """
    cmd = "journalctl --since today -o cat | grep 'Failed password'"
    result = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout.splitlines()


def detect_failed_logins(logs):
    """
    Extract IP addresses from failed SSH attempts
    """
    ip_count = defaultdict(int)
    pattern = re.compile(r"from\s+([^\s]+)", re.IGNORECASE)

    for line in logs:
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            ip_count[ip] += 1

    return ip_count


def main():
    logs = get_ssh_logs()
    failed_ips = detect_failed_logins(logs)

    if not failed_ips:
        print("[INFO] No failed SSH attempts detected today")
        return

    for ip, count in failed_ips.items():
        if count >= THRESHOLD:
            alert_msg = f"Brute force detected from {ip} | Attempts: {count}"

            print(f"ALERT: {alert_msg}")

            with open(ALERT_LOG_FILE, "a") as f:
                f.write(alert_msg + "\n")


if __name__ == "__main__":
    main()
