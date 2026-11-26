import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from access_control import AccessControlEngine
from rule_manager import load_rules


class AccessControlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rules, default_action = load_rules(ROOT / "config" / "access_rules.json")
        cls.engine = AccessControlEngine(rules, default_action)

    def decide(self, source, destination, protocol, port):
        return self.engine.evaluate({
            "source_ip": source,
            "destination_ip": destination,
            "protocol": protocol,
            "destination_port": port,
        })["action"]

    def test_admin_ssh_allowed(self):
        self.assertEqual(self.decide("192.168.1.10", "192.168.1.100", "TCP", 22), "ALLOW")

    def test_employee_http_allowed(self):
        self.assertEqual(self.decide("192.168.1.20", "192.168.1.100", "TCP", 80), "ALLOW")

    def test_employee_ssh_denied(self):
        self.assertEqual(self.decide("192.168.1.20", "192.168.1.100", "TCP", 22), "DENY")

    def test_guest_access_denied(self):
        self.assertEqual(self.decide("192.168.1.30", "192.168.1.100", "TCP", 80), "DENY")

    def test_unknown_device_default_denied(self):
        self.assertEqual(self.decide("192.168.1.50", "192.168.1.100", "TCP", 443), "DENY")

    def test_cidr_matching(self):
        rules = [{
            "id": "NET",
            "source_ip": "192.168.2.0/24",
            "destination_ip": "*",
            "protocol": "*",
            "destination_port": "*",
            "action": "ALLOW",
        }]
        engine = AccessControlEngine(rules, "DENY")
        result = engine.evaluate({
            "source_ip": "192.168.2.22",
            "destination_ip": "10.0.0.5",
            "protocol": "UDP",
            "destination_port": 53,
        })
        self.assertEqual(result["action"], "ALLOW")


if __name__ == "__main__":
    unittest.main()
