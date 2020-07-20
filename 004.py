class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        sortedList=self.mergeTwoSortedLists(nums1,nums2)
        if len(sortedList)%2==0:
            index=len(sortedList)/2
            median=sortedList[int(index)-1]+sortedList[int(index)]
            return float(median/2)
        else:
            return float(sortedList[int(0.5*(len(sortedList)))])



    def mergeTwoSortedLists(self, list1, list2):
        sortedArray = [None] * (len(list1) + len(list2))
        list1Counter = list2Counter = sortedListCounter = 0
        while list1Counter < len(list1) and list2Counter < len(list2):
            if list1[list1Counter] <= list2[list2Counter]:
                sortedArray[sortedListCounter] = list1[list1Counter]
                list1Counter += 1
            else:
                sortedArray[sortedListCounter] = list2[list2Counter]
                list2Counter += 1
            sortedListCounter += 1
        while list1Counter < len(list1):
            sortedListCounter += 1
            sortedArray[sortedListCounter] = list1[list1Counter]
            list1Counter += 1

        while list2Counter < len(list2):
            sortedArray[sortedListCounter] = list2[list2Counter]
            list2Counter += 1
            sortedListCounter += 1

        return sortedArray
print(Solution().findMedianSortedArrays([1,3],[2]))
print(Solution().findMedianSortedArrays([1,2],[3,4]))