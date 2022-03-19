const fs = require('fs');

const getFriends = (filePath)=>{
    if(!filePath){
        throw new Error("filePath is not given");
    }
    const friends =  fs.readFile(filePath);
    return friends;
}

module.exports = {
    getFriends
}