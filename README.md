**Automated SSH Brute Force Attack Detection System**

**Project Overview**

This project is designed to detect SSH brute force attacks on a Linux system by analyzing authentication failure logs. The system monitors failed SSH login attempts, counts repeated failures from the same IP address, and raises an alert when a predefined threshold is exceeded.
The project is developed using open-source tools and Linux native logging mechanisms, making it suitable for SOC and entry-level cybersecurity roles.

**Problem Statement**
SSH services are a common target for brute force attacks where attackers repeatedly attempt to gain unauthorized access by trying multiple username and password combinations. Manual monitoring of system logs is inefficient and error-prone.
There is a need for an automated system that can detect such suspicious behavior in real time and generate alerts.

Objective
-To analyze SSH authentication logs on a Linux system
-To identify repeated failed login attempts from the same IP address
-To detect potential brute force attacks based on a defined threshold
-To generate alerts for security monitoring and audit purposes

**Tools and Technologies Used**

-Operating System: Linux (Parrot OS / Ubuntu)
-Programming Language: Python 3
-Log Source: systemd journal (journalctl)
-Automation Tool: Linux shell utilities
-Libraries:
  -subprocess
  -re (Regular Expressions)
  -collections (defaultdict)
All tools used in this project are free and open-source.

**System Architecture**

-SSH authentication failures are recorded in Linux system logs
-The Python script retrieves today’s SSH failure logs using journalctl
-Log entries are parsed to extract source IP addresses
-Failed attempts are counted per IP address
-An alert is generated if the number of attempts crosses the threshold
-Alerts are displayed on the terminal and logged into a file


**Detection Logic**
-The system reads SSH logs generated on the current day
-It searches for log entries containing “Failed password”
-The IP address following the keyword from is extracted
-A counter tracks failed attempts per IP
-If attempts from an IP exceed the defined threshold, it is flagged as a possible brute force attack

Threshold value used: 3 failed attempts

**Project Structure**
ssh-bruteforce-detector/
│
├── scripts/
│   └── detect_bruteforce.py
│
├── reports/
│   └── alert.log
│
└── README.md


**How to Run the Project**
-Ensure SSH service is running on the system
-Navigate to the project root directory
-Run the script with root privileges:
-sudo python3 scripts/detect_bruteforce.py
-If the threshold is exceeded, an alert will be displayed and logged in reports/alert.log

**Sample Output**
ALERT: Brute force detected from ::1 | Attempts: 5

**Limitations**

-The system detects attacks only after the threshold is crossed
-It is limited to SSH services
-It does not block the attacking IP automatically
-Log analysis is limited to the current day

**Future Scope**

-Automatic IP blocking using firewall rules
-Email or dashboard-based alerting
-Support for additional services like FTP or HTTP
-Integration with SIEM platforms
-Persistent monitoring across reboots

**Conclusion**

This project demonstrates a practical approach to detecting brute force attacks using Linux log analysis and Python scripting. It reflects real-world SOC practices and provides a strong foundation for further security automation.

**Author**
the-cyber-wolf
