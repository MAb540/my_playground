const express = require("express");
const { getUsers, postUsers } = require("../controllers/apiController.js");
const cors = require('cors');

const apiRoute = express.Router();


const whitelist = ['http://example1.com', 'http://example2.com']
const corsOptions = {
  origin: function (origin, callback) {
    if (whitelist.indexOf(origin) !== -1 || !origin) {
      callback(null, true)
    } else {
      callback(new Error('Not allowed by CORS'))
    }
  }
} 

// apiRoute.options('*',cors(corsOptionsDelegate),(req,res) => {
//     res.statusCode(200);
// })

apiRoute.head("/", (req, res) => {
  const new_key = Math.round(Math.random(83434) * 29838990 + 1);
  const xApiKey = req.get("x-api-key");
  if (String(xApiKey) === "new-key-required") {
    res.setHeader("x-api-key", new_key);
  } else {
    res.setHeader("x-api-key", xApiKey);
  }

  console.log(new_key);

  res.setHeader("Content-Type", "application/json");
  res.setHeader("resourcetype", "json");
  res.end();
});


apiRoute.get("/",cors() ,getUsers);
apiRoute.post("/", postUsers);

module.exports = apiRoute;
