import random
from BST import *
from time import time
import matplotlib.pyplot as plt


def populate(n):
    randomList = []
    bstList = BST()

    for i in range(0, n):
        randomList.append(random.randint(0, n))
        bstList.append(random.randint(0, n))
    return (randomList, bstList)


def searchList(list, n):
    if n in list:
        return True
    else:
        return False


if __name__ == "__main__":
    count = 0
    countBST = 0
    nVal = 200000
    t1List = []
    t2List = []

    timeAtStart = time()
    for i in range(1, 10000, 1000):
        (tryList, tryBSTList) = populate(i)

        for n in tryList:
            if searchList(tryList, n) == True:
                count += 1
        timeAtEndTL = time()
        t1List.append(timeAtEndTL - timeAtStart)

        #timeAtStartBST = time()
        for n in range(nVal):
            if tryBSTList.isin(n) == True:
                countBST += 1
        timeAtEndBST = time()
        #print(timeAtEndBST)
        #print(timeAtEndTL)
        t2List.append(timeAtEndBST - timeAtEndTL)

    print("Time difference for searching list: {}".format(timeAtEndTL - timeAtStart))
    print("Time difference for searching BST: {}".format(timeAtEndBST - timeAtEndTL))

    print("Count_list: {}".format(count))
    print("Count_BST: {}".format(countBST))

    plt.plot(range(1, 10000, 1000), t1List, label="List")
    plt.plot(range(1, 10000, 1000), t2List, label="BSTList")
    plt.legend()
    plt.show()



