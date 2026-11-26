# Test Cases

| Test | Input scenario | Expected result |
|---|---|---|
| TC-01 | Admin IP to server, TCP 22 | ALLOW |
| TC-02 | Employee IP to server, TCP 80 | ALLOW |
| TC-03 | Employee IP to server, TCP 22 | DENY |
| TC-04 | Guest IP to internal server | DENY |
| TC-05 | Unlisted source IP to server, TCP 443 | DENY (default) |
| TC-06 | Source in matching CIDR rule | ALLOW |

Run the tests from the project root using `python -m unittest discover -s tests -v`.
