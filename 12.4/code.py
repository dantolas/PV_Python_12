import multiprocessing
import time

class VypisCiselProcess(multiprocessing.Process):


    def __init__(self, od, do):
        multiprocessing.Process.__init__(self)
        self.od = od
        self.do = do


    def vypis_cisel(self,od, do):
        for i in range(od,do):
            print(i)
            time.sleep(1)
        print(do)
    
    def run(self):

        self.vypis_cisel(self.od,self.do)



if __name__ == "__main__":
    print("ZACATEK PROGRAMU")
    p1 = VypisCiselProcess(1,5)
    p1.start()
    p1.join()
    print("KONEC PROGRAMU")