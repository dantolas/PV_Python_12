import threading
from threading import Lock


class BankovniUcet:
    def __init__(self, zustatek):
        self.zustatek = zustatek
    def vloz_mince(self,pocetKusu, mince,lock):
        lock.acquire()
        for i in range(0, pocetKusu):
            self.zustatek += mince

        lock.release()
    def __str__(self):
        return "Bankovni ucet se zustatkem: {:d} CZK".format(self.zustatek)


lock = Lock()
mujUcet = BankovniUcet(0)

t1 = threading.Thread(target=mujUcet.vloz_mince, args=(100000,1,lock))
t2 = threading.Thread(target=mujUcet.vloz_mince, args=(1000000,2,lock))
t3 = threading.Thread(target=mujUcet.vloz_mince, args=(100000,5,lock))
t4 = threading.Thread(target=mujUcet.vloz_mince, args=(1000000,10,lock))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print(mujUcet)