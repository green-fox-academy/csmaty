'use strict'

console.log('nem vagyok robot');

var cim = document.querySelector('.majom');
console.log(cim);

// cim.style.backgroundColor = 'pink';
cim.classList.add('piros');

var majomKep = document.querySelector('.majmos');
majomKep.setAttribute('src','http://images.clipartpanda.com/monkey-clipart-4ib5bExig.jpeg');

function kepcsinalo(src) {
  var ujkep = document.createElement('img');
  ujkep.setAttribute('src', src);
  document.querySelector('body').appendChild(ujkep);

  var bodyvaltozoban = document.querySelector('body');

  bodyvaltozoban.appendChild(ujkep);
}

kepcsinalo('https://41.media.tumblr.com/84729c469ca431c8c80dad1cd4281205/tumblr_o08zo7SJan1tx21ogo1_540.jpg')



for (var i = 0; i < 4; i++) {
  kepcsinalo('https://pbs.twimg.com/profile_images/3215719745/5cc0e2137e0f1070e33cc35853e9d26a.jpeg');
}


var kepek = [
            'http://downloadicons.net/sites/default/files/cute-penguin-icon-52438.png',
            'http://downloadicons.net/sites/default/files/cute-little-tiger-icons-50282.png', 'http://www.icon2s.com/wp-content/uploads/2014/06/animal-icon-crab.png',
            'https://pbs.twimg.com/profile_images/3215719745/5cc0e2137e0f1070e33cc35853e9d26a.jpeg',
            'http://www.icon2s.com/wp-content/uploads/2014/06/animal-icon-tuna-blue-fish.png',
          ];

kepek.forEach(function(e){
  kepcsinalo(e);
});

var gomb = document.querySelector('.csinal');
gomb.addEventListener('click', function() {
 alert('kattintottam');
 kepcsinalo('https://pbs.twimg.com/profile_images/3215719745/5cc0e2137e0f1070e33cc35853e9d26a.jpeg')
});

window.addEventListener('scroll', function() {
  console.log('scroll', window.scrollY);
});


var cicagomb = document.querySelector('.cicat');
var kutyagomb = document.querySelector('.kutyat');
var valtoskep = document.querySelector('.cicaskutyaskep');

kutyagomb.addEventListener('click', function() {
 valtoskep.setAttribute('src', 'http://icons.iconarchive.com/icons/iconka/tailwaggers/128/dog-einstein-icon.png')
});


cicagomb.addEventListener('click', function() {
 valtoskep.setAttribute('src', 'http://icons.iconarchive.com/icons/cuberto/toys/256/cat-icon.png')
});
