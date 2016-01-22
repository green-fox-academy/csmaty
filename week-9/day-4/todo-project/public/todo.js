'use strict';

var url = 'http://localhost:3000/todos'
var todoContainer = document.querySelector('.todo-container');

var submitTodoButton = document.querySelector('.submit-todo-button');
var addTodoInput = document.querySelector('.todo-input');
submitTodoButton.addEventListener('click', function() {
  addTodoItem();
})

var addTodoItem = function () {
  var newTodo = JSON.stringify({text: addTodoInput.value});
  createRequest('POST', url, newTodo, null);
  refreshItemsDisplay();
};

var removeTodoItem = function (id) {
  var todoUrl = url + '/' + id;
  createRequest('DELETE', todoUrl, null, null);
  refreshItemsDisplay();
};

var updateChosenItem = function (id) {
    var updateStatus = JSON.stringify({completed: 'true'});
    var todoUrl = url + '/' + id
    createRequest('PUT', todoUrl, null, null);
    refreshItemsDisplay();
};

var refreshItemsDisplay = function () {
  createRequest('GET', url, null, listTodoItems);
};

var listTodoItems = function (response) {
  clearDisplay();
  var todoItems = JSON.parse(response);
  todoItems.forEach(function(item){
    var newTodoLine = document.createElement('div');
    newTodoLine.setAttribute('class', 'todo-line')

    var completedIcon = document.createElement('button')
    completedIcon.innerText = 'COMPL';
    completedIcon.setAttribute('class', 'completed-icon')
    completedIcon.setAttribute('id', item.id);
    newTodoLine.appendChild(completedIcon);
    completedIcon.addEventListener('click', function() {
      var id = event.target.id;
      updateChosenItem(id);
    })
    
    var todoItem = document.createElement('p');
    if (item.completed == true) {
      var itemStatus = '[X]';
    } else {
      var itemStatus = '[_]';
    }
    todoItem.innerText = itemStatus + '  ' + item.text;
    newTodoLine.appendChild(todoItem);

    var deleteIcon = document.createElement('button')
    deleteIcon.setAttribute('class', 'delete-icon')
    deleteIcon.innerText = 'DEL';
    deleteIcon.setAttribute('id', item.id);
    newTodoLine.appendChild(deleteIcon);
    deleteIcon.addEventListener('click', function() {
      var id = event.target.id;
      removeTodoItem(id);
    })

    todoContainer.appendChild(newTodoLine);
  })
};

function deletebybutton(id) {
  var todoUrl = url + '/' + id;
  createRequest('DELETE', todoUrl, null, null);
  refreshItemsDisplay();
}

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

