from time import sleep
from threading import Thread
from queue import Queue

def producent(queue):
    print('Producent zacal')
    for pismeno in ["a","h","o","j","s","v","e","t","e"]:
        queue.join()

        while True:
            queue.put(pismeno,True)
            print("Producent vlozil do fronty pismeno : {}".format(pismeno))
            break

    queue.put(-1) #Vlozeni None znamena ukonceni
    print('Producent skoncil')


def konzument(queue):
    print('Konzument zacal')
    while True:
         
        pismeno = queue.get(True)
        if pismeno == -1: #Pokud je to None, znamena to ukonceni
            break

        print("Konzument nacetl : {}".format(pismeno))
        sleep(1)
        if queue.qsize() == 0:
            for i in range(queue.unfinished_tasks):
                queue.task_done()
            
    print('Konzument skoncil')


if __name__ == "__main__":
    queue = Queue(3)
    queue.put("A") 
    queue.put("B")
    queue.put("C")

    konzument = Thread(target=konzument, args=(queue,))
    producent = Thread(target=producent, args=(queue,))

    konzument.start()
    producent.start()

    producent.join()
    konzument.join()