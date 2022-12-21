import os
from threading import Thread
from time import sleep
import sys


def run_client(script):
    os.system(script)


p_count = int(sys.argv[1])
script = "python client.py"
all_p = []
for _ in range(p_count):
    p = Thread(target=run_client, args=(script,))
    all_p.append(p)
for i in range(p_count):
    all_p[i].start()
    print(f"Started P{i+1}")
    sleep(0.3)
