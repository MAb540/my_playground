const sinon = require('sinon');
const { expect } = require('chai');

const friendStore = require('../friendStore');
const { greetFriends } = require('../birthdayService');
const mailService = require('../mailService');


describe('birthdayService', () => {

    describe('greetFriends', () => {

        // test('should call getFriends from friendStore', () => {

        //     const fake_getFriends = sinon.fake();
        //     sinon.replace(friendStore, 'getFriends', fake_getFriends);

        //     greetFriends();

        //     expect(fake_getFriends.calledOnceWithExactly('./friends.json')).to.be.true;

        // })

        test("should send mail to friends who have birthday today",()=>{

            const friends = [
                {
                    firstName:"saurabh",
                    lastName:"saur",
                    dob: new Date(1998,new Date().getMonth(),new Date().getDate()),
                    email:"saurabh@gmail.com"
                }
            ];

            const fake_getFriends = sinon.fake.returns(friends);
            sinon.replace(friendStore,"getFriends",fake_getFriends);


            const fake_sendMail = sinon.fake();
            sinon.replace(mailService,'sendMail',fake_sendMail);
            greetFriends();


            expect(fake_getFriends.calledOnceWithExactly('./friends.json')).to.be.true;

            const mailOptions = {
                from:"",
                to:friends[0].email,
                subject:"Happy Birthday",
                body:`Happy birthday, dear ${friends[0].firstName}!`
            }


            expect(fake_sendMail.calledOnceWithExactly(mailOptions)).to.be.true;

        })



    })

})
