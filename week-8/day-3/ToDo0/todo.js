'use strict';

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos'
var todoContainer = document.querySelector('.todo-container');
var dataToSend = JSON.stringify({text: ''})

function createRequest(url, callback) {
  var httpRequest = new XMLHttpRequest();
  httpRequest.open('GET', url);
  httpRequest.send();
  httpRequestRequest.onreadystatechange = function() {
    console.log('state: ', httpRequest.readyState);
    if (httpRequest.readyState === 4) {
      callback(httpRequest.response);
    }
  };
}

function createPostRequest(method, url, callback, dataTosSend) {
  var httpRequest = new XMLHttpRequest();
  httpRequest.open(method, url);
  httpRequest.setRequestHeader('Content-Type', 'application/json')
  httpRequest.send(dataTosSend)
  httpRequest.onreadystatechange = function() {
    console.log('state: ', httpRequest.readyState);
    if (httpRequest.readyState === 4) {
      callback(httpRequest.response);
    }
  };
}

var todoListCallBack = function (response) {
  // console.log(JSON.parse(response));
  var todoArray = JSON.parse(response);
  todoArray.forEach(function(todoItem) {
    console.log(todoItem.text);
    var newTodoItem = document.createElement('p');
    // next can be done with innerHtml
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);
  })
}

// createPostRequest('POST', url, todoListCallBack, dataToSend);
createRequest(url, todoListCallBack);
