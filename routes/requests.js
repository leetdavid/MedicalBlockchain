let express = require('express');
let router = express.Router();

let RequestHistory = require('../models/requesthistory');

/* GET request page. */
router.get('/', (req, res, next) => {
  RequestHistory.find({}, (err, requesthistory) => {
    res.render('requests', { title: 'Express', requests: requesthistory});
  });
});

/* POST request page. */
router.post('/', (req, res, next) => {
  
});

module.exports = router;