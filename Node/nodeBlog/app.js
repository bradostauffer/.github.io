var createError = require("http-errors");
var express = require("express");
var path = require("path");
var cookieParser = require("cookie-parser");
var logger = require("morgan");
var indexRouter = require("./routes/index");
var postsRouter = require("./routes/posts");
var categoriesRouter = require('./routes/categories');
var session = require("express-session");
var moment = require("moment");
var expressValidator = require("express-validator");
var flash = require('connect-flash');
var mongo = require('mongodb');
var monk = require('monk');
var url = 'localhost:27017/nodeblog';
var db = monk(url);
var app = express();

app.locals.moment = require('moment');
app.locals.truncateText = (text, length) => {
  var truncatedText = text.substring(0, length);
  return truncatedText;
}
// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, "public")));

// Handle Sessionssss
app.use(
  session({
    secret: "secret",
    saveUninitialized: true,
    resave: true
  })
);

// Validator
app.use(
  expressValidator({
    errorFormatter: function(param, msg, value) {
      var namespace = param.split("."),
        root = namespace.shift(),
        formParam = root;

      while (namespace.length) {
        formParam += "[" + namespace.shift() + "]";
      }
      return {
        param: formParam,
        msg: msg,
        value: ""
      };
    }
  })
);

// connect flash
app.use(flash());
app.use((req, res, next) => {
  res.locals.messages = require("express-messages")(req, res);
  next();
});
// make db accessible to our router
app.use((req, res, next) => {
  req.db = db;
  next();
});

app.use("/", indexRouter);
app.use("/posts", postsRouter);
app.use("/categories", categoriesRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get("env") === "development" ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render("error");
});

module.exports = app;
