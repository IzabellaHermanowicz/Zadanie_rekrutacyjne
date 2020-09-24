from threading import Thread

def numer1():
    import time
    n=0
    while n<10:
        print ('to ja: numer 1')
        time.sleep(2)
        n+=2

def numer2():
    import time
    n=0
    while n<10:
        print ('to ja: numer 2')
        time.sleep(1)
        n+=1

if __name__ == '__main__':
    Thread(target = numer1).start()
    Thread(target = numer2).start()
