# Working Explanation

## What is an ACL?
An Access Control List is a set of ordered rules that determine whether traffic or access requests should be permitted or denied.

## Fields used in this simulation
- Source IP: address of the device sending the simulated request.
- Destination IP: address of the target device.
- Protocol: TCP, UDP, or ICMP (the demo rules use TCP).
- Destination port: identifies a service, such as HTTP port 80 or SSH port 22.
- Action: ALLOW or DENY.

## Rule order
Rules are evaluated top to bottom. The first matching rule wins. If no rule matches, the default policy is DENY.

## Example
An employee at 192.168.1.20 requests the server at 192.168.1.100 on TCP port 80. The HTTP allow rule matches, so the result is ALLOW. If the same employee requests TCP port 22, the SSH deny rule matches, so the result is DENY.

## Use cases of ACLs
- Restricting access to selected services.
- Separating guest and employee network permissions.
- Limiting management access to authorized devices.
- Understanding firewall and router filtering policies.

## Important limitation
This code only evaluates example traffic data. It does not inspect network packets or change the configuration of a router, switch, firewall, or computer.
