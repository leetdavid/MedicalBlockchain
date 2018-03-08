var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var index = require('./routes/index');
var users = require('./routes/users');

var patients = require('./routes/patients');  //added by Roger
var login = require('./routes/login');    //added by Roger

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

// uncomment after placing your favicon in /public
app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', patients);
//app.use('/patients', patients); //added by Roger
app.use('/users', users); 

let requests = require('./routes/requests');
app.use('/requests', requests);

let dashboard = require('./routes/dashboard');
app.use('/dashboard', dashboard);

//connect to database using mongoose
const mongoose = require('mongoose');
const dbURL = 'mongodb://medical.documents.azure.com:10255/?ssl=true&replicaSet=globaldb';
mongoose.connect(dbURL, {
    auth: {
      user: 'medical',
      password: 'Qg3c94uvojB2Fa1q2kh1ggo0jm5m2V9H66pYJCT77GfTnnWCJflmNRLSjH6S1RwcBHGdJlUSMBrZZ6jLBIqINQ=='
    }
})
.then(() => console.log(`Successfully connected to ${dbURL}!`))
.catch((err) => console.error(err));


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
