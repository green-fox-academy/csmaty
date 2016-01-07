'use strict';

function Student(name, grades) {
  this.name = name;
  this.grades = grades;
  this.addGrade = function(subject, grade) {
    // this.grades.push({subject: subject, grade: grade}); // solution 2
    if (this.grades[subject] === undefined) {
    // if (!(subject in this.grades)) { // same as previous line, only works for objects
      this.grades[subject] = [grade];
    } else {
      this.grades[subject].push(grade);
    }
  };

  this.getCount = function() {
    var subjectlist = []
    for (var subject in this.grades) {
      subjectlist[subject] = this.grades[subject].length;
    }
    return subjectlist

    // var output = {}; // solution 2
    // this.grades.forEach(function(grade){
    //   if (!(grade.subject in output)) {
    //     output[grade.subject] = 0;
    //   }
    //   output[grade.subject]++;
    // })

    return this.grades.reduce(function(output, grade) {
      if (!(grade.subject in output)) {
        output[grade.subject] = 0;
      }
      output[grade.subject]++;
    }, {});


  };

  // this.getAverage = function(subject) {
  //   var average = 0
  //   function reduceSum(accumulator, num) {
  //     return accumulator + num;
  //   }
  //   var average = this.grades[subject].reduce(reduceSum) / this.grades[subject].length;
  //   return average
  // }
}




var dezso = new Student('Dezsokem', {});


dezso.addGrade('matek', 5);
dezso.addGrade('matek', 4);
dezso.addGrade('matek', 4);
dezso.addGrade('rajz', 1);
dezso.addGrade('rajz', 3);

console.log(dezso.grades);

console.log(dezso.getCount());
// console.log(dezso.getAverage()); // osszes jegy atlaga
//
//
// szorgalmika:
// dezso.getAverageBySubject() // atlag tantargyankent
