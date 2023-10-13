
import time
from threading import Thread,Lock
import queue


## programme largement inspiré de multi_threaded.py sur cette page https://realpython.com/python-gil/#:~:text=The%20Python%20Global%20Interpreter%20Lock%20or%20GIL%2C%20in%20simple%20words,at%20any%20point%20in%20time.
## il est simple et permet de tester clairement 
COUNT = 500000

def countdown(id,COUNT):
    print(id)
    global COUNTG
    COUNTG=COUNT
    while COUNTG>0:
        COUNTG-=1
        

t1 = Thread(target=countdown, args=(1,COUNT,))
t2 = Thread(target=countdown, args=(2,COUNT,))


start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(COUNTG)

print("variable partagée en écriture prends tant de temps: "+ str(end-start))