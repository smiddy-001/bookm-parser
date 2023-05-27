const express = require('express');
const cors = require('cors');
// what lets us connect to our mongodb database
const mongoose = require('mongoose');

// so we can have enviroment variables in the dotenv file
require('dotenv').config();

// how we create express sever
const app = express();
const port = process.env.PORT || 5000;

// middleware / allows to parse json
app.use(cors());
app.use(express.json());

// database uri which is obtained from mongodb dashboard
// connects to database. 
const uri = process.env.ATLAS_URI;
mongoose.connect(uri, { useNewUrlParser: true }
);
const connection = mongoose.connection;
connection.once('open', () => {
    console.log('mongodb database connection established succesfully!');
})

// Connect to routes. 
const exerciseRouter = require('./routes/exercises');
const usersRouter = require('./routes/users');

app.use('/exercises', exerciseRouter);
app.use('/users', usersRouter);

// starts server
app.listen(port, () => {
    console.log(`server is running on port: ${port}`);
});