'use strict'

function listItemAdder(list) {
  var sum = 0
  for (var i = 0; i < list.length; i++) {
    sum += list[i];
  }
  return sum
}

console.log(listItemAdder([3,3,4,4,5,10]));
