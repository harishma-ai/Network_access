# Architecture

```text
                 +-------------------------+
                 |  Sample Traffic Inputs  |
                 | source / target / proto |
                 | port                   |
                 +------------+------------+
                              |
                              v
                 +-------------------------+
                 |     main.py (CLI)       |
                 +------------+------------+
                              |
                +-------------+--------------+
                |                            |
                v                            v
       +------------------+        +---------------------+
       | rule_manager.py  |        | traffic_simulator  |
       | loads JSON rules |        | provides scenarios |
       +---------+--------+        +----------+----------+
                 |                            |
                 +-------------+--------------+
                               v
                    +------------------------+
                    | access_control.py      |
                    | checks ordered rules   |
                    +-----------+------------+
                                |
                                v
                    +------------------------+
                    | ALLOW / DENY + reason  |
                    +------------------------+
```

## Components
- **main.py:** Runs the demonstration and prints decisions.
- **rule_manager.py:** Loads rules and default policy from JSON.
- **access_rules.json:** Stores editable ACL policy.
- **access_control.py:** Matching and decision engine.
- **traffic_simulator.py:** Contains sample requests.
- **test_access_control.py:** Automated tests for expected decisions.
