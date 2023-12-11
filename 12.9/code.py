import csv
import os
import time
import hashlib
import multiprocessing as mp

#Na nize uvedeny zdrojovy kod v uloze 12.6 nesahat !
def hledej(od, do, hash_rc):
    i = 0
    with open('./12.6/dluznici.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader, None)  #preskoci prvni radek s hlavickou
        print("Searching through:("+str(od)+","+str(do)+" for "+hash_rc)
        for row in reader:
            if i > od and i < do and hashlib.sha384(row[1].encode()).hexdigest() == hash_rc:
                return "Nalezen zaznam na radku {} pro rodne cislo {} s dluhem {} CZK.".format(row[0],row[1], row[2])
                #print("Nalezen zaznam na radku {} pro rodne cislo {} s dluhem {} CZK.".format(row[0],row[1], row[2]))
                
            i = i+1
#Na vyse uvedeny zdrojovy kod v uloze 12.6 nesahat !


if __name__ == "__main__":

    print(os.getcwd())

    __PROCESSCOUNT__ = 5

    hash_hledaneho_rc = "5275a2bd25897f396e5f1de8b1ede4fe94d960b20619c772a3b4eccd04430afdabc44e5d388f175aa72428e009ff927c"
    startTime = time.time()
    search_range = 3_000_000 / __PROCESSCOUNT__
    processPool = mp.Pool(__PROCESSCOUNT__)
    result = "Empty"
    start = 0
    end = start + search_range
    for i in range(__PROCESSCOUNT__):
        
        results = [processPool.apply_async(hledej,args=(start,end,hash_hledaneho_rc))]

        start = end
        end = end + search_range
    
    processPool.close()
    processPool.join()
    endTime = time.time()
    results = [result.get() for result in results]
    print(f'{results}')  # -> ['abc', 'xyz']
    print("Vypocet trval {:.6f} sec.".format((endTime - startTime)))