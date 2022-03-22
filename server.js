import express from "express";
import schedule from 'node-schedule';

const app = express();


const sendEmail = (name,email)=>{
    console.log(new Date().toUTCString())
    console.log(`Email has been sended to ${name} with email ${email}`);
    return 'confirmation message';
}
let count = 0;
// schedule.scheduleJob('0 20,22 * 15-21 * Tue',function(){
//     console.log(new Date().toUTCString())
//     console.log(new Date().getUTCMinutes());
//     count = count + 1;
//     console.log('The answer to life, the self, the universe and everything is count: ',count);
//     sendEmail('john','john@gmail.com')
//     console.log('running \n\n')
// })




// today is birthday of Mun,War and i want to send message to them today
// with their names and email addresses at 11:15am

// the format of data will be some thing like this
// {name:'Muz',dateOfBirth:2022-27-09}   
// const data = [
//     {name:'Muz',email:"muz@gmail.com",dateOfBirth:'2022-27-01',time:'11:15'},
//     {name:'War',email:"war@gmail.com",dateOfBirth:'2022-27-01',time:'11:16'}
// ]

// a function that takes a rule and a callback that will be executed when the rule is triggered.
// function scheduleJobUtility(rule, callback){
//     let cornPattern = '0 54,55 11 27 Jan Thu'
//     const job = schedule.scheduleJob(cornPattern,function(){
//         mainFunc(data);
//     });
// }

// function mainFunc(data){
//     data.forEach(d => {
//         sendEmail(d.name,d.email)
//     })
// }
// scheduleJobUtility();

// function testJob(data){

//    data.forEach(d =>{
//        const startTime = new Date(Date.now()+ 5000);
//        const endTime = new Date(startTime.getTime() + 120000);
//        const pattern = `0 4 8 28 Jan 0`; 
//        schedule.scheduleJob({start:startTime,end:endTime,rule:pattern},function(){
//             sendEmail(d.name,d.email);
//        })
//    })
// }
// testJob(data);




const rule = new schedule.RecurrenceRule();
rule.second = 50;
rule.minute = 49;
rule.hour = 8;
rule.date = 28
rule.month = 'January'


const job = schedule.scheduleJob(rule,function(){
    console.log("This email will be sended to you")
})



app.get('/', (req, res) => {    
    res.send('world is fine');
})


const port = 5000;
app.listen(port,()=>{
    console.log("Server is listening on port: ",port);
});
