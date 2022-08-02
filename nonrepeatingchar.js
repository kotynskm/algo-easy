/* Find the first non repeating character in a string. */

function firstNonRepeatingCharacter(string) {
    // create a count dictionary
    let count_dict = {}
    // loop characters in string, and check if it is in the dict
    // if not present, set count dict at that char to 1, else increment again
    for(let char of string){
      if (count_dict[char] == undefined){
        count_dict[char] = 1;
      }else{
        count_dict[char]++;
      }
    }
    // loop keys in count dict, find the key where the value is 1 and return
    // the index of that char in the string
    for(let key in count_dict){
      if (count_dict[key] == 1){
        return string.indexOf(key)
      }
    }
    
    return -1;
  }