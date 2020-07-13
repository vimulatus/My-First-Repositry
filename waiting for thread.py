import threading

def function():
    for x in range(10):
        print("HELLO WORLD!")

t1 = threading.Thread(target = function)
t1.run()

print("This is the end!")
