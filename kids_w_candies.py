
class Solution:

    def __init__(self):
        pass

    
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        #List to store results
        greatest = []

        '''
        Outer loop establishes adds the extra candies to the candies at the current index
        also establishes a tracker variable for checking if the temp value is the would-be
        greatest among the rest of the list.

        The inner list skips the current index and then checks if every other index is less
        than or equal to the temp (since multiple kids can have the most candies in the same iteration)

        Then, if the count is equal to the length of the original list -1 (ie. every value is <= temp),
        then True is added to greatest, otherwise false is added.
        '''
        for i in range(len(candies)):
            temp = candies[i] + extraCandies
            count = 0
            for j in range(len(candies)):
                if j == i:
                    continue
                else: 
                    if candies[j] <= temp:
                        count += 1
            if count == len(candies) -1:
                greatest.append(True)
            else:
                greatest.append(False)

        return greatest
