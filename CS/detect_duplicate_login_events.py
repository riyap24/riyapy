login_ips = [
    "192.168.1.1",
    "10.0.0.2",
    "192.168.1.1",
    "172.16.0.5",
    "10.0.0.2"
]

seen = set()

for ip in login_ips:
    if ip in seen:
        print("Repeated login event:", ip)
    else:
        seen.add(ip)