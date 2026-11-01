blocked_ips = {
    "192.168.1.10",
    "10.0.0.25",
    "172.16.0.5"
}

ip = input("Enter IP address: ")

if ip in blocked_ips:
    print("Access Denied: IP Blocked")
else:
    print("Access Allowed")