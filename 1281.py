class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        product=1
        for i in str(n):
            sum+=int(i)
            product*=int(i)

        return product-sum
print(Solution().subtractProductAndSum(234))