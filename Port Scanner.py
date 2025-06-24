import socket

target = input("Enter IP address: ")
for port in range(20, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if s.connect_ex((target, port)) == 0:
        print(f"Port {port} is open")
    s.close()
