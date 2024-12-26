const mongoose = require('mongoose');

mongoose.connect(process.env.MONGODBURI, { useNewUrlParser: true, useUnifiedTopology: true });

const TrendSchema = new mongoose.Schema({
    nameoftrend1: String,
    nameoftrend2: String,
    nameoftrend3: String,
    nameoftrend4: String,
    nameoftrend5: String,
    timestamp: Date,
    ip: String,
});

module.exports =  mongoose.model('Trend', TrendSchema);