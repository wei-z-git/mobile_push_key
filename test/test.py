from threading import Thread
from time import sleep


def async1(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


@async1
def A():
    sleep(10)
    print("sleep 10")
    print("a function")


def B():
    print("b function")
    

if __name__ == '__main__':
    A()
    B()
