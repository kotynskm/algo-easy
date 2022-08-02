/* If any two numbers in an array sum to the target sum, return the two numbers as an array. */

function twoNumberSum(array, targetSum) {
    // outer loop to get first num in the array
    for(let i = 0; i < array.length; i++){
      // inner loop to get the following nums in the array
        for(let j = i + 1; j < array.length; j++){
          // check if sum of the nums equals the target
             if(array[i] + array[j] == targetSum){
                return [array[i],array[j]];
            }
        }    
    }
    return [];
  }