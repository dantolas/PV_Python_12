import multiprocessing
import time
nakupniSeznam = ["Mleko","Maslo","Rohlik"]

def vypisNakupniSeznam():
    global nakupniSeznam
    for predmet in nakupniSeznam:
        print(predmet)
        time.sleep(1)


if __name__ == "__main__":
    print("ZACATEK PROGRAMU")
    p1 = multiprocessing.Process(target=vypisNakupniSeznam)
    p1.start()
    p1.join()
    print("KONEC PROGRAMU")
