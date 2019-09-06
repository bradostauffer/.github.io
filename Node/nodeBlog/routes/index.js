var express = require("express");
var router = express.Router();
var mongo = require('mongodb');
var monk = require('monk');
var url = 'localhost:27017/nodeblog';
var db = monk(url);

/* GET home page. */
router.get("/", function(req, res, next) {
  var d = req.db;
  var posts = d.get("posts");
  posts.find({}, {}, (err, posts) => {
    res.render("index", { posts: posts });
  });
});

module.exports = router;
