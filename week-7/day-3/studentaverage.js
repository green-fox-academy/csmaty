'use strict';

function Student(name, grades) {
  this.name = name;
  this.grades = grades;
  this.addGrade = function(grade) {
    this.grades.push(grade);
    return grades
    console.log(this.grades);
    }
  this.getAverage = function() {
    var average = 0
    function reduceSum(accumulator, num) {
      return accumulator + num;
    }
    var average = this.grades.reduce(reduceSum) / this.grades.length;
    return average
  }
}

var jozsi = new Student('Jozsi', []);
jozsi.addGrade(4);
jozsi.addGrade(3);
jozsi.addGrade(5);
jozsi.addGrade(5);
console.log(jozsi.getAverage());
