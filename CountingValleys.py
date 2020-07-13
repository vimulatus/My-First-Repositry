# Status: Not Working

import threading

event = threading.Event()

def str_to_lst(str):
    lst = []
    for i in str:
        lst.append(i)
    return lst

count = 0

def countvalley():
    global count
    event.wait()
    count += 1
    event.clear()

def heightcalc(ar):
    height = 0
    for i in ar:
        if i == 'U':
            height += 1
        else:
            height -= 1
        if height == -1:
            event.set()
    
thread = threading.Thread(target=countvalley, daemon = True)
n = int(input("Enter number of steps: "))
ar = map(str_to_lst,input("Enter sequence of steps:\n"))
print("Number of valleys: {}".format(count/2))
