""" If any two numbers in an array sum to the target sum, return the two numbers as an array. """

def twoNumberSum(array, targetSum):
    # outer loop to get first num
    for i in range(len(array)):
        # inner loop to get following nums
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i],array[j]]

    return []