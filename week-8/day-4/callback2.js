'use strict'

function runvin5seconds(callback) {
  setTimeout(callback, 5000);
}

runvin5seconds(function() {
  console.log('jeej');
});
