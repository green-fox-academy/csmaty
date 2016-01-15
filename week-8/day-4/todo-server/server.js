'use strict'

var express = require("express");
var bodyParser = require("body-parser");
var app = express();
app.use(bodyParser.json());

var itemsList = []
var idToGiveNext = 0;

var TodoItem = function () {
  this.id = idToGiveNext;
  this.text = '';
  this.completed = false;
  this.update = function(updaterequest) {
    this.text = updaterequest.text;
    this.completed = updaterequest.completed;
  }
}

function addTodoItem(itemText) {
  var item = new TodoItem();
  item.id = idToGiveNext;
  item.text = itemText
  itemsList.push(item);
  idToGiveNext++
  return item;
}

function removeTodoItem(itemId) {
  itemsList.forEach(function(e){
    if (e.id === itemId) {
      var itemIndex = itemsList.indexOf(e);
      delete itemsList[itemIndex];
    }
  });
}


addTodoItem('csiga');
addTodoItem('biga');
addTodoItem('gye');
addTodoItem('re');
addTodoItem('ki');

// GET /todos => list all todo items
app.get('/todos', function (req, res) {
  res.json(itemsList);
});

app.post("/todos", function (req, res) {
  // var item =
  addTodoItem(req.body);
  // res.status(201).json(item);
});

app.put("/todos/:id", function (req, res) {
  var selectedItem
  itemsList.forEach(function(e){
    if (e.id === itemId) {
      selectedItem = itemsList.indexOf(e);
    }
  selectedItem.update(req.body);
  res.json(selectedItem);
});

app.delete("/todos/:id", function (req, res) {
  var selectedItem
  itemsList.forEach(function(e){
    if (e.id === itemId) {
      selectedItem = itemsList.indexOf(e);
    }
  removeTodoItem(id);
  res.json(selectedItem);
});

app.listen(3000);
