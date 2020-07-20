def threeSum(array, target):
    possibleCombinations = []
    array.sort()
    for i in range(len(array) - 1):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == target:
                possibleCombinations.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
    return possibleCombinations


print(threeSum([1, 2, 3, 1, 1, 2], 4))
