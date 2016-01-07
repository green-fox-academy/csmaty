'use strict';

function createStudent(name, grades) {
  return {
    name: name,
    grades: grades,
    addGrade: function(grade) {
      this.grades.push(grade);
    },
    getAverage: function() {
      var average = 0
      function reduceSum(accumulator, num) {
        return accumulator + num;
      }
      var average = this.grades.reduce(reduceSum) / this.grades.length;
      return average
    }
  };
}

var jozsi = createStudent('Jozsi', []);

jozsi.addGrade(4);
jozsi.addGrade(3);
jozsi.addGrade(5);
jozsi.addGrade(5);
console.log(jozsi.getAverage());
