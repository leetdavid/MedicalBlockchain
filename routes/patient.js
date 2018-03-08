var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', (req, res, next) => {
  res.render('patient', { title: 'Profile - Mark Green' });
});

module.exports = router;