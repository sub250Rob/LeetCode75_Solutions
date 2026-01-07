'''
Docstring for Merge_Strings

This is my solution for LeetCode 75, Problem #1768 (Difficulty: Easy)
'''

class Solution:

    def __init__(self):
        pass

    def mergeAlternately(self, word1, word2):

        merged = ""

        if len (word1) < len(word2):
            smaller = word1
            other = word2
        else:
            smaller = word2
            other = word1
        
        for i in range (len(smaller)): 
            merged += word1[i]
            merged += word2[i]
        
        merged += other[(len(smaller)):]

        return merged
