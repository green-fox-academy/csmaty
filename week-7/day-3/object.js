'use strict';

var humwee = {
  type: 'Rendes Katonai Hummer',
  color: 'Terep',
  km: 20000
};

console.log(humwee.km);

function oldride(car, km) {
  car.km += km;
}

oldride(humwee, 200);
console.log(humwee.km);

// **************************************************

var humwee2 = {
  type: 'Rendes Katonai Hummer',
  color: 'Terep',
  km: 20000,
  ride: function(km) {
    this.km += km;
  }
};

humwee2.ride(200);
console.log(humwee.km);
