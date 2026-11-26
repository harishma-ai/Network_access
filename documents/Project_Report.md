# Project Report: Network Access Control System (ACL Simulator)

## Abstract
This project is a Python-based educational simulator that demonstrates the logic of network Access Control Lists. It checks simulated traffic against ordered rules using source/destination IP addresses, protocol, and destination port. The result is an Allow or Deny decision with the matching rule and explanation.

## Problem statement
Networks need policies that restrict which devices can communicate with selected services. ACLs can express these policies, but beginners may find it difficult to understand how rules are matched and how rule order affects decisions. This simulator makes that process visible without requiring networking hardware.

## Objectives
- Demonstrate ACL rule matching.
- Practice IP addresses, CIDR notation, protocols, and ports.
- Explain rule order and default-deny policy.
- Provide repeatable sample scenarios and tests.

## Methodology
1. Load rules from JSON.
2. Read each simulated traffic scenario.
3. Compare source and destination IP, protocol, and port with rules in order.
4. Stop at the first matching rule.
5. Return the action and reason; if nothing matches, apply the default action.

## Results
The included scenarios show administrator SSH access permitted, employee HTTP access permitted, employee SSH access denied, guest access denied, and unlisted traffic denied by the default policy.

## Conclusion
The simulator provides a simple way to learn ACL decision logic. It is not connected to a real network and does not enforce security policies on actual devices.
