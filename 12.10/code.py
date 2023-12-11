import threading
import multiprocessing.pool as pool

class BankovniUcet:
    def __init__(self, zustatek):
        self.zustatek = zustatek
    def vloz_mince(self,pocetKusu, mince):
        for i in range(0, pocetKusu):
            self.zustatek += mince
    def __str__(self):
        return "Bankovni ucet se zustatkem: {:d} CZK".format(self.zustatek)

mujUcet = BankovniUcet(0)



__THREADCOUNT__ = 5


threadPool = pool.ThreadPool(__THREADCOUNT__)

threadPool.apply_async(mujUcet.vloz_mince, args=(1000,10))
threadPool.apply_async(mujUcet.vloz_mince, args=(1000,2))
threadPool.apply_async(mujUcet.vloz_mince, args=(1000,5))
threadPool.apply_async(mujUcet.vloz_mince, args=(1000,1))

threadPool.close()
threadPool.join()
print(mujUcet)