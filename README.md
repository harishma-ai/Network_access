# Network Access Control System (ACL Simulator)

A beginner-friendly Python project that simulates network Access Control List (ACL) decisions.
It evaluates simulated traffic against configurable rules using source IP, destination IP,
protocol, and destination port. This is an educational simulator; it does **not** configure
or block traffic on a real network.

## Features
- Source and destination IP matching (supports CIDR networks)
- TCP, UDP, and ICMP protocol matching
- Destination-port matching
- Allow / deny rules with first-match priority
- Default-deny behavior when no rule matches
- JSON-based rules configuration
- Simulated traffic examples and decision logs
- Unit tests

## Requirements
- Python 3.9 or later
- No third-party packages required

## Run on Windows
1. Download/extract the ZIP.
2. Open the project folder in VS Code or File Explorer.
3. Open Command Prompt or PowerShell in this folder.
4. Run:

   ```bash
   python src/main.py
   ```

   If `python` is not recognized, try `py src/main.py`.

## Run tests
```bash
python -m unittest discover -s tests -v
```

## How rule evaluation works
Rules are checked in order from top to bottom. The first matching rule determines
the result. If no rule matches, the simulator denies the request (default deny).

## Sample demo
- Employee workstation `192.168.1.20` to server `192.168.1.100` TCP port `80` → ALLOW
- Employee workstation to server TCP port `22` → DENY
- Guest network `192.168.1.30` to internal server → DENY
- Admin workstation `192.168.1.10` to server TCP port `22` → ALLOW

## Project structure
```text
Network-Access-Control-System/
├── README.md
├── requirements.txt
├── LICENSE
├── src/
│   ├── main.py
│   ├── access_control.py
│   ├── rule_manager.py
│   └── traffic_simulator.py
├── config/
│   └── access_rules.json
├── tests/
│   └── test_access_control.py
├── docs/
│   ├── Project_Report.md
│   ├── Architecture.md
│   ├── Working_Explanation.md
│   └── Test_Cases.md
└── screenshots/
    └── README.md
```

## Technologies
Python, Python standard library (`ipaddress`, `json`, `unittest`), JSON, Git, GitHub.

## Limitations
This project simulates ACL decisions using example traffic. It is not a real firewall,
router configuration, packet capture, or production security tool.
