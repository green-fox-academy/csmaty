'use strict';

var kids = [
	{name:'JULI', age: 8, sex:'f'},
	{name:'TIBOr', age: 7, sex:'m'},
	{name:'zsolti', age: 6, sex:'m'},
	{name:'Gerda', age: 9, sex:'f'},
	{name:'Zsombor', age: 8, sex:'m'}
];


function getAgeByName(kids, name) {
	var kidage = 0;
	kids.forEach(function(e) {
		if(e.name === name) {
			kidage = e.age;
		}
	});
	return kidage;
}


console.log(getAgeByName(kids, "Gerda"));