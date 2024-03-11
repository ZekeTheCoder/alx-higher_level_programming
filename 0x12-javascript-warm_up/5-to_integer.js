#!/usr/bin/node
/* This prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
* - If the argument can’t be converted to an integer, print “Not a number”
*/

const num = parseInt(process.argv[2]);

if (Number.isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
