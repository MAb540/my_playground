const dotenv  = require('dotenv');
dotenv.config();

const mongoose = require('mongoose');

//DB connection


// const db_url = 'mongodb+srv://MAb:messi@myfirstcluster.afjzk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });
  const db = mongoose.connection;
  db.on('error', console.error.bind(console, 'connection error:'));
  db.once('open', function () {
    // we're connected!
    console.log('db connected');
  });