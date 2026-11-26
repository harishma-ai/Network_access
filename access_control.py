"""ACL evaluation engine for simulated network traffic."""
from ipaddress import ip_address, ip_network


class AccessControlEngine:
    """Evaluate simulated traffic against ordered ACL rules."""

    def __init__(self, rules, default_action="DENY"):
        self.rules = rules
        self.default_action = default_action.upper()

    @staticmethod
    def _ip_matches(value, rule_value):
        if rule_value in (None, "*", "ANY"):
            return True
        address = ip_address(value)
        network = ip_network(rule_value, strict=False)
        return address in network

    @staticmethod
    def _protocol_matches(value, rule_value):
        return rule_value in (None, "*", "ANY") or value.upper() == rule_value.upper()

    @staticmethod
    def _port_matches(value, rule_value):
        if rule_value in (None, "*", "ANY"):
            return True
        if isinstance(rule_value, list):
            return value in rule_value
        if isinstance(rule_value, str) and "-" in rule_value:
            low, high = map(int, rule_value.split("-", 1))
            return low <= value <= high
        return value == int(rule_value)

    def evaluate(self, traffic):
        """Return a decision dictionary for a traffic request."""
        source = str(ip_address(traffic["source_ip"]))
        destination = str(ip_address(traffic["destination_ip"]))
        protocol = traffic["protocol"].upper()
        port = traffic.get("destination_port")

        for rule in self.rules:
            matched = (
                self._ip_matches(source, rule.get("source_ip", "*"))
                and self._ip_matches(destination, rule.get("destination_ip", "*"))
                and self._protocol_matches(protocol, rule.get("protocol", "*"))
                and (port is None or self._port_matches(port, rule.get("destination_port", "*")))
            )
            if matched:
                return {
                    "action": rule["action"].upper(),
                    "rule_id": rule.get("id", "unnamed"),
                    "reason": rule.get("description", "Matched configured ACL rule"),
                }

        return {
            "action": self.default_action,
            "rule_id": "DEFAULT",
            "reason": "No ACL rule matched; default policy applied",
        }
