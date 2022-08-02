/* Determine whether a string is a palindrome. */

function isPalindrome(string) {
    // build string in reverse using a backwards for loop
    let reversed = ""
  
    for(let i = string.length-1; i >= 0; i --){
      reversed += string[i];
    }
    return reversed == string;
  }

  
  function isPalindrome(string) {
    // reverse input string using split, reverse, and join methods
    reversed = string.split("").reverse().join("")
  
    if(reversed == string){
      return true;
    }
    return false;
  }