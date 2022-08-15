import threading
from time import sleep


def sek(t: int):
    for i in range(1, t + 1):
        sleep(1)
        print(f' left  {i}  sec')


t1 = threading.Thread(target=sek(4),)
t2 = threading.Thread(target=sek(4),)
t3 = threading.Thread(target=sek(4),)
t4 = threading.Thread(target=sek(4),)
t5 = threading.Thread(target=sek(4),)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

