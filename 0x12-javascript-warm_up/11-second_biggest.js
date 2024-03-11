#!/usr/bin/node
/* This script searches the second biggest integer in the list of arguments.
* - If no argument passed, print 0
* - If the number of arguments is 1, print 0
*/

let largest = -Infinity;
let secondLargest = -Infinity;

for (let i = 2; i < process.argv.length; i++) {
  const num = parseInt(process.argv[i]);

  if (num > largest) {
    secondLargest = largest;
    largest = num;
  } else if (num > secondLargest && num !== largest) {
    secondLargest = num;
  }
}

console.log(secondLargest !== -Infinity ? secondLargest : 0);
