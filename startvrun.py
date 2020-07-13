import threading

def function1():
    for x in range(10):
        print("ONE")

def function2():
    for x in range(10):
        print("TWO")

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.run()
t2.run()

 
