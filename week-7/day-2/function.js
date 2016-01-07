'use strict'

function greet(name) {
  console.log('Hi ' + name + '!');
}

greet('Mr. T')
greet('Mr. T', 4, 'kacsapulcsiban', [])

greet()

function printArgs(a, b, c, d, e) {
  console.log(a, b, c, d, e);
}

printArgs(34, 2332, 21)

function double(num) {
  return 2 * num
}

console.log(double(123));
