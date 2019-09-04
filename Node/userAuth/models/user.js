var mongoose = require("mongoose");
var bcrypt = require("bcryptjs");

mongoose.connect("mongodb://127.0.0.1:27017/nodeauth", {
  useNewUrlParser: true
});

var db = mongoose.connection;

// user schema
var UserSchema = mongoose.Schema({
  username: {
    type: String,
    index: true
  },
  password: {
    type: String
  },
  email: {
    type: String
  },
  name: {
    type: String
  },
  profileimage: {
    type: String
  }
});

var User = (module.exports = mongoose.model("User", UserSchema));
module.exports.getUserById = (id, callback) => {
    User.findById(id, callback);
}
module.exports.getUserByUsername = (username, callback) => {
    var query = {username: username};
    User.findOne(query, callback);
}
module.exports.comparePassword = (canidatePassword, hash, callback) => {
    bcrypt.compare(canidatePassword, hash, (err, isMatch) => {
        callback(null, isMatch);
    });
}
module.exports.createUser = (newuser, callback) => {
  bcrypt.genSalt(10, function(err, salt) {
    bcrypt.hash(newuser.password, salt, function(err, hash) {
        newuser.password = hash;
        newuser.save(callback);
    });
  });
};
