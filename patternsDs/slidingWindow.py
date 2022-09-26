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


if __name__ == "__main__":
    t1 = slidingWindow()
    arr = [2, 1, 5, 2, 3, 2]
    k = 8
    print(t1.optSolutionP2(k, arr))
