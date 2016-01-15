'use strict';

var url = "https://mysterious-dusk-8248.herokuapp.com/todos";
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

var updateChosenItem = function () {
  var todoUrl = url + '/' + completedTodoInput.value
  createRequest('GET', todoUrl, null, setAsCompleted);
};

var setAsCompleted = function(response) {
  var chosenItem = JSON.parse(response);
  var itemtext = chosenItem.text
  var todoUrl = url + '/' + completedTodoInput.value
  var updatedTodo = JSON.stringify({text: itemtext, completed: 'true'});
  createRequest('PUT', todoUrl, updatedTodo, displayModified)
};

var removeTodoItem = function () {
  var todoUrl = url + '/' + removeInput.value
  createRequest('DELETE', todoUrl, null, displayModified);
};

var addTodoItem = function () {
  var newTodo = JSON.stringify({text: addTodoInput.value});
  createRequest('POST', url, newTodo, displayModified);
};

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

var displayModified = function(response) {
  var modifiedItem = JSON.parse(response);
  todoContainer.innerHTML = ''
  var todoItem = document.createElement('p');
  todoItem.innerText = modifiedItem.id + ': ' + modifiedItem.text + '  [' + modifiedItem.completed + ']'
  todoContainer.appendChild(todoItem);
};

var listTodoItems = function (response) {
  var todoItems = JSON.parse(response);
  todoContainer.innerHTML = ''
  todoItems.forEach(function(e){
    var todoItem = document.createElement('p');
    todoItem.innerText = e.id + ': ' + e.text + '  [' + e.completed + ']';
    todoContainer.appendChild(todoItem);
  })
};

var refreshItemsDisplay = function () {
  // clearInputfields();
  createRequest('GET', url, {}, listTodoItems);
};

function clearInputfields() {
  var inputfields = document.getElementsById('input')
  inputfields.reset();
};
