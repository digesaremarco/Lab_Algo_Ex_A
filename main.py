from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
import random
import LinkedList
import HashTable


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
    for i in range(300):
        time, element = testAddLinkedList(100, k)
        timesAdd.append(time)
        elementsAdd.append(element)
    for i in range(len(timesAdd[0])):
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
    for i in range(300):
        time, element = testSearchLinkedList(10, k)
        timesSearch.append(time)
        elementsSearch.append(element)
    for i in range(len(timesSearch[0])):
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


def testAddHashTable(iterations, k):
    times = []
    elements = []
    h = HashTable.HashTable(len(k))
    for i in range(iterations):
        start = timer()
        for j in range(10):
            h.insert(k[(j + i * 10) % len(k)])
        end = timer()
        times.append((end - start) * 1000)
        elements.append(i * 10)
    return times, elements


def testSearchHashTable(iterations, k):
    times = []
    elements = []
    h = HashTable.HashTable(len(k))
    for i in range(iterations):
        for j in range(100):
            h.insert(k[(j + i * 10) % len(k)])
        elements.append(j * (i+1))
        start = timer()
        for j in range(10):
            h.search(random.randint(0, 1000))
        end = timer()
        times.append((end - start) * 1000)
    return times, elements


def testHashTable(k):
    timesAdd = []
    elementsAdd = []
    timesSearch = []
    elementsSearch = []
    avgTimesAdd = []
    avgElementsAdd = []
    avgTimesSearch = []
    avgElementsSearch = []

    # test add
    for i in range(300):
        time, element = testAddHashTable(100, k)
        timesAdd.append(time)
        elementsAdd.append(element)
    for i in range(len(timesAdd[0])):
        avgTimesAdd.append(0)
        avgElementsAdd.append(0)
        for j in range(len(timesAdd)):
            avgTimesAdd[i] += timesAdd[j][i]
            avgElementsAdd[i] += elementsAdd[j][i]
        avgTimesAdd[i] /= len(timesAdd)
        avgElementsAdd[i] /= len(timesAdd)
    plt.plot(avgElementsAdd, avgTimesAdd)
    plt.xlabel('Elementi nella tabella hash')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Performance inserimento in tabella hash')
    plt.show()

    # test search
    for i in range(100):
        time, element = testSearchHashTable(10, k)
        timesSearch.append(time)
        elementsSearch.append(element)
    for i in range(len(timesSearch[0])):
        avgTimesSearch.append(0)
        avgElementsSearch.append(0)
        for j in range(len(timesSearch)):
            avgTimesSearch[i] += timesSearch[j][i]
            avgElementsSearch[i] += elementsSearch[j][i]
        avgTimesSearch[i] /= len(timesSearch)
        avgElementsSearch[i] /= len(timesSearch)
    plt.plot(avgElementsSearch, avgTimesSearch)
    plt.xlabel('Elementi nella tabella hash')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Performance ricerca in tabella hash')
    plt.show()


if __name__ == '__main__':
    print('PyCharm')
    h = np.random.randint(0, 100000, 1000)  # generate 3000 random numbers between 0 and 1000
    #testLinkedList(k)
    k = np.random.choice(10000, size=1000, replace=False)
    testHashTable(k)

