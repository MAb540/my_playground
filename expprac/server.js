const dotenv  = require('dotenv');
dotenv.config();
const express = require('express');
const http = require('http');
const db = require('./db/dbConnection.js');
const apiRoute = require('./routes/apiRoute.js');

const app = express();

app.use(express.raw());

app.use(express.json());
app.use(
  express.urlencoded({
    extended: false,
  }),
);

app.use('/users',apiRoute);

// app.get('/', (req, res) => {
//   res.send('working from new ')
// })

// app.post('/datatest', (req, res) => {

//   console.log('raw body', req.body);
//   res.send('working from new ')

  
// })


const server = http.createServer(app);
const port = process.env.PORT || 8000;

server.listen(port ,function(){
  // console.log(process.env.MONGODB_URI);
  console.log(`server is running at port ${port}`)
})