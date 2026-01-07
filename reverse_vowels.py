'''
Docstring for reverse_vowels

This is my solution for LeetCode 75, Problem #345 (Difficulty: Easy)
'''

#solution class required by Leet code
class Solution:

    #default constructor:
    def __init__(self):
        pass

    #function definition for reversing vowels
    def reverseVowels(self, s: str) -> str: #type: ignore

        #tuple for the loop to check for vowels
        vowels = ("a","e","i","o","u","A","E","I","O","U")

        #new string that will contain the reversed vowels
        new = ""

        #turns the original string into a list in order to better access and reverse the individual characters
        s = list(s)

        #list for storing just the vowles
        vows = []

        #for loop to populate the vowels-of-the-word list
        for elem in s:
            if elem in vowels:
                vows.append(elem)

        # the vowels of the original string need a seperate counter
        j = -1

        #Iterates through the list 's', if the letter is not a vowel
        #it is appended, if not, the vowel list of the original
        #word is iterated through and appended to new backwards,
        #the extra tracker variable 'j' allows vows to not be affected
        #by i's updates
        for i in range (0, len(s)):
            if s[i] not in vowels:
                new += s[i]
            else:
                new += vows[j]
                j -=1

        return new
    
