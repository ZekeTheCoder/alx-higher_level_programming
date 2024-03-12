#!/usr/bin/node
/* A function that prints the number of arguments already printed and the new argument value. */

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
