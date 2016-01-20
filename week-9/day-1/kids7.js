'use strict';

var kids = [
	{name:'JULI', age: 8, sex:'f'},
	{name:'TIBOr', age: 7, sex:'m'},
	{name:'zsolti', age: 6, sex:'m'},
	{name:'Gerda', age: 9, sex:'f'},
	{name:'Zsombor', age: 8, sex:'m'}
];

function groupBySex(kids) {
  var sexes = {}
  kids.forEach(function(kid) {
    if (sexes[kid.sex] === undefined) {
      sexes[kid.sex] = [];
    }
    sexes[kid.sex].push(kid);
  });
  return sexes;
}

console.log(groupBySex(kids));
 // { f:
 //   [ { name: 'JULI', age: 8, sex: 'f' },
 //     { name: 'Gerda', age: 9, sex: 'f' } ],
 //  m:
 //   [ { name: 'TIBOr', age: 7, sex: 'm' },
 //     { name: 'zsolti', age: 6, sex: 'm' },
 //     { name: 'Zsombor', age: 8, sex: 'm' } ] }
