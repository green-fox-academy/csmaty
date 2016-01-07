'use strict';

var numbers = [5, 6, 3, 8];

function reduceSum(accumulator, num) {
  return accumulator + num;
}

var sum = numbers.reduce(reduceSum, 0);
console.log(sum);
