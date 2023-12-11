import time
import csv
import re
import multiprocessing.pool as pool

#Na nize uvedeny zdrojovy kod v uloze 12.7 nesahat !
data = []
with open('./12.6/dluznici.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)  # skip the headers
    for row in reader:
        data.append(row)

def rok_narozeni_z_rc(rodne_cislo):
    rok_narozeni = int(rodne_cislo[0:2])
    if (rok_narozeni > 21):
        rok_narozeni += 1900
    else:
        rok_narozeni += 2000
    return rok_narozeni

def prumerny_dluh_dle_roku_narozeni(rok_od,rok_do,label):
    if rok_od < 0:
        raise Exception('Nevalidni rok od')
    if rok_do < 0:
        raise Exception('Nevalidni rok do')

    soucet = 0
    pocet = 0
    prumerny_dluh = 0
    for i in range(0,len(data)):
        if not re.search("^[0-9]{1,}$", data[i][0]):
            raise Exception('Nevalidni ID')
        if not re.search("^[0-9]{6}\/[0-9]{4}$", data[i][1]):
            raise Exception('Nevalidni rodne cislo')
        if not re.search("^\-?[0-9]{1,}$", data[i][2]):
            raise Exception('Nevalidni dluh')

        if(rok_od <= rok_narozeni_z_rc(data[i][1]) < rok_do):
            pocet += 1
            soucet += int(data[i][2])

    if(pocet > 0):
        prumerny_dluh = round(soucet/pocet)

    print("Prumerny dluh pro "+label+" je "+str(prumerny_dluh)+" CZK")

#Na vyse uvedeny zdrojovy kod v uloze 12.7 nesahat !

if __name__ == "__main__":

    __THREADCOUNT__ = 5

    start = time.time()

    threadPool = pool.ThreadPool(__THREADCOUNT__)
   
    threadPool.apply_async(prumerny_dluh_dle_roku_narozeni,args=(1991,2001,"dvacatniky"))
    threadPool.apply_async(prumerny_dluh_dle_roku_narozeni,args=(1981,1991,"tricatniky"))
    threadPool.apply_async(prumerny_dluh_dle_roku_narozeni,args=(1971,1981,"ctyricatniky"))
    threadPool.apply_async(prumerny_dluh_dle_roku_narozeni,args=(1961,1971,"padesatniky"))
    threadPool.apply_async(prumerny_dluh_dle_roku_narozeni,args=(1951,1961,"sedesatniky"))

    threadPool.close()
    threadPool.join()

    end = time.time()
    print("Vypocet trval {:.6f} sec.".format((end - start)))