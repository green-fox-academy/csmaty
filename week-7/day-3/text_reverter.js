'use strict';

function revertText(text) {
  var charlist = text.split('')
  var output = ''
  for (var i = (text.length - 1); i >= 0; i--) {
    output += text[i]
  }
  return output;
}

console.log(revertText('empiriokriticizmus'));

// ************************************

function reverseRecursive(input, i) {
  if (i < 0) {
    return '';
  } else {
    return input[i] + reverseRecursive(input, i);
  }
}

console.log(reverseRecursive('kacsa', 4));
