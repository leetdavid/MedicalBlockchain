let mongoose = require('mongoose');
let Schema = mongoose.Schema;

let RequestHistorySchema = new Schema({
  sourceName: {
    type: String,
    index: true
  },
  sourceURL: {
    type: String,
    index: true
  },
  uuid: {
    type: String,
    index: true
  },
  requestdate: {
    type: Date,
    default: Date.now,
    index: true
  },
  status: {
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