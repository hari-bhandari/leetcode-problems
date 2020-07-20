def binarySearchAlgorithm(sortedArray, target):
    left = 0
    right = len(sortedArray) - 1
    while left <= right:
        median = (left + right) // 2
        if sortedArray[median] == target:
            return True
        elif sortedArray[median] < target:
            right = median - 1
        else:
            left = median + 1

    return False


print(binarySearchAlgorithm([1, 2, 3, 4, 5], 34))
