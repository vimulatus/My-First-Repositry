import threading

event = threading.Event()

def function():
    print("Waiting for event...\n")
    event.wait()
    print("Continuing!")

t = threading.Thread(target = function)
t.start()

x = input("Trigger event?")

if x in ("y", "Y", "yes", "Yes", "YES"):
    event.set()

