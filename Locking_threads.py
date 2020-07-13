import threading, time

x = 8192

def halve():
    global x, lock
    while (x > 1):
        x /= 2
        print(x)
        time.sleep(0.5)
    print("END!")

def double():
    global x, lock
    while (x < 16384):
        x *= 2
        print(x)
        time.sleep(0.5)
    print("END!")

t1 = threading.Thread(target = halve)
t2 = threading.Thread(target = double)

t1.run()
t2.run()
