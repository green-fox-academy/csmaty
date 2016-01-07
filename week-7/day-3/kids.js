'use strict';

var kids = [
  {name: 'Tibor', candies: 2} ,
  {name: 'Steve', candies: 3} ,
  {name: 'Agost', candies: 0} ,
  {name: 'Julika', candies: 7} ,
  {name: 'Krisztian', candies: 4} ,
];

function getTheRichestKidsname(kids) {
  var richKid = kids[0];
  for (var i = 1; i < kids.length; i++) {
    if (kids[i].candies > richKid.candies) {
      richKid = kids[i];
    }
  }
  return richKid.name
}
console.log(getTheRichestKidsname(kids))


// function getTheRichestKidsnameReduce(kids) {
// var RichKid = kids.reduce(function(acc, kids){
//   a.candies > b.candies ? a.name : b.name;
//     return RichKid
//   });
// }
// console.log(getTheRichestKidsnameReduce(kids))


// function getTheRichestKidsname2(kids) {
//   var richestKid = kids[0];
//   kids.forEach(function(currentKid))
//
// }
// kids.forEach(function)
