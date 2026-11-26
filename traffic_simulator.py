"""Sample traffic used to demonstrate ACL decisions."""
SAMPLE_TRAFFIC = [
    {
        "label": "Admin SSH access",
        "source_ip": "192.168.1.10",
        "destination_ip": "192.168.1.100",
        "protocol": "TCP",
        "destination_port": 22,
    },
    {
        "label": "Employee web access",
        "source_ip": "192.168.1.20",
        "destination_ip": "192.168.1.100",
        "protocol": "TCP",
        "destination_port": 80,
    },
    {
        "label": "Employee SSH attempt",
        "source_ip": "192.168.1.20",
        "destination_ip": "192.168.1.100",
        "protocol": "TCP",
        "destination_port": 22,
    },
    {
        "label": "Guest to internal server",
        "source_ip": "192.168.1.30",
        "destination_ip": "192.168.1.100",
        "protocol": "TCP",
        "destination_port": 80,
    },
    {
        "label": "Unlisted device",
        "source_ip": "192.168.1.50",
        "destination_ip": "192.168.1.100",
        "protocol": "TCP",
        "destination_port": 443,
    },
]
