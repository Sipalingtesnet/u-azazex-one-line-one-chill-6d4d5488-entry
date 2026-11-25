import os
import hashlib

line = "As the autopilot confirmed we had cleared Earth's atmosphere, the exterior camera showed my childhood bedroom window still tapping against the hull."
os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(line)

with open("/output/entry.txt", "rb") as f:
    b1 = f.read()

h1 = hashlib.sha256(b1).hexdigest()

with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(line)

with open("/output/entry.txt", "rb") as f:
    b2 = f.read()

h2 = hashlib.sha256(b2).hexdigest()

print("Run 1 SHA256:", h1)
print("Run 2 SHA256:", h2)
print("Match:", h1 == h2)
print("No trailing newline:", b1[-1:] != b'\n')
print("Code points count:", len(line))
