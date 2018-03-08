var express = require('express');
var router = express.Router();

let Request = require('../models/requestreal');

/* GET home page. */
router.get('/', (req, res, next) => {
  Request.find({
    'address': '0x0B45548a180a80B1d47A07b924491e0d3026E915',
    'status': 'REQUESTED'
  }, (err, requests) => {
    console.log('dug out: ' + requests);
    res.render('patientfunction', { title: 'Healthchain - Patient Dashboard' , requests: requests});
  });
});

router.post('/approve', (req, res, next) => {
  let dur = req.body.durp || req.query.durp;
  console.log('APPROVE dur: ' + dur);
  Request.findOne({
    _id: dur
  }, (err, result) => {
    if(err) {
      console.log(result);
      res.redirect('/patientfunction');
    }
    result.status = 'APPROVED';
    result.save((err) => {
      if(err){
        console.log('PROBLEM UPDATING DATA');
      }
    })
    res.redirect('/patientfunction');
  });
});

router.post('/delete', (req, res, next) => {
  let dur = req.body.durp || req.query.durp;
  console.log('DELETE dur: ' + dur);
  Request.remove({
    _id: dur
  }, (err, result) => {
    res.redirect('/patientfunction');
  });
});

module.exports = router;