'use strict';

var pictureList = [
  'http://icons.iconarchive.com/icons/cuberto/toys/256/cat-icon.png',
  'http://downloadicons.net/sites/default/files/cute-penguin-icon-52438.png',
  'http://downloadicons.net/sites/default/files/cute-little-tiger-icons-50282.png',
  'http://www.icon2s.com/wp-content/uploads/2014/06/animal-icon-crab.png',
  'https://pbs.twimg.com/profile_images/3215719745/5cc0e2137e0f1070e33cc35853e9d26a.jpeg',
  'http://www.icon2s.com/wp-content/uploads/2014/06/animal-icon-tuna-blue-fish.png'];



var nextButton = document.querySelector('.show_next');
var previousButton = document.querySelector('.show_previous');
var displayedPicture = document.querySelector('.current_image');
var currentImage = 0

nextButton.addEventListener('click', function() {
  currentImage ++;
  if (currentImage > pictureList.length -1) {
    currentImage = 0;
  }
  displayedPicture.setAttribute('src', pictureList[currentImage])
  console.log(currentImage);
});

previousButton.addEventListener('click', function() {
  currentImage --;
  if (currentImage < 0) {
    currentImage = pictureList.length -1;
  }
  displayedPicture.setAttribute('src', pictureList[currentImage])
  console.log(currentImage);
});
