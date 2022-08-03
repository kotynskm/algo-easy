""" If any two numbers in an array sum to the target sum, return the two numbers as an array. """

def twoNumberSum(array, targetSum):
    # outer loop to get first num
    for i in range(len(array)):
        # inner loop to get following nums
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i],array[j]]

    return []

# solution using hash table, O(n) runtime - from Leetcode

def twoSum(self, nums, target):
        # create a hash table to store nums present in array
        nums_dict = {}
        result = []
        
        # loop our array and calculate num needed, store num in nums dict
        for i in range(len(nums)):
            num_needed = target - nums[i]
            # if num needed is in the dict, return the index of num and of num needed
            if num_needed in nums_dict:
                result.extend([i, nums.index(num_needed)])
                return result
            # otherwise, add num to the num dict    
            else:
                nums_dict[nums[i]] = True
        return []
        