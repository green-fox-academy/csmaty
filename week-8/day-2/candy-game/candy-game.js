'use strict'

var candyCount = 0;
var lollyCount = 0;
var hasGameEnded = false;

var candyButton = document.querySelector('.recieve-candies');
candyButton.addEventListener('click', function() {
  candyCount ++;
  displayCurrentCandies()
});

var lollyButton = document.querySelector('.buy-lollypops');
lollyButton.addEventListener('click', function() {
  if (candyCount >= 10) {
    exchangeCandiesForLolly()
    displayCurrentCandies()
    displayCurrentLollies()
    IsGoalReached();
  }
});

function displayCurrentCandies() {
  document.querySelector('.candy-counter').innerHTML = candyCount;
}

function displayCurrentLollies() {
  document.querySelector('.lolly-counter').innerHTML = lollyCount;
}

function exchangeCandiesForLolly() {
  candyCount -= 10;
  lollyCount ++;
}

function IsGoalReached() {
  if (candyCount >= 10000) {
    alert('We have a winner!');
    hasGameEnded = true;
  }
};

setInterval (function() {
  var plusCandyPerSecond =  Math.floor(lollyCount / 10);
  if (!hasGameEnded) {
    candyCount += plusCandyPerSecond;
    displayCurrentCandies();
    IsGoalReached();
  }
}, 1000);
