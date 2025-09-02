import time
import sys

victim_name = "The Victim"

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

slow_print("Initializing system breach...\n",0.1)
time.sleep(1)

for i in range(0, 101):
    sys.stdout.write(f"\rHacking {victim_name}'s personal files... {i}% complete")
    sys.stdout.flush()
    time.sleep(0.2)

slow_print("\nAccess granted!\n", 0.125)

time.sleep(2)
slow_print(f"Retrieving confidential information on {victim_name}...\n", 0.06)
time.sleep(1)

funny_facts = [
    "System breached, device hacked successfully."
]

for fact in funny_facts:
    slow_print(fact, 0.09)
    time.sleep(1)

for i in range(0, 103,4):
    sys.stdout.write(f"\rWaiting - {i} %")
    sys.stdout.flush()
    time.sleep(0.15)
print()

slow_print("\nFinished. Logging out...", 0.1)
slow_print(" ", 5)
