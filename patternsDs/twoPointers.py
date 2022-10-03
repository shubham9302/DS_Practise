class twoPointers():
    def __init__(self):
        pass

    """
    Problem1
    Given an array of sorted numbers and a target sum, 
    find a pair in the array whose sum is equal to the given target.
    Write a function to return the indices of the
    two numbers (i.e. the pair) such that they add up to the given target.
    """

    def problem1solution1(self, sum, arr):
        for i in range(len(arr)):
            for y in range(i + 1, len(arr)):
                if arr[i] + arr[y] == sum:
                    return i, y

    def problem1solution2(self, sum, arr):
        for i in range(0, len(arr)):
            second_number = sum - arr[i]
            result = self.binarySearch(arr, second_number, len(arr), i)
            if result != -1:
                return i, result

    def binarySearch(self, arr, number, high, low):
        while low <= high:
            mid = int((high + low) / 2)
            if arr[mid] > number:
                high = mid - 1
            elif arr[mid] < number:
                low = mid + 1
            elif arr[mid] == number:
                return mid
        else:
            return -1

    def problem1solution3(self, arr, k):
        start_pointer = 0
        end_pointer = len(arr) - 1
        while start_pointer <= end_pointer:
            sum = arr[start_pointer] + arr[end_pointer]
            if sum > k:
                end_pointer -= 1
            elif sum < k:
                start_pointer += 1
            elif sum == k:
                return start_pointer, end_pointer
            else:
                return None, None




if __name__ == "__main__":
    t1 = twoPointers()
    arr = [1, 2, 3, 4, 6]
    sum = 6
    # print(t1.problem1solution1(sum, arr)) >
    """
    Time Complexity : O(n2)
    Space Complexity : O(1)
    """
    # print(t1.problem1solution2(sum, arr))
    """
    Time Complexity : O(n*logn)
    Space Complexity : O(n)
    """
    print(t1.problem1solution3(arr, sum))
    """
    Time Complexity : O(n)
    Space Complexity : O(1)
    """
