"use-strict"

var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'test',
  password : 'test',
  database : 'todo'
});


var TodoItem = function () {
  this.id = nextId();
  this.text = "";
  this.completed = false;
}

TodoItem.prototype.update = function(attributes) {
  this.text = attributes.text || "";
  this.completed = !!attributes.completed;
};

var currId = 0;
function nextId() {
  return ++currId;
}

var items = {};

function getItem(id) {
  connection.query('SELECT FROM `todo` WHERE todo_id=?', [id], function(err, id) {
    if (err) throw err;
    console.log(id);
    return id;
  });
  // return items[id];
}

function addItem(attributes) {
  connection.query('INSERT INTO todo SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  });
}

function removeItem(id) {
  connection.query('DELETE FROM `todo` WHERE todo_id=?', [id], function(err, id) {
    if (err) throw err;
    console.log(id);
    return id;
  });
  // delete items[id];
}

function allItems() {
  connection.query('SELECT * FROM `todo`', function(err, results) {
    if (err) throw err;
    console.log(results);
    return results;
  });

  // var values = [];
  // for (var id in items) {
  //   values.push(items[id]);
  // }
  // return values;
}

module.exports = {
  get: getItem,
  add: addItem,
  remove: removeItem,
  all: allItems,
};

