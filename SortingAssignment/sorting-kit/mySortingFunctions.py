# Name: Will Christie
# Email: william.christie@colorado.edu
# SUID: 810-91-5676
#
# By submitting this file as my own work, I declare that this
# code has been written on my own with no unauthorized help. I agree to the
# CU Honor Code. I am also aware that plagiarizing code may result in
# a failing grade for this class.
from __future__ import print_function
import sys
import random
import time
import numpy as np
import matplotlib.pyplot as plt

# --------- Insertion Sort -------------
# Implementation of getPosition
# Helper function for insertionSort
def getPosition(rList, elt):
    # Find the position where element occurs in the list
    #
    for (i,e) in enumerate(rList):
        if (e >= elt):
            return i
    return len(rList)

# Implementation of Insertion Sort 
def insertionSort(lst):
    n = len(lst)
    retList = []
    for i in lst:
        pos = getPosition(retList, i)
        retList.insert(pos, i)
    return retList

#------ Merge Sort --------------
def mergeSort(lst):
    if len(lst) > 1:
        # partition lst into 2 sub-arrays.
        middle = len(lst)//2
        left = lst[:middle]
        right = lst[middle:]
        # recurse each of the sub-arrays.
        mergeSort(left)
        mergeSort(right)
        # initialize counters.
        i = 0  # left sub-array
        j = 0  # right sub-array
        k = 0  # return list
        # merge step to sort in ascending order.
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    return lst

#------ Quick Sort --------------

def quickSort(lst):
    # User interface to enter single array to be sorted
    quickSortie(lst, 0, len(lst)-1)  # Call quickSort helper function.
    return lst

def quickSortie(lst, p, r):
    # Python representation of quicksort algorithm pg 171 Introduction to Algorithms, Cormen
    if p < r:
        q = randomizedpartition(lst, p, r)
        quickSortie(lst, p, q-1)
        quickSortie(lst, q+1, r)

def randomizedpartition(lst, p, r):
    # randomized partition to select random index from array.
    i = random.randint(p, r)
    lst[p], lst[i] = lst[i], lst[p]  # swap first element in array with chosen index.
    return partition(lst, p, r)  # call partition with first element being chosen index.

def partition(lst, p, r):
    # partition scheme similar to "Hoare Partition" pg 185 Introduction to Algorithms, Cormen.
    pivot = lst[p]
    # keep pivot in place and adjust array pointer.
    left = p + 1
    right = r

    done = False
    while not done:  # traverse array from either end [p+1 -->  <--r]
        while left <= right and lst[left] <= pivot:
            left += 1
        while lst[right] >= pivot and right >= left:
            right -= 1

        if right < left:  # when pointers pass one another.
            done = True
        else:  # when element fails conditions above, swap.
            temp = lst[left]
            lst[left] = lst[right]
            lst[right] = temp

    temp = lst[p]
    lst[p] = lst[right]
    lst[right] = temp

    return right

# ------ Timing Utility Functions ---------

# Code below is given only for demonstration purposes

# Function: generateRandomList
# Generate a list of n elements from 0 to n-1
# Shuffle these elements at random

def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst


def measureRunningTimeComplexity(sortFunction,lst):
    t0 = time.clock()
    sortFunction(lst)
    t1 = time.clock()  # A rather crude way to time the process.
    return (t1 - t0)

# Write code to extract average/worst-case time complexity for your sorting routines.
def calcRunTimesIS():
        averageCase = []
        worstCase = []
        for j in range(5, 500, 5):  # iterate through n.
            runTime = []
            for i in range(0, 75):  # 75 trials per n.
                lst = generateRandomList(j)  # generate lst of size n
                runtime = measureRunningTimeComplexity(insertionSort, lst)  # analyze runtime of the sort function.
                runTime.append(runtime)
            maximum = max(runTime)  # determine maximum run time of 20 trials of size n.
            worstCase.append(maximum)  # collection of worst case run times of increasing size n.
            average = sum(runTime)/float(len(runTime))  # determine average run times over 20 trials of size n.
            averageCase.append(average)  # collection of average run times of increasing size n.

        # set up x axis.
        xaxis = []
        index = 5
        for j in range(0, 99):
            xaxis.append(index)
            index += 5
        # set up plot
        title = ('Average vs Worst Case of Insertion Sort')
        print (title)
        plt.plot(xaxis, averageCase)
        plt.plot(xaxis, worstCase)
        plt.title(title)
        plt.legend(['average case', 'worst case'], loc='upper left')
        plt.ylabel('Run Time (s)')
        plt.xlabel('Size of Array (n)')
        plt.show()

def calcRunTimesMS():
        averageCase = []
        worstCase = []
        for j in range(5, 500, 5):  # iterate through n.
            runTime = []
            for i in range(0, 75):  # 50 trials per n.
                lst = generateRandomList(j)  # generate lst of size n
                runtime = measureRunningTimeComplexity(mergeSort, lst)  # analyze runtime of the sort function.
                runTime.append(runtime)
            maximum = max(runTime)  # determine maximum run time of 20 trials of size n.
            worstCase.append(maximum)  # collection of worst case run times of increasing size n.
            average = sum(runTime)/float(len(runTime))  # determine average run times over 20 trials of size n.
            averageCase.append(average)  # collection of average run times of increasing size n.

        # set up x axis.
        xaxis = []
        index = 5
        for j in range(0, 99):
            xaxis.append(index)
            index += 5
        # set up plot
        title = ('Average vs Worst Case of Merge Sort')
        print (title)
        plt.plot(xaxis, averageCase)
        plt.plot(xaxis, worstCase)
        plt.title(title)
        plt.legend(['average case', 'worst case'], loc='upper left')
        plt.ylabel('Run Time (s)')
        plt.xlabel('Size of Array (n)')
        plt.show()

def calcRunTimesQS():
        averageCase = []
        worstCase = []
        for j in range(5, 500, 5):  # iterate through n.
            runTime = []
            for i in range(0, 75):  # 50 trials per n.
                lst = generateRandomList(j)  # generate lst of size n
                runtime = measureRunningTimeComplexity(quickSort, lst)  # analyze runtime of the sort function.
                runTime.append(runtime)
            maximum = max(runTime)  # determine maximum run time of 20 trials of size n.
            worstCase.append(maximum)  # collection of worst case run times of increasing size n.
            average = sum(runTime)/float(len(runTime))  # determine average run times over 20 trials of size n.
            averageCase.append(average)  # collection of average run times of increasing size n.

        # set up x axis.
        xaxis = []
        index = 5
        for j in range(0, 99):
            xaxis.append(index)
            index += 5
        # set up plot
        title = ('Average vs Worst Case of Quicksort')
        print (title)
        plt.plot(xaxis, averageCase)
        plt.plot(xaxis, worstCase)
        plt.title(title)
        plt.legend(['average case', 'worst case'], loc='upper left')
        plt.ylabel('Run Time (s)')
        plt.xlabel('Size of Array (n)')
        plt.show()

def main():
    print("Analyzing Insertion Sort...")
    calcRunTimesIS()
    print("Analyzing Merge Sort...")
    calcRunTimesMS()
    print ("Analyzing Quicksort...")
    calcRunTimesQS()
    print ("Analysis complete")