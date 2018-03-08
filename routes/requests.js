let express = require('express');
let router = express.Router();

let RequestHistory = require('../models/requesthistory');

/* GET request page. */
router.get('/', (req, res, next) => {
  RequestHistory.find({}, (err, requesthistory) => {
    res.render('requests', { title: 'Medichain - Request History', requests: requesthistory});
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