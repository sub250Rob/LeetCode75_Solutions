'''
Docstring for prod_of_arr_except_self

This is my solution for LeetCode 75, Problem #238 (Difficulty: Medium)
'''

class Solution:
    def productExceptSelf(self, nums: list):
        
        if len(nums) == 0:
            raise ValueError ("List was empty when assumed to not be empty")
        
        arr_sizer = len(nums)
        
        prefix_product_arr = [1] * arr_sizer
        postfix_products_arr = [1] * arr_sizer

        answer = [1] * arr_sizer
 
        #compute prefix product for other elements in the array except the current one:
        
        for i in range (1, len(nums)):
            
            prefix_product_arr[i] = prefix_product_arr[i-1] * nums[i - 1]
        
        #compute postfix product for other elements in the array: 
            
        for i in range (len(nums) - 2, -1, -1):
            
            postfix_products_arr[i] = postfix_products_arr[i+1] * nums[i + 1]
        
        
        for i in range (len(nums)):
            answer[i] = prefix_product_arr[i] * postfix_products_arr[i]
            
            
        return answer
