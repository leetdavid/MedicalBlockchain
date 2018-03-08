let express = require('express');
let router = express.Router();

let RequestHistory = require('../models/requesthistory');
let Request = require('../models/requestreal');

/* GET request page. */
router.get('/', (req, res, next) => {
  Request.find({}, (err, requests) => {
    res.render('requests', { title: 'Medichain - Request History', requests: requests});
  });
});

/* POST (Add Request to database) */
router.post('/', (req, res, next) => {
  let newEntry = {
    "address": req.body.address,
    "duration": req.body.duration,
    "status": 'REQUESTED'
  };
  Request.create(newEntry, (err, doc) => {
    if(err) throw err;
    console.log('new entry added:' + newEntry);
    res.redirect('/requests');
  });
});

router.get('/new', (req, res, next) => {
  res.render('requests_add', {title: 'Medichain - Add Request'});
});

/* POST request page. */
router.post('/new', (req, res, next) => {
  let newEntry = {
    "sourceName": req.body.entry.sourceName,
    "sourceURL": null,
    "status": req.body.entry.status,
    "requestdate": req.body.entry.requestdate,
    "transactiondate": req.body.entry.transactiondate,
    "city": req.body.entry.city,
    "country": req.body.entry.country
  };

  RequestHistory.create(newEntry, (err, doc) => {
    if(err) throw err;
    console.log('new entry inserted:'+newEntry);
    res.redirect('/requests');
    // RequestHistory.find({}, (err, history) => {
      
    // });
  })
});

module.exports = router;