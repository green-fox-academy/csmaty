'use strict'

var g = 123;

function printG() {
  console.log(g);
  g = 333;
}

printG()
console.log(g);


function prinLocalG() {
  var g = 7;
  console.log(g);
}

printlocalG();
console.log(g);

function printA() {
  var a = 123;
  console.log(a);
}

printA();
// console.log(a); (Error - a was created in the function printA, it would be out of scope.)
