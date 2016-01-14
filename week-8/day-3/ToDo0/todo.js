'use strict';

var url = "https://mysterious-dusk-8248.herokuapp.com/todos";
var todoContainer = document.querySelector('.todo-container');
var newTodo = JSON.stringify({text: ''});

function createRequest (method, url, data, callback) {
  var httpRequest = new XMLHttpRequest();
  httpRequest.open(method, url);
  httpRequest.setRequestHeader('Content-Type', 'application/json');
  httpRequest.send(data);
  httpRequest.onreadystatechange = function() {
    console.log('state: ', httpRequest.readyState);
    if (httpRequest.readyState === 4) {
      callback(httpRequest.response);
    }
  };
}

var listTodoItems = function (response) {
  var todoItems = JSON.parse(response);
  todoItems.forEach(function(e){
    var todoItem = document.createElement('p');
    console.log(e);
    todoItem.innerText = e.id + ': ' + e.text + '_______' + e.completed;
    todoContainer.appendChild(todoItem);
  })
};

var refreshItemsDisplay = function () {
  createRequest('GET', url, {}, listTodoItems);
};

var addTodoItem = function () {
  createRequest('POST', url, newTodo, refreshItemsDisplay);
};

var removeTodoItem = function (response) {
  individualitem = JSON.parse(response);
  createRequest('DELETE', url, {}, listTodoItems);
}

var markTodoItemCompleted = function (response) {
  createRequest('PUT', url, {"completed": "true"}, listTodoItems);
}

// var removeTodoItem = function (response) {
//   var todoItems = JSON.parse(response);
//   todoItems.splice(index, 10)
// };




// var createTodoCallback = function (response) {
//   refreshItemsDisplay();
// }

// createRequest('POST', url, newTodo, refreshItemsDisplay);


// createRequest('DELETE', "https://mysterious-dusk-8248.herokuapp.com/todos/10", {},
//  refreshItemsDisplay);

// for (var i = 503; i <= 999; i++) {
//   var httpRequest = new XMLHttpRequest();
//   var todolink = "https://mysterious-dusk-8248.herokuapp.com/todos/" + String(i);
//   console.log(todolink);
//   httpRequest.open('DELETE', todolink);
//   httpRequest.setRequestHeader('Content-Type', 'application/json');
//   httpRequest.send();
// }

 // var httpRequest = new XMLHttpRequest();
 // httpRequest.open('DELETE', "https://mysterious-dusk-8248.herokuapp.com/todos/25");
 // httpRequest.setRequestHeader('Content-Type', 'application/json');
 // httpRequest.send();


 createRequest('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/1', {}, refreshItemsDisplay);
 refreshItemsDisplay()
