class Utilities:
    @staticmethod
    def swap(a, b, arr):
        arr[a], arr[b] = arr[b], arr[a]
        return arr
