import sys


class HeapSort:

    def __init__(self, arr=[]):
        self.arr = arr
        self.tempArray = []

    def insertElementInHeap(self):
        for i in range(0, len(self.arr)):
            self.tempArray.append(self.arr[i])
            child_index = i
            self._heapCreation(child_index)
        print(self.tempArray)

    def _heapCreation(self, child_index):
        parent_index = int((child_index - 1) / 2)
        parent = self.tempArray[parent_index]
        child = self.tempArray[child_index]
        if parent < child and child_index > 0:
            self.tempArray[parent_index], self.tempArray[child_index] = self.tempArray[child_index], self.tempArray[
                parent_index]
            self._heapCreation(parent_index)

    def _heapDeletion(self, parent_index, end__index):
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2
        right_child = self.tempArray[right_child_index]
        left_child = self.tempArray[left_child_index]
        print("end_index", end__index)
        print("left_child_index", left_child_index)
        print("right_child_index", right_child_index)
        if left_child_index < end__index and right_child_index < end__index:
            if left_child > right_child:
                comparisonIndex = left_child_index
                comparisonElement = left_child
            else:
                comparisonIndex = right_child_index
                comparisonElement = right_child
            print("comparisonElement", comparisonElement)
            print("comparisonIndex", comparisonIndex)
            end__index = end__index
            parentElement = self.tempArray[parent_index]
            if comparisonElement > parentElement and comparisonElement is not None:
                self.tempArray[comparisonIndex], self.tempArray[parent_index] = self.tempArray[parent_index], \
                                                                                self.tempArray[comparisonIndex]
                self._heapDeletion(comparisonIndex, end__index)

        elif left_child_index >= end__index > right_child_index:
            comparisonIndex = right_child_index
            comparisonElement = right_child
            end__index = end__index
            parentElement = self.tempArray[parent_index]
            if comparisonElement > parentElement and comparisonElement is not None:
                self.tempArray[comparisonIndex], self.tempArray[parent_index] = self.tempArray[parent_index], \
                                                                                self.tempArray[comparisonIndex]
                self._heapDeletion(comparisonIndex, end__index)

        elif left_child_index < end__index <= right_child_index:
            comparisonIndex = left_child_index
            comparisonElement = left_child
            end__index = end__index
            parentElement = self.tempArray[parent_index]
            if comparisonElement > parentElement and comparisonElement is not None:
                self.tempArray[comparisonIndex], self.tempArray[parent_index] = self.tempArray[parent_index], \
                                                                                self.tempArray[comparisonIndex]
                self._heapDeletion(comparisonIndex, end__index)

    def deleteElementFromHeap(self):
        end_index = len(self.tempArray) - 1
        for i in range(0, end_index):
            temp_value = self.tempArray[0]
            self.tempArray[0] = self.tempArray[end_index]
            self._heapDeletion(0, end_index)
            self.tempArray[end_index] = temp_value
            end_index -= 1
            print("postForLoop", self.tempArray)

    def heapSort(self):
        pass


if __name__ == "__main__":
    arr = [10, 20, 15, 30, 40]
    t1 = HeapSort(arr)
    t1.insertElementInHeap()
    t1.deleteElementFromHeap()
