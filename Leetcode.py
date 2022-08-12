
import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooLock = threading.Lock()
        self.barLock = threading.Lock()
        self.barLock.acquire()


    def foo(self, printFoo: 'Callable[[str], None]') -> None:

        for i in range(self.n):
            self.fooLock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo('foo')
            self.barLock.release()


    def bar(self, printBar: 'Callable[[str], None]') -> None:

        for i in range(self.n):
            self.barLock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar('bar')
            self.fooLock.release()


def print_name(name:str):
    print(name)

if __name__ == '__main__':

    foobar = FooBar(3)
    foobar.foo(print_name)
    foobar.bar(print_name)

