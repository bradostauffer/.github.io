const http = require("http");
const path = require("path");
const fs = require("fs");
//use "npm run dev" to start app and be run with nodemon

const server = http.createServer((req, res) => {
  /*	if(req.url === '/') {  //we know it's index page
		fs.readFile(path.join(__dirname, 'index.html'),
		(err, content) => { 
		if (err) throw err;
		res.writeHead(200, {'Conent-Type': 'text/html'});
		res.end(content);		
		})

	}
	if(req.url === '/about') {  //we know it's index page
		fs.readFile(path.join(__dirname, 'about.html'),
		(err, content) => { 
		if (err) throw err;
		res.writeHead(200, {'Conent-Type': 'text/html'});
		res.end(content);		
		})

	}
*/

  //Build filepath
  let filePath = path.join(
    __dirname,
    "public",
    req.url === "/" ? "index.html" : req.url
  ); //if / index else do req.url (ternary operator)
  console.log(filePath);

  //Extension of file
  let extname = path.extname(filePath);

  // Initial content type
  let contentType = "text/html";

  // Check ext and set accordingly
  switch (extname) {
    case ".js":
      contentType = "text/javascript";
      break;
    case ".css":
      contentType = "text/css";
      break;
    case ".json":
      contentType = "text/json";
      break;
    case ".png":
      contentType = "image/png";
      break;
    case ".jpg":
      contentType = "image/jpg";
      break;
  }

  //read file
  fs.readFile(filePath, (err, content) => {
    if (err) {
      if (err.code == "ENOENT") {
        //page not found
        fs.readFile(
          path.join(__dirname, "public", "404.html"),
          (error, content) => {
            res.writeHead(200, { "Content-Type": "text/html" });
            res.end(content, "utf8");
          }
        );
      } else {
        res.writeHead(500);
        res.end(`Server Error: ${err.code}`);
      }
    } else {
      //success
      res.writeHead(200, { "Content-Type": contentType });
      res.end(content, "utf8");
    }
  });
});
const PORT = process.env.PORT || 5000; //will run it on clients eviornment var or 5000 if
//not found
server.listen(PORT, () => console.log(`Server running on port ${PORT}`));
