'use strict';

var array = ['apple', 'pear', 'melon', 'carrot', 'grape'];

function removeItem(array,item) {
	array.forEach(function(e) {
		if (e === item) {
			var index = array.indexOf(e);
			// console.log(index);
			array.splice(index, 1);
		}
	});
	return array;
}

console.log(removeItem(array, 'carrot'));