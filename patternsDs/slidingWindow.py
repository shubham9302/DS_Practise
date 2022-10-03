class slidingWindow():

    def __init__(self):
        pass

    """
    Problem 1:
    Given an array, find the average of each subarray of ‘K’ contiguous elements in it.
    For example :
    input : Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
    o/p : [2.2, 2.8, 2.4, 3.6, 2.8]
    """

    def bruteForceApproach(self, k, arr=[]):
        result = []

        for i in range(0, len(arr)):
            sum = 0.0
            for y in range(i, i + k):
                sum += arr[y]

            result.append(sum / k)
        return result

    ### Time complexity = O(k*n)
    ##Space Complexity = O(k)

    def optimisedApproach(self, k, arr):
        """
        In this optimised approach ,if we closely observe
        we are adding one new element and removing one new
        element in the second loop ,if we somehow save the sum
        and add the new element in the existing and subtract the
        element removed from sum ,we can get rid of the additional
        loop because in every continous block ,k-1 elements are
        same
        :return:
        """
        result = []
        initialSum, FirstVal = 0.0, 0
        for i in range(len(arr)):
            initialSum += arr[i]
            if i >= k - 1:
                resultData = (initialSum / k)
                initialSum -= arr[FirstVal]
                FirstVal += 1
            result.append(resultData)

    """
    Given an array of positive integers and a number ‘S,’ 
    find the length of the smallest contiguous subarray 
    whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists
    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].
    """

    def bruteForceP2(self, k, arr):
        minLength = float('inf')
        for i in range(len(arr)):
            sum = 0.0
            counter = 0
            for y in range(i + 1, len(arr)):
                sum += arr[y]
                counter += 1
                if sum >= k:
                    if counter < minLength:
                        minLength = counter
                    break
        return minLength

    def optSolutionP2(self, k, arr):
        minLength = float('inf')
        sumVal, elementIndex = 0.0, 0
        steps = 0
        for i in range(len(arr)):
            sumVal += arr[i]
            print("sumVal", sumVal)
            while sumVal >= k:
                print("i", i)
                print("eleementIndex", elementIndex)
                steps = i - elementIndex + 1
                sumVal -= arr[elementIndex]
                elementIndex += 1
                print("steps", steps)
                print("sumValReduced", sumVal)
                print("eleementIndex", elementIndex)
                print("i", i)

                if steps < minLength:
                    minLength = steps

                print("minLength", minLength)

            print("#######")

        return minLength

    """
    Given an array of positive numbers and a positive number ‘k,’ 
    find the maximum sum of any contiguous subarray of size ‘k’
    Input: [2, 1, 5, 1, 3, 2], k=3 
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3]
    """

    def solution(self, k, arr):
        firstVal = 0
        MaxResult = float('-inf')
        sumVal = 0
        for i in range(len(arr)):
            sumVal += arr[i]
            print("start sumVal", sumVal)
            if i >= k - 1:
                if sumVal > MaxResult:
                    MaxResult = sumVal
                    print("MaxResult", MaxResult)

                sumVal -= arr[firstVal]
                firstVal += 1
                print("arr", arr[i])
                print("sumVal", sumVal)
        print("########")
        return MaxResult

    def solution2(self, value, arr):
        import math
        minLength = math.inf
        for i in range(0, len(arr)):
            sumVal = arr[i]
            print("first", sumVal)
            counter = 1
            if sumVal >= value:
                if counter < minLength:
                    minLength = counter
                break
            for y in range(i + 1, len(arr)):
                sumVal += arr[y]
                print("second", sumVal)
                counter += 1
                print("sumVal", sumVal)
                print("counter", counter)
                if sumVal >= value:
                    if counter < minLength:
                        minLength = counter
                    break
            print("minLength", minLength)
            print("########")
        return minLength

    """
    Given a string, find the length of the longest 
    substring in it with no more than K distinct characters.
    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".
    """

    def bruteForceP3(self, k, str):
        output = 0
        maxLength = float("-inf")
        for i in range(len(str)):
            new_str = ""
            dict = {}
            if str[i] in dict.keys():
                dict[str[i]] = dict[str[i]] + 1
            else:
                dict[str[i]] = 1
            new_str = str[i]
            print("dict", dict)
            print("new_str", new_str)
            for y in range(i + 1, len(str)):
                print("inside y loop")
                if str[y] in dict.keys():
                    print("Keys exist")
                    dict[str[y]] = dict[str[y]] + 1
                else:
                    dict[str[y]] = 1
                new_str = new_str + str[y]
                print("dict", dict)
                print("new_str", new_str)
                print("dict length", len(dict.keys()))
                print("k", k)
                if len(dict.keys()) <= k:
                    print("inside length Loop")
                    output = sum(dict.values())
                    if output > maxLength:
                        maxLength = output
                        resultantString = new_str

                else:
                    break
            print("maxLength", maxLength)
            print("output", output)
            print("#########")
        return maxLength, resultantString

    def optSolP3(self, str1, k):
        window_start = 0
        max_length = 0
        char_frequency = {}
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char not in char_frequency:
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1
            while len(char_frequency) > k:
                left_char = str1[window_start]
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length

    """
    Given a string, find the length of the longest substring, 
    which has all distinct characters.
    
    """

    def problemAllDistinct(self, arr):
        k = len(set(arr))
        op = self.optSolP3(k,arr)
        return op


if __name__ == "__main__":
    t1 = slidingWindow()
    arr = [2, 1, 5, 2, 3, 2]
    k = 8
    # print(t1.optSolutionP2(k, arr))
    # arr = [2, 3, 4, 1, 5]
    # print(t1.solution(2, arr))
    # value, arr = 7, [2, 1, 5, 2, 8]
    # print(t1.solution2(value, arr))
    strData = "cbbebi"
    k = 3
    print(t1.bruteForceP3(k, strData))
