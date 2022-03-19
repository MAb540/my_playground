const {getFriends} = require('../friendStore');
const { assert, expect } = require("chai");
const sinon = require("sinon");
const fs = require("fs");

describe("friendStore",()=>{
    describe('getFriends',()=>{
        it('should throw error if filePath is not given',()=>{
            assert.throws(()=>getFriends(),'filePath is not given');
        })
        it("should return list of friends if filePath is given",()=>{
            
            const friends = [
                {firstName:"John", lastName:"Snow",dob: new Date(),email:"john@gmail.com"}
            ]

            const fake_readFile = sinon.fake.returns(friends);
            sinon.replace(fs,"readFile",fake_readFile);

            const result = getFriends('./friends.json');
            expect(result).to.deep.equals(friends);
            expect(fake_readFile.calledOnceWithExactly("./friends.json")).to.be.true;
        })
    })
})
