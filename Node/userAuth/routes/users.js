var express = require("express");
var router = express.Router();
var multer = require("multer");
var upload = multer({ dest: "./uploads" });
var User = require("../models/user");
var passport = require("passport");
var LocalStrategy = require("passport-local").Strategy;
/* GET users listing. */
router.get("/", function(req, res, next) {
  res.render("index", { title: "Members" });
});
router.get("/register", function(req, res, next) {
  res.render("register", { title: "Register" });
});
router.get("/login", function(req, res, next) {
  res.render("login", { title: "Login" });
});
router.post(
  "/login",
  passport.authenticate("local", {
    failureRedirect: "/users/login",
    failureFlash: "Invalid information"
  }),
  function(req, res) {
    req.flash("success", "You are now logged in");
    res.redirect("/");
  }
);
passport.serializeUser(function(user, done) {
  done(null, user.id);
});

passport.deserializeUser(function(id, done) {
  User.getUserById(id, function(err, user) {
    done(err, user);
  });
});

passport.use(
  new LocalStrategy((username, password, done) => {
    User.getUserByUsername(username, (err, user) => {
      if (err) throw err;
      if (!user) {
        return done(null, false, { message: "Unknown User" });
      }

      User.comparePassword(password, user.password, (err, isMatch) => {
        if (err) return done(err);
        if (isMatch) {
          return done(null, user);
        } else {
          return done(null, false, { message: "Invalid Password" });
        }
      });
    });
  })
);

router.post("/register", upload.single("profileimage"), (req, res, next) => {
  var name = req.body.name;
  var email = req.body.email;
  var username = req.body.username;
  var password = req.body.password;
  var password2 = req.body.password2;
  if (req.file) {
    console.log("uploading file");
    var profileimage = req.file.filename;
  } else {
    console.log("no image");
    var profileimage = "noimage.jpg";
  }
  // (for validator
  req.check("name", "Name is required!").notEmpty();
  req.check("email", "Email is required!").notEmpty();
  req.check("email", "Email is not valid!").isEmail();
  req.check("username", "Username is required!").notEmpty();
  req.check("password", "Password is required!").notEmpty();
  req.check("password2", "passwords do not match!").equals(req.body.password);

  // Check errors
  var err = req.validationErrors();

  if (err) {
    res.render("register", {
      errors: err
    });
  } else {
    var newUser = new User({
      name: name,
      email: email,
      username: username,
      password: password,
      profileimage: profileimage
    });

    User.createUser(newUser, (err, user) => {
      if (err) throw err;
      console.log(user);
    });
    req.flash("success", "you are now registered");
    res.location("/");
    res.redirect("/");
  }
});

router.get('/logout', (req, res) => {
  req.logout();
  req.flash('success', 'you are now logged out');
  res.redirect('/users/login');
});
module.exports = router;
