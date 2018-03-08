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
    type: String,
    index: true,
    default: Date.now
  }
});