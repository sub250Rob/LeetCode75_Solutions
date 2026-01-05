from math import gcd


# solution class required for leetcode
class Solution:
    def __init__(self):
        pass

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #leetcode constraint satisfied by converting to all upper-case
        s1 = s1.upper()
        s2 = s2.upper()

        # checks if the both strings contain the pattern
        if s1 + s2 != s2 + s1:
            return ""

        #uses the gcd library to extract the index just to the right of the last character in the pattern
        divisor_len = gcd(len(s1), len(s2))
        # pattern is properly sliced and returned
        return s1[:divisor_len]

