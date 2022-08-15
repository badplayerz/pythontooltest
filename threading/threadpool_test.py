"""
@author: zlh
@file: threadpool_test.py
@time: 2022/8/15 16:33
@desc: threadpool
"""

from concurrent.futures import ThreadPoolExecutor
import time

def doThread(page):
    time.sleep(2)
    print("thread page is ", page)
    return page

def main():

    with ThreadPoolExecutor(max_workers=4) as threadpool: # 初始化线程池，线程数为4
        print("threading start....")
        excutor = threadpool.map(doThread, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        for data in excutor:
            print(f"result {data} ...")
        threadpool.shutdown()

if __name__ == '__main__':
    main()
