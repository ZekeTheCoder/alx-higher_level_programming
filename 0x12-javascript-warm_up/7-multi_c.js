#!/usr/bin/node
/* This script prints x times “C is fun”
* - Where x is the first argument of the script
* - If the first argument can’t be converted to an integer, print “Missing number of occurrences”s amazing”
*/

const x = parseInt(process.argv[2]);

if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
