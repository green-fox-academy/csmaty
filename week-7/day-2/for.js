'use strict';

for (var i = 0 ; i < 5; i++) {
  console.log(i);
}

var dogs = ['kati', 'robi', 'lali'];

for (var i = 0 ; i < dogs.length; i++) {
  console.log(dogs[i]);
}

var student = {
  kor: 6,
  nev: 'Tibi',
  labmeret: 45
  };

for (var key in student) {
  console.log(key);
  console.log(student[key]);
}
