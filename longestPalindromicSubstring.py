longestPalindrome=0
def longestPalindromes(s):
    longest=''
    for i in range(len(s)):
        for j in range(i+1, len(s) + 1):
            palindrome= s[i:j]
            isPalindrome=palindrome==palindrome[::-1]
            if isPalindrome:
                if len(palindrome)>len(longest):
                    longest=palindrome
    return longest




print(longestPalindromes('aaa'))


