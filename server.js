// Server & app requirements
const express = require("express");
const bodyParser = require("body-parser");
const app = express();

//connect to database
const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb+srv://admin:cavalier@cluster0-iwimf.mongodb.net/test?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true});

app.use(bodyParser.json());
app.use(express.static(__dirname));
app.use(bodyParser.urlencoded({
  extended: true
}));
 
// Server route handler
app.get("/", function(req, res) {
  res.sendFile(__dirname + "/index.html");
});

// Start server
app.listen(3000, function() {
  console.log("Server running on port 3000");
});


