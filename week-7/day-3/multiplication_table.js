'use strict';

for (var j = 1; j <= 10; j++) {
  for (var i = 1; i <= 10; i++) {
    console.log(String(i) + ' * ' + String(j) + ' = ' + String(i * j));
  }
}

function multiplicatontable(num) {
  var output = ''
  for (var i = 1; i <= 10; i++) {
    output += (String(i) + ' * ' + String(num) + ' = ' + String(i * num) + '\n');
  }
  return output
}

console.log(multiplicatontable(7));
