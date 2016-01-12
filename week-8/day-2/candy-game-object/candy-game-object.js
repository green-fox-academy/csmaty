'use strict'

function CandyGame() {
  var _this = this;
  this.candyCount = 0;
  this.lollyCount = 0;
  this.hasGameEnded = false;

  this.candyButton = document.querySelector('.recieve-candies');
  this.candyButton.addEventListener('click', function() {
      _this.candyCount++;
      _this.displayCurrentCandies()
  });

  this.lollyButton = document.querySelector('.buy-lollypops');
  this.lollyButton.addEventListener('click', function() {
    if (_this.candyCount >= 10) {
      _this.exchangeCandiesForLolly()
      _this.displayCurrentCandies()
      _this.displayCurrentLollies()
      _this.IsGoalReached();
    }
  });

  this.displayCurrentCandies = function() {
    document.querySelector('.candy-counter').innerHTML = this.candyCount;
  }

  this.displayCurrentLollies = function() {
    document.querySelector('.lolly-counter').innerHTML = this.lollyCount;
  }

  this.exchangeCandiesForLolly = function() {
    this.candyCount -= 10;
    this.lollyCount ++;
  }

  this.IsGoalReached = function () {
    if (this.candyCount >= 10000) {
      alert('We have a winner!');
      this.hasGameEnded = true;
    }
  }


  this.init = function() {
    setInterval (function() {
      _this.plusCandyPerSecond =  Math.floor(_this.lollyCount / 10);
      if (! _this.hasGameEnded) {
        _this.candyCount += _this.plusCandyPerSecond;
        _this.displayCurrentCandies();
        _this.IsGoalReached();
      }
    }, 1000);
  };

};

var newgame = new CandyGame();
newgame.init()
