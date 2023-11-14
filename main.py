from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
import random
import LinkedList


def testAddLinkedList(iterations, k):
    times = []
    elements = []
    l = LinkedList.LinkedList()
    for i in range(iterations):
        start = timer()
        for j in range(10):
            l.add(k[(j + i * 50) % 1000])
        end = timer()
        times.append((end - start) * 1000)
        elements.append(l.size())
    return times, elements

def testSearchLinkedList(iterations, k):
    times = []
    elements = []
    l = LinkedList.LinkedList()
    for i in range(iterations):
        for j in range(100):
            l.add(k[(j + i * 50) % 1000])
        start = timer()
        for j in range(10):
            l.search(random.randint(0, 1000000))
        end = timer()
        times.append((end - start) * 1000)
        elements.append(l.size())
    return times, elements

def testLinkedList(k):
    timesAdd = []
    elementsAdd = []
    timesSearch = []
    elementsSearch = []
    avgTimesAdd = []
    avgElementsAdd = []
    avgTimesSearch = []
    avgElementsSearch = []

    # test add
    for i in range (300):
        time, element = testAddLinkedList(100, k)
        timesAdd.append(time)
        elementsAdd.append(element)
    for i in range(len(timesAdd[0])): # calculate the average time and the average number of elements for each iteration
        avgTimesAdd.append(0)
        avgElementsAdd.append(0)
        for j in range(len(timesAdd)):
            avgTimesAdd[i] += timesAdd[j][i]
            avgElementsAdd[i] += elementsAdd[j][i]
        avgTimesAdd[i] /= len(timesAdd)
        avgElementsAdd[i] /= len(timesAdd)
    plt.plot(avgElementsAdd, avgTimesAdd)
    plt.xlabel('Elementi nella lista')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Performance inserimento in lista concatenata')
    plt.show()

    # test search
    for i in range (10):
        time, element = testSearchLinkedList(10, k)
        timesSearch.append(time)
        elementsSearch.append(element)
    for i in range(len(timesSearch[0])): # calculate the average time and the average number of elements for each iteration
        avgTimesSearch.append(0)
        avgElementsSearch.append(0)
        for j in range(len(timesSearch)):
            avgTimesSearch[i] += timesSearch[j][i]
            avgElementsSearch[i] += elementsSearch[j][i]
        avgTimesSearch[i] /= len(timesSearch)
        avgElementsSearch[i] /= len(timesSearch)
    plt.plot(avgElementsSearch, avgTimesSearch)
    plt.xlabel('Elementi nella lista')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Performance ricerca in lista concatenata')
    plt.show()


if __name__ == '__main__':
    print('PyCharm')
    k = np.random.randint(0, 1000000, 1000)  # generate 1000 random numbers between 0 and 1000000
    testLinkedList(k)
