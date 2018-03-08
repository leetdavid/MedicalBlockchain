let mongoose = require('mongoose');
let Schema = mongoose.Schema;

let RequestHistorySchema = new Schema({
  //Name of source (e.g. Hong Kong General Hospital)
  sourceName: {
    type: String,
    index: true
  },
  sourceURL: {
    type: String,
    index: true
  },
  requestdate: {
    type: Date,
    default: Date.now,
    index: true
  },
  status: {
    //'REQUESTED'
    //'APPROVED'
    //'COMPLETE'
    //'DENIED'
    type: String, 
    index: true
  },
  transactiondate: {
    type: Date,
    index: true
  },
  country: {
    type: String,
    index: true
  },
  city: {
    type: String,
    index: true
  }
});

let RequestHistory = mongoose.model('RequestHistory', RequestHistorySchema, 'RequestHistory');

module.exports = RequestHistory;