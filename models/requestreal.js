let mongoose = require('mongoose');
let Schema = mongoose.Schema;

let RequestSchema = new Schema({
  address: {
    type: String,
    index: true
  },
  duration: {
    type: Number,
    index: true
  },
  status: {
    //REQUESTED
    //APPROVED
    //COMPLETE
    //DENIED
    type: String,
    index: true
  },
  timestamp: {
    type: Date,
    index: true,
    default: Date.now
  },
  requestor: {
    type: String,
    index: true,
    default: "Dr. Demo"
  }
});

let Request = mongoose.model('Request', RequestSchema, 'Request');

module.exports = Request;