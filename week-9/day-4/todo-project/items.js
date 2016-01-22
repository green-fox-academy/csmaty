"use-strict"

var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'test',
  password : 'test',
  database : 'todo'
});


function addItem(attributes) {
  connection.query('INSERT INTO todolist SET ?', attributes, function(err, result) {
    if (err) throw err;
  });
}

function removeItem(id, callback) {
  connection.query('DELETE FROM `todolist` WHERE id=?', [id], function(err, result) {
    if (err) throw err;
    console.log(result);
    callback(result)
  });
}


function allItems(callback) {
  connection.query('SELECT * FROM `todolist`', function(err, results) {
    if (err) throw err;
    callback(results);
  });
}

function updateItem(id, callback) {
  connection.query('UPDATE todolist SET COMPLETED=true WHERE id=?', [id], function(err, result) {
    if (err) throw err;
    callback(result)
  });
}

function getItem(id, callback) {
  connection.query('SELECT * FROM todolist WHERE id=?', id, function(err, result) {
    if (err) throw err;
    callback(result);
  });
}

module.exports = {
  get: getItem,
  add: addItem,
  remove: removeItem,
  all: allItems,
  update: updateItem
};
