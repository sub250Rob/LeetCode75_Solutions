
'''
Docstring for reverse_wrds_in_string

This my solution for LeetCode 75, Problem #151 (Difficulty: Medium)
'''



class Solution:

    def reverseWords(self, s):

        #splits the string s into individual tokens so they can be reversed
        tokens = s.split()

        #using .join to cut out extra spaces and concatenate the tokens to a new string in reverse order.
        new = " ".join(tokens[::-1])

        return new

        