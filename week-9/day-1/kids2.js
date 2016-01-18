'use strict'

var kids = [
	{name:'JULI', age: 8, sex:'f'},
	{name:'TIBOr', age: 7, sex:'m'},
	{name:'zsdolti', age: 6, sex:'m'},
	{name:'Gerda', age: 9, sex:'f'},
	{name:'Zsombi', age: 8, sex:'m'}
];


function countByAge(kids, age) {
	var kidcount = 0;
	kids.forEach(function(kid) {
		if (kid.age === age) {
			kidcount ++;
		}
	});
	return kidcount;
}

console.log(countByAge(kids, 8)); // 2