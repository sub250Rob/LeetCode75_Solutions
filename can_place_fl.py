
# Standard class definition for Leetcode submission
class Solution:

    def __init__(self):
        pass

    # Function definition for solution
    #2 inputs, a list and a number, with a true or false output
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        #can_place is the boolean value that will be returned
        can_place = False
        #counter that will track if new flowers can be placed, will directly affect the state of can_place
        count = 0

        # skips the current index if the value at that index is 1
        #otherwise, checks if the current element and its adjacent elements are zero, if so
        #count is incremented
        for i in range (len(flowerbed)):

            #case if the element is 1
            if flowerbed[i] == 1:
                continue
            #cases if the element is 0
            if (flowerbed[i] ==0):
                # case if the length of the flowerbed is 1
                if len(flowerbed) ==1:
                    flowerbed[i] = 1
                    count += 1
                # case if the element that is 0 is the first element
                elif i == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1
                #case if the element that is 0 is the last element
                elif (i == (len(flowerbed)-1)) and flowerbed[i-1] ==0:
                    flowerbed[i] = 1
                    count += 1
                else:
                    #case if the element that is 0 is at any other part of the list
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count +=1

        # will return true if the number of valid new flower positions is >= n
        if count >= n:
            can_place = True
        


        return can_place
        


