#!/usr/bin/node
/* A function that prints the number of arguments already printed and the new argument value.
* - Output format: <number arguments already printed>: <current argument value>
*/

let nArgs = 0;

exports.logMe = function (item) {
  console.log(`${nArgs}: ${item}`);
  nArgs++;
};
