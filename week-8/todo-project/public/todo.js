'use strict';

var url = 'http://localhost:3000/todos'
var todoContainer = document.querySelector('.todo-container');

var listAllButton = document.querySelector('.list-all-todo-button');
listAllButton.addEventListener('click', function() {
  refreshItemsDisplay();
})

var submitTodoButton = document.querySelector('.submit-todo-button');
var addTodoInput = document.querySelector('.todo-input');
submitTodoButton.addEventListener('click', function() {
  addTodoItem();
})

var removeTodoButton = document.querySelector('.remove-todo-button');
var removeInput = document.querySelector('.remove-input');
removeTodoButton.addEventListener('click', function() {
  removeTodoItem();
})

var completedTodoButton = document.querySelector('.completed-todo-button');
var completedTodoInput = document.querySelector('.completed-todo-input');
completedTodoButton.addEventListener('click', function() {
  updateChosenItem();
})

var addTodoItem = function () {
  var newTodo = JSON.stringify({text: addTodoInput.value});
  createRequest('POST', url, newTodo, null);
  refreshItemsDisplay();
};

var removeTodoItem = function () {
  var todoUrl = url + '/' + removeInput.value
  createRequest('DELETE', todoUrl, null, null);
  refreshItemsDisplay();
};

var updateChosenItem = function () {
  var todoUrl = url + '/' + completedTodoInput.value
  createRequest('GET', todoUrl, null, setAsCompleted);
};

var setAsCompleted = function(response) {
  var chosenItem = JSON.parse(response);
  var itemtext = chosenItem.text
  var todoUrl = url + '/' + completedTodoInput.value
  var updatedTodo = JSON.stringify({text: itemtext, completed: 'true'});
  createRequest('PUT', todoUrl, updatedTodo, null)
  refreshItemsDisplay();
};

var refreshItemsDisplay = function () {
  createRequest('GET', url, null, listTodoItems);
};

var listTodoItems = function (response) {
  clearDisplay();
  var todoItems = JSON.parse(response);
  todoItems.forEach(function(e){
    var todoItem = document.createElement('p');
    if (e.completed === true) {
      var itemStatus = '[X]';
    } else {
      var itemStatus = '[_]';
    }
    todoItem.innerText = e.id + ': ' + itemStatus + '  ' + e.text;
    todoContainer.appendChild(todoItem);
  })
};

function createRequest (method, url, data, callback) {
  var httpRequest = new XMLHttpRequest();
  httpRequest.open(method, url);
  httpRequest.setRequestHeader('Content-Type', 'application/json');
  httpRequest.send(data);
  httpRequest.onreadystatechange = function() {
    if (httpRequest.readyState === 4) {
      if (callback !== null) {
        callback(httpRequest.response);
      }
    }
  };
}

function clearDisplay() {
  todoContainer.innerHTML = '';
  var inputFields = document.getElementsByTagName('input');
  for (var i = 0; i < inputFields.length; i++) {
    inputFields[i].value = '';
  }
}


function init() {
  refreshItemsDisplay();
}


init();
