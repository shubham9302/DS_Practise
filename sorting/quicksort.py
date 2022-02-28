from sorting.commonutil import Utilities
import math


class quickSort:

    def __init__(self):
        pass

    def partition(self, start, end, arr):

        pivot = arr[start] ## 8
        pivot_index = start ##0
        ## start 0
        ### end 4
        print("intial start",start)
        print("initial end",end)
        while start < end:

            while start < len(arr) and arr[start] <= pivot:
                start += 1
                print("start ",start)

            while arr[end] > pivot:
                end = end - 1
                print("end ",end)

            if start < end:
                print("inside if ")
                print("start index", start)
                print("end index", end)
                arr[start], arr[end] = arr[end], arr[start]
                print("arr", arr)
        arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
        print("final arr",arr)
        print("last end ",end)
        return end

    def sort(self, start, end, arr):

        if start < end:
            partition = self.partition(start, end, arr)
            self.sort(start, partition - 1, arr)
            print("left sort done")
            self.sort(partition + 1, end, arr)
            print("right sort done")
        return arr


if __name__ == "__main__":
    arr = [8, 5, 7, 3, 2]
    #arr = [8, 7, 5, 3, 2]
    t1 = quickSort()
    print(t1.sort(0, len(arr) - 1, arr))
