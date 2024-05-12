'''Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.'''
def lengthOfLongestSubstring(s):
        seen={}
        l=0
        max_len=0
        for r,char in enumerate(s):
                if char in seen and seen[char]>=l:
                        l=seen[char]+1
                else:
                        max_len=max(max_len,r-l+1)
                seen[char]=r
        return max_len
def lengthOfLongestSubstringWithSet(s):
        charset=set()
        l=0
        max_len=0
        for r,char in enumerate(s):
                if char not in  charset:
                        charset.add(char)
                        max_len=max(max_len,r-l+1)
                else:
                        while char in charset:
                                charset.remove(s[l])
                                l+=1
                        charset.add(char)
        return max_len

s ="abcabcbb"
res=lengthOfLongestSubstring(s)
print("Expected:3 ","Ouput:",res)


s ="bbbbb"
res=lengthOfLongestSubstringWithSet(s)
print("Expected:1 ","Ouput:",res)