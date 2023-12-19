import os
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
import random
import LinkedList
import HashTable
import ABR


def testAddLinkedList(iterations, k):
    times = []
    elements = []
    l = LinkedList.LinkedList()
    for i in range(iterations):
        start = timer()
        for j in range(100):
            l.add(k[(j + i * 10) % len(k)])
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
            l.add(k[(j + i * 10) % len(k)])
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
    for i in range(10):
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
    save_path = os.path.join(os.getcwd(), 'insert_List.png')
    plt.savefig(save_path)
    plt.show()

    # test search
    for i in range(10):
        time, element = testSearchLinkedList(100, k)
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
    save_path = os.path.join(os.getcwd(), 'search_List.png')
    plt.savefig(save_path)
    plt.show()


def testAddHashTable(iterations, k):
    times = []
    elements = []
    h = HashTable.HashTable(len(k))
    for i in range(iterations):
        start = timer()
        for j in range(100):
            h.insert(k[(j + i * 100) % len(k)])
        end = timer()
        times.append((end - start) * 1000)
        elements.append(i * 100)
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
            h.search(k[random.randint(0, iterations * 100 - 1)])
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
    for i in range(10):
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
    save_path = os.path.join(os.getcwd(), 'insert_Hash.png')
    plt.savefig(save_path)
    plt.show()

    # test search
    for i in range(10):
        time, element = testSearchHashTable(100, k)
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
    save_path = os.path.join(os.getcwd(), 'search_Hash.png')
    plt.savefig(save_path)
    plt.show()

def testAddABR(iterations, k):
    times = []
    elements = []
    a = ABR.ABR()
    for i in range(iterations):
        start = timer()
        for j in range(100):
            a.add(k[(j + i * 10) % len(k)])
        end = timer()
        times.append((end - start) * 1000)
        elements.append(i * 10)
    return times, elements

def testSearchABR(iterations, k):
    times = []
    elements = []
    a = ABR.ABR()
    for i in range(iterations):
        for j in range(100):
            a.add(k[(j + i * 10) % len(k)])
        elements.append(j * (i+1))
        start = timer()
        for j in range(10):
            a.search(random.randint(0, 100000))
        end = timer()
        times.append((end - start) * 1000)
    return times, elements

def testABR(k):
    timesAdd = []
    elementsAdd = []
    timesSearch = []
    elementsSearch = []
    avgTimesAdd = []
    avgElementsAdd = []
    avgTimesSearch = []
    avgElementsSearch = []

    # test add
    for i in range(100):
        time, element = testAddABR(100, k)
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
    plt.xlabel('Elementi nell\'albero')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Performance inserimento in albero binario di ricerca')
    #plt.ylim([0, 0.3]) # the y axis is limited to 0.2 milliseconds because the time is too small
    save_path = os.path.join(os.getcwd(), 'insert_ABR.png')
    plt.savefig(save_path)
    plt.show()

    # test search
    for i in range(100):
        time, element = testSearchABR(100, k)
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
    plt.xlabel('Elementi nell albero')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Performance ricerca in albero binario di ricerca')
    plt.ylim([0, 0.3])
    save_path = os.path.join(os.getcwd(), 'search_ABR.png')
    plt.savefig(save_path)
    plt.show()


def testInsertAllStructureOnePlot(k):
    timesAddList = []
    timesAddHash = []
    timesAddABR = []
    elementsAdd = []
    avgTimesAddList = []
    avgTimesAddHash = []
    avgTimesAddABR = []
    avgElementsAdd = []

    # test add
    for i in range(10):
        time, element = testAddLinkedList(100, k)
        timesAddList.append(time)
        elementsAdd.append(element)
    for i in range(len(timesAddList[0])):
        avgTimesAddList.append(0)
        avgElementsAdd.append(0)
        for j in range(len(timesAddList)):
            avgTimesAddList[i] += timesAddList[j][i]
            avgElementsAdd[i] += elementsAdd[j][i]
        avgTimesAddList[i] /= len(timesAddList)
        avgElementsAdd[i] /= len(timesAddList)
    for i in range(10):
        time, element = testAddHashTable(100, k)
        timesAddHash.append(time)
    for i in range(len(timesAddHash[0])):
        avgTimesAddHash.append(0)
        for j in range(len(timesAddHash)):
            avgTimesAddHash[i] += timesAddHash[j][i]
        avgTimesAddHash[i] /= len(timesAddHash)
    for i in range(10):
        time, element = testAddABR(100, k)
        timesAddABR.append(time)
    for i in range(len(timesAddABR[0])):
        avgTimesAddABR.append(0)
        for j in range(len(timesAddABR)):
            avgTimesAddABR[i] += timesAddABR[j][i]
        avgTimesAddABR[i] /= len(timesAddABR)
    plt.plot(avgElementsAdd, avgTimesAddList, label='Lista concatenata')
    plt.plot(avgElementsAdd, avgTimesAddHash, label='Tabella hash')
    plt.plot(avgElementsAdd, avgTimesAddABR, label='Albero binario di ricerca')
    plt.xlabel('Elementi nella struttura')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Performance inserimento in tutte le strutture')
    plt.legend()
    #save_path = os.path.join(os.getcwd(), 'insert_All.png')
    #plt.savefig(save_path)
    plt.show()

def testSearchAllStructureOnePlot(k):
    timesSearchList = []
    timesSearchHash = []
    timesSearchABR = []
    elementsSearch = []
    avgTimesSearchList = []
    avgTimesSearchHash = []
    avgTimesSearchABR = []
    avgElementsSearch = []

    # test search
    for i in range(10):
        time, element = testSearchLinkedList(100, k)
        timesSearchList.append(time)
        elementsSearch.append(element)
    for i in range(len(timesSearchList[0])):
        avgTimesSearchList.append(0)
        avgElementsSearch.append(0)
        for j in range(len(timesSearchList)):
            avgTimesSearchList[i] += timesSearchList[j][i]
            avgElementsSearch[i] += elementsSearch[j][i]
        avgTimesSearchList[i] /= len(timesSearchList)
        avgElementsSearch[i] /= len(timesSearchList)
    for i in range(10):
        time, element = testSearchHashTable(100, k)
        timesSearchHash.append(time)
    for i in range(len(timesSearchHash[0])):
        avgTimesSearchHash.append(0)
        for j in range(len(timesSearchHash)):
            avgTimesSearchHash[i] += timesSearchHash[j][i]
        avgTimesSearchHash[i] /= len(timesSearchHash)
    for i in range(10):
        time, element = testSearchABR(100, k)
        timesSearchABR.append(time)
    for i in range(len(timesSearchABR[0])):
        avgTimesSearchABR.append(0)
        for j in range(len(timesSearchABR)):
            avgTimesSearchABR[i] += timesSearchABR[j][i]
        avgTimesSearchABR[i] /= len(timesSearchABR)
    plt.plot(avgElementsSearch, avgTimesSearchList, label='Lista concatenata')
    plt.plot(avgElementsSearch, avgTimesSearchHash, label='Tabella hash')
    plt.plot(avgElementsSearch, avgTimesSearchABR, label='Albero binario di ricerca')
    plt.xlabel('Elementi nella struttura')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Performance ricerca in tutte le strutture')
    plt.legend()
    #save_path = os.path.join(os.getcwd(), 'search_All.png')
    #plt.savefig(save_path)
    plt.show()



if __name__ == '__main__':
    k = np.random.choice(100000, size=10000, replace=False)
    #testLinkedList(k)
    #testHashTable(k)
    #testABR(k)
    testInsertAllStructureOnePlot(k)
    testSearchAllStructureOnePlot(k)

