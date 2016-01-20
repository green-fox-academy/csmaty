'use strict';

var kids = [
	{name:'JULI', age: 8, sex:'f'},
	{name:'TIBOr', age: 7, sex:'m'},
	{name:'zsolti', age: 6, sex:'m'},
	{name:'Gerda', age: 9, sex:'f'},
	{name:'Zsombor', age: 8, sex:'m'}
];



function filterNamesBySex(kids, sex) {
	var namelist = [];
	kids.forEach(function (kid) {
		if (kid.sex === sex) {
			namelist.push(kid.name)
		}
	});
	return namelist;
}

console.log(filterNamesBySex(kids, 'f')); // Juli, Gerda