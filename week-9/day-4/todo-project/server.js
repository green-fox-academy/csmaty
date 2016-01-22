"use strict"

var express = require("express");
var bodyParser = require("body-parser");
var items = require("./items.js");

var app = express();

app.use(logRequest);
app.use(express.static("public"));
app.use(bodyParser.json());

app.get("/todos", function (req, res) {
  items.all(function(result) {
  res.json(result);
  });
});

app.post("/todos", function (req, res) {
  var item = items.add(req.body);
  res.json(item);
});


app.get("/todos/:id", function (req, res) {
  items.get(req.params.id, function (item) {
    return res.json(item);
  });
});

app.put("/todos/:id", function (req, res) {
  items.update(req.params.id, function (item) {
    return res.json(item);
  });
});

app.delete("/todos/:id", function (req, res) {
  items.remove(req.params.id, function (item) {
    return res.json(item);
  });
});

app.listen(3000, function () {
  console.log("Listening on port 3000...")
});

function logRequest(req, res, next) {
  var parts = [
    new Date(),
    req.method,
    req.originalUrl,
  ];
  console.log(parts.join(" "));

  next();
}
