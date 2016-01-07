'use strict'

function add(a, b) {
  return a + b;
}

console.log(add(23, 81));

var osszeadas = add;
console.log(osszeadas(4, 5));

var szorzas = function (a, b) {
  return a * b;
};

console.log(szorzas(6, 6));
