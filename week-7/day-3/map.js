'use strict';

var benaSzavak = [
  'kuty',
  'macsk',
  'alm',
  'kacs'
]

var faszaSzavak = [];
for (var i = 0 ; i < benaSzavak.length; i++) {
  faszaSzavak.push(benaSzavak[i] + 'a');
}
console.log(faszaSzavak);

// **************************************************

var faszaSzavak2 = [];
benaSzavak.forEach(function(szo) {
faszaSzavak2.push(szo + 'a');
});
console.log(faszaSzavak2);

// ****************************************************

var faszaSzavak3 = benaSzavak.map(function(szo) {
  return szo + 'a';
});
console.log(faszaSzavak3);



// ********************************************************
// SZORZOTABLA

var szorzotabla1 = '';

for (var i = 1; i <= 10; i++) {
  szorzotabla1 += i + ' * ' + i*4 + '=' + '\n';
}
console.log(szorzotabla1);

var szorzotabla2 = '';
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].forEach(function (e){
  szorzotabla2 += e + ' * ' + e*4 + '=' + '\n';
});
console.log(szorzotabla2);


var szorzotabla3 = '';
var sorok = szamok.map(function(e) {
  return e + '*' + 4 + '=' + e*4;
});


szorzotabla3 = sorok.join('\n')
console.log(szorzotabla3);
