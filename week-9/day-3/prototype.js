'use strict';

function PowerRanger(color) {
	this.color = color;
}

function Fighter() {
	this.isPowerFull = true;
}

PowerRanger.prototype = new Fighter;

var yellowranger = new PowerRanger('yellow');

console.log(yellowranger.color);
console.log(yellowranger.isPowerFull);