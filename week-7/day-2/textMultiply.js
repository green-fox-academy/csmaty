'use strict'

function textMultiply(text, number) {
  var output = ''
  for (var i = 0; i < number; i++) {
    output += text;
  }
  return output
}

console.log(textMultiply('empiriokriticizmus', 9));

function RecursivetextMultiply(text, number) {
  return number ? text + RecursivetextMultiply(text, number - 1) : '';
}

console.log(RecursivetextMultiply('empiriokriticizmus', 9));
