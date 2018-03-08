var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', (req, res, next) => {
  function render(){
    res.render('patient', { title: 'Healthchain - Profile - Mark Green' });
  }
  setTimeout(render, 1000);
});

module.exports = router;