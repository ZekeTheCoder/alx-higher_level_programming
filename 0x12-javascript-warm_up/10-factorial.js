#!/usr/bin/node
/* This script computes and prints a factorial
* - The first argument is integer (argument can be cast as integer) used for computing the factorial
* - Factorial of NaN is 1
* - use recursive
* - use a function
*/

const num = parseInt(process.argv[2]);

function factorial (n) {
  // Base case: factorial of 0 or NaN is 1
  if (n === 0 || Number.isNaN(n)) {
    return (1);
  } else {
    // Recursive case: n! = n * (n-1)!
    return (n * factorial(n - 1));
  }
}

console.log(factorial(num));
