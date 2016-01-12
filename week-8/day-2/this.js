'use strict';

var human = {
  word: ['Kacsa', 'Macska', 'Medv'],
  name: 'Tibbor'
  speak: speak
}



function speak() {
  var _this = this;
  this.word.Foreach(function(w) {
    console.log('I am ' + _this.name);
    console.log('blabla'  + w);
  });
}


human.speak();
