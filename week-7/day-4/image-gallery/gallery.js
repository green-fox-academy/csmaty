'use strict';

var pictureList = [
  'http://icons.iconarchive.com/icons/cuberto/toys/256/cat-icon.png',
  'http://downloadicons.net/sites/default/files/cute-penguin-icon-52438.png',
  'http://downloadicons.net/sites/default/files/cute-little-tiger-icons-50282.png',
  'http://www.icon2s.com/wp-content/uploads/2014/06/animal-icon-crab.png',
  'http://icons.iconarchive.com/icons/martin-berube/animal/256/rabbit-icon.png',
  'http://www.icon2s.com/wp-content/uploads/2014/06/animal-icon-tuna-blue-fish.png',
  'http://www2.psd100.com/ppp/2013/11/2701/Cute-littles-cattle-1127125620.png'];



var nextButton = document.querySelector('.show_next');
var previousButton = document.querySelector('.show_previous');
var displayedPicture = document.querySelector('.current_image');
var currentThumbnail = document.querySelector('.current_thumbnail');
var currentImage = 0

nextButton.addEventListener('click', function() {
  currentImage++;
  if (currentImage > pictureList.length -1) {
    currentImage = 0;
  }
  displayedPicture.setAttribute('src', pictureList[currentImage])
  console.log(currentImage);

});

previousButton.addEventListener('click', function() {
  currentImage--;
  if (currentImage < 0) {
    currentImage = pictureList.length -1;
  }
  displayedPicture.setAttribute('src', pictureList[currentImage])
  console.log(currentImage);
});


function insertAsThumbnail(src) {
  var thumbnailList = document.querySelector('.thumbnail_list');
  var thumbnail = document.createElement('img');
  thumbnail.setAttribute('src', src);
  thumbnailList.appendChild(thumbnail);

  thumbnail.addEventListener('click', function(){
    currentImage = pictureList.indexOf(src);
    displayedPicture.setAttribute('src', pictureList[currentImage]);


    currentThumbnail = document.querySelector('.current_thumbnail');
    if (currentThumbnail !== null) {
      currentThumbnail.classList.remove('current_thumbnail')
    }
    thumbnail.classList.add('current_thumbnail');

    console.log(currentImage);
  });
}

// function changeImageThroughTumbnail () {
//
// }

pictureList.forEach(function(e){
  insertAsThumbnail(e);
});