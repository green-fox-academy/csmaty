'use strict';

var pictureList = [
        'img/04earth.png',
        'img/09uranus.png',
        'img/01sun.png',
        'img/06mars.png',
        'img/05moon.png',
        'img/08saturn.png',
        'img/07jupiter.png',
        'img/03venus.png']

var displayedPicture = document.querySelector('.current_image');
var thumbs
var currentThumbnail
var currentImage

var nextButton = document.querySelector('.show_next');
nextButton.addEventListener('click', function() {
  currentImage++;
  if (currentImage > pictureList.length -1) {
    currentImage = 0;
  }
  displayedPicture.setAttribute('src', pictureList[currentImage])
  removeHighlightfromPrevThumbnail()
  addHighlightToCurrentThumbnail(currentImage)
});

var previousButton = document.querySelector('.show_previous');
previousButton.addEventListener('click', function(thumbs) {
  currentImage--;
  if (currentImage < 0) {
    currentImage = pictureList.length -1;
  }
  displayedPicture.setAttribute('src', pictureList[currentImage])
  removeHighlightfromPrevThumbnail()
  addHighlightToCurrentThumbnail(currentImage)
});

function removeHighlightfromPrevThumbnail() {
  currentThumbnail = document.querySelector('.current_thumbnail');
  currentThumbnail.classList.remove('current_thumbnail');
}

function addHighlightToCurrentThumbnail (currentImage) {
  thumbs = document.querySelectorAll('.thumbnail_list img');
  thumbs[currentImage].classList.add('current_thumbnail');
}

function insertAsThumbnail(src) {
  var thumbnailList = document.querySelector('.thumbnail_list');
  var thumbnail = document.createElement('img');
  thumbnail.setAttribute('src', src);
  thumbnailList.appendChild(thumbnail);
  thumbnail.addEventListener('click', function(event) {
    currentImage = pictureList.indexOf(src);
    displayedPicture.setAttribute('src', pictureList[currentImage]);
    removeHighlightfromPrevThumbnail()
    thumbnail.classList.add('current_thumbnail');
  });
}

function main() {
  displayedPicture.setAttribute('src', pictureList[0])
  pictureList.forEach(function(e){
    insertAsThumbnail(e);
  });
  currentImage = 0;
  thumbs = document.querySelectorAll('.thumbnail_list img')
  thumbs[currentImage].classList.add('current_thumbnail');
}

main();
