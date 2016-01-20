'use strict';

var kids = [
	{name:'JULI', age: 8, sex:'f'},
	{name:'TIBOr', age: 7, sex:'m'},
	{name:'zsolti', age: 6, sex:'m'},
	{name:'Gerda', age: 9, sex:'f'},
	{name:'Zsombor', age: 8, sex:'m'}
];

function getTheLongestNamesAge(kids) {
  var longestNamedKid = kids[0]
  kids.forEach(function (kid) {
    if (kid.name.length > longestNamedKid.name.length) {
      longestNamedKid = kid
    }
  });
  return longestNamedKid.age;
}

console.log(getTheLongestNamesAge(kids)); // 8
