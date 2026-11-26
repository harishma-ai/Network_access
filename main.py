"""Command-line demo for the Network Access Control System."""
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from access_control import AccessControlEngine
from rule_manager import load_rules
from traffic_simulator import SAMPLE_TRAFFIC


def main():
    config_file = PROJECT_ROOT / "config" / "access_rules.json"
    rules, default_action = load_rules(config_file)
    engine = AccessControlEngine(rules, default_action)

    print("=" * 72)
    print(" NETWORK ACCESS CONTROL SYSTEM - ACL SIMULATOR")
    print("=" * 72)
    print("Educational simulation: decisions are displayed; real traffic is not changed.")
    print()

    for traffic in SAMPLE_TRAFFIC:
        result = engine.evaluate(traffic)
        print(f"Scenario : {traffic['label']}")
        print(f"Source   : {traffic['source_ip']}")
        print(f"Target   : {traffic['destination_ip']}")
        print(f"Protocol : {traffic['protocol']} / Port {traffic.get('destination_port', 'N/A')}")
        print(f"Decision : {result['action']}")
        print(f"Rule     : {result['rule_id']}")
        print(f"Reason   : {result['reason']}")
        print("-" * 72)

    print("Demo complete. Edit config/access_rules.json to customize the example rules.")


if __name__ == "__main__":
    main()
