#!/usr/bin/node
/* This script pprints the addition of 2 integers
* - The first argument is the first integer
* - The second argument is the second integer
* - A function defined with this prototype: function add(a, b)
*/

function add (a, b) {
  return a + b;
}

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (Number.isNaN(num1) && Number.isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
