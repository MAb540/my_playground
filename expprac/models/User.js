const mongoose = require('mongoose');

const Schema = mongoose.Schema;


const userTestSchema = new Schema({

    name:{
        type:String,
        trim:true,
        required:true,
        lowercase:true,
        default:'',
    },
    age:{
        type:Number,
    },
    address:{
        type:String,
        trim:true,
    },
    education:{
        type:String,
        trim:true,
        lowercase:true,
    }
},{
    timestamps:true
}
);

const userTests = mongoose.model('userTests',userTestSchema);

module.exports = userTests;