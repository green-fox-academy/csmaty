'use strict';

var kids = [
	{name:'JULI', age: 8, sex:'f'},
	{name:'TIBOr', age: 7, sex:'m'},
	{name:'zsdolti', age: 6, sex:'m'},
	{name:'Gerda', age: 9, sex:'f'},
	{name:'Zsombi', age: 8, sex:'m'}
];


function getAges(kids) {
  var agelist = [];
  kids.forEach(function (kid) {
  agelist.push(kid.age);
  })
  return agelist;
}

function getAges2(kids) {
  return kids.map(function(kid) {
    return kid.age;
  });
}

console.log(getAges(kids)); // [8, 7, 6, 9, 8]
console.log(getAges2(kids)); // [8, 7, 6, 9, 8]
