#!/usr/bin/node
/* A class Square that defines a square and inherits from Square of 5-square.js:
* - You must use the class notation for defining your class and extends
* - Create an instance method called charPrint(c) that prints the rectangle using the character c
*        - If c is undefined, use the character X
*/

const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    let myChar = '';
    if (c === undefined) {
      myChar = 'X';
    } else {
      myChar = c;
    }

    for (let i = 0; i < this.height; i++) {
      let column = '';
      for (let j = 0; j < this.width; j++) {
        column += myChar;
      }
      console.log(column);
    }
  }
}
module.exports = Square;
