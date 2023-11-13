from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
import random
import LinkedList


def testAddLinkedList(iterations, l, k):
    times = []
    elements = []
    for i in range(iterations):
        #sum = 0
        start = timer()
        for j in range(50):
            l.add(k[(j)])
        end = timer()
            #sum += (end - start) * 1000  # convert seconds to milliseconds
        #average_time = sum / 20
        times.append((end-start)*1000)
        elements.append(l.size())
    plt.plot(elements, times)
    plt.xlabel('Elementi nella lista')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Performance del metodo add')
    plt.show()


if __name__ == '__main__':
    print('PyCharm')
    k = np.random.randint(0, 1000000, 1000) # generate 1000 random numbers between 0 and 1000000
    l = LinkedList.LinkedList() # create an empty list
    testAddLinkedList(2000, l, k)

