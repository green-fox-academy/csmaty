'use strict';

function createCar(color, type, km) {
	function ride(distance) {
		km += distance;
	}


	function getKm() {
		return km;
	}

	return {
		ride: ride,
		getKm: getKm
	};
}

var opel = createCar('white', 'opel', 4000);

opel.ride(100);
console.log(opel.getKm());