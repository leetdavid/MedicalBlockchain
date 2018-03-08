let express = require('express');
let router = express.Router();

router.get('/', (req, res, next) => {
  res.render('phone_index', {title: 'Phone Sim'});
});

module.exports = router;