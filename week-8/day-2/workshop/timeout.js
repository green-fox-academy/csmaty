'use strict'

var isEnd = false;
setTimeout(function() {
  console.log('yayy!');
  isEnd = true;
}, 0);

function end() {
  console.log('end!');
  console.log('endebb');
}

end();

while (!isEnd) {}
