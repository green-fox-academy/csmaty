'use strict';

function greet (name) {
  console.log('Hi, ' + name + '!');
}

greet('everyone')

var koszontes = greet;

koszontes('Mark');

var print = console.log;

function greeter (name, log) {
  log('Csovi ' + name);
}

greeter('Lajos, nem Lali', print);

// function add(a, b) {
//   return a + b;
// }
// same as following

var add = function (a, b) (return a + b; );

console.log(add(1, 2));


greeter('Csabi', function(text)) {
  console.log(text, 'logged by my function');
}
