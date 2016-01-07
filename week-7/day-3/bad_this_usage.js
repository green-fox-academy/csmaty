'use strict';

var student = {
  age: 10,
  sayYourage: sayYourage
};

function sayYourage() {
  console.log('I am ' + this.age);
}

student.sayYourage();

sayYourage();
