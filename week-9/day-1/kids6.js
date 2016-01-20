'use strict';

var kids = [
	{name:'JULI', age: 8, sex:'f'},
	{name:'TIBOr', age: 7, sex:'m'},
	{name:'zsolti', age: 6, sex:'m'},
	{name:'Gerda', age: 9, sex:'f'},
	{name:'Zsombor', age: 8, sex:'m'}
];


function countKidsBySex(kids) {
	var sexes = {f: 0, m: 0}
	kids.forEach(function(kid) {
		sexes[kid.sex]++;
	});
	return sexes;
}

function countKidsBySex2(kids) {
	var sexes = {}
	kids.forEach(function(kid) {
		if (sexes[kid.sex] === undefined) {
			sexes[kid.sex] = 0;
		}
		sexes[kid.sex]++;
	});
	return sexes;
}


console.log(countKidsBySex(kids));
console.log(countKidsBySex2(kids));

