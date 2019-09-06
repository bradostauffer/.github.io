var express = require("express");
var router = express.Router();
var mongo = require("mongodb");
var monk = require("monk");
var url = "localhost:27017/nodeblog";
var db = monk(url);


router.get("/show/:category", function(req, res, next) {
  var posts = db.get("posts");

  posts.find({category: req.params.category}, {}, function(err, posts) {
    res.render("index", {
      title: req.params.catrgory,
      "posts": posts
    });
  });
});
router.get("/add", function(req, res, next) {
  res.render("addcategory", {
    title: "Add Category"
  });
});

router.post("/add", function(req, res, next) {
  // Get form values
  var name = req.body.name;


  // Form Validation
  req.check("name", "name is required").notEmpty();

  // Check errors
  var err = req.validationErrors();
  if (err) {
    res.render("addcategory", {
      errors: err
    });
  } else {
    var categories = db.get("categories");
    categories.insert(
      {
          "name":name
      },
      (err, categories) => {
        if (err) {
          res.send(err);
        } else {
          req.flash("success", "Category Added");
          res.location("/");
          res.redirect("/");
        }
      }
    );
  }
});

module.exports = router;
