const friendStore = require('./friendStore.js');
const {sendMail} = require('./sendMail.js');

const greetFriends = ()=>{
    // read friends from file
    // filter out friends who have birthday today
    // send email

    const friends = friendStore.getFriends("./friends.json");
    let friendsWithBirthday = friends.filter(friend => friend.dateOfBirth.getDate() === new Date().getDate() && friend.dateOfBirth.getMonth() === new Date().getMonth());

    friendsWithBirthday.forEach(friend => {

        const mailOptions = {
            from:"birthdayService@gmail.com",
            to:friend.email,
            subject:"Happy Birthday",
            body:`Happy birthday, dear ${friend.firstName}!`
        }
        
    });
 

}

module.exports = {
    greetFriends
}