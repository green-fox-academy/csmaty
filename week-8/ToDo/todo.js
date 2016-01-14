'use strict';

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos'
var todoContainer = document.querySelector('.todo-container');

function createRequest(url, callback) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open('GET', url);
  probaRequest.send();
  probaRequest.onreadystatechange = function() {
    console.log('state: ', probaRequest.readyState);
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  };
}

var dataToSend = JSON.stringify({text: ''})

function createRequest(url, callback, dataTosSend) {
  var request = new XMLHttpRequest();
  request.open('POST', url);
  request.setRequestHeader('Content-Type', 'application/json')
  request.send(dataTosSend)
  request.onreadystatechange = function() {
    console.log('state: ', probaRequest.readyState);
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  };
}

var todoListCallBack = function (response) {
  console.log(JSON.parse(response));
  var todoArray = JSON.parse(response);
  todoArray.forEach(function(todoItem) {
    console.log(todoItem.text);
    var newTodoItem = document.createElement('p');
    // next can be done with innerHtml
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);
  })
}

// createPostRequest(url, todoListCallBack, dataToSend);
createRequest(url, todoListCallBack);
