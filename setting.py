server = "127.0.0.1"
port = 5555

with open("hostIP.txt", "r") as f:
    server = f.read().strip()
