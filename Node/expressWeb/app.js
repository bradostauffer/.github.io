const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const nodemailer = require("nodemailer");

var app = express();

app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname + "/public")));
app.get("/", (req, res) => {
  res.render("index", { title: "Welcome" });
});
app.get("/about", (req, res) => {
  res.render("about");
});
app.get("/contact", (req, res) => {
  res.render("contact");
});
app.post("/contact/send", (req, res) => {
  var trasporter = nodemailer.createTransport({
    service: "Gmail",
    auth: {
      user: "bradostauffer@gmail.com",
      pass: "brado1998"
    }
  });
  var mailOptions = {
    from: "Brado Stauffer <bradostauffer@gmail.com>",
    to: "bradotornado1@gmail.com",
    subject: "Website Submission",
    text:
      "You have a submission with the following details...Name: " +
      req.body.name +
      "Email" +
      req.body.email +
      "message" +
      req.body.message,
    html:'<p>You have a submission with the following details...</p><ul><li>Name:'+req.body.name+'</li><li>Email: '+req.body.email+'</li><li>Message: '+req.body.message+'</li></ul>'
  };
  trasporter.sendMail(mailOptions, (err, info) => {
      if(err) {
          console.log(err);
          res.redirect('/');
      } else {
          console.log('message sent' + info.response);
          res.redirect('/');
      }
  })
});
app.listen(3000);
console.log("server is running on port 3000");
