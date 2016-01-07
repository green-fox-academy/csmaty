'use strict';

function Student(name, grades) {
  this.name = name;
  this.grades = grades;
  this.addGrade = function(subject, grade) {
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
  };

  this.getAverage = function () {
    var sum = 0;
    var count = 0;
    for (var subject in this.grades) {
      this.grades[subject].forEach(function(grade) {
        sum += grade;
        count += 1;
      });
    }
    return sum/count;
  };
}


var dezso = new Student('Dezsokem', {});


dezso.addGrade('matek', 5);
dezso.addGrade('matek', 4);
dezso.addGrade('matek', 4);
dezso.addGrade('rajz', 1);
dezso.addGrade('rajz', 3);

console.log(dezso.grades);

console.log(dezso.getCount());
console.log(dezso.getAverage()); // osszes jegy atlaga
//
//
// szorgalmika:
// dezso.getAverageBySubject() // atlag tantargyankent
