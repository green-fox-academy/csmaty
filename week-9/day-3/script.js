'use strict';

var buttons = document.querySelectorAll('buttom')
for (var i = 0; i <= 5; i++) {
	function(i) {
		buttons[i].addEventlistener('click', function() {
			alert(i + 1);
		});
	})(i);
}