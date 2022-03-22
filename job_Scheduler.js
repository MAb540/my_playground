import schedule from 'node-schedule';

const sendEmail = (name)=>{
    return 'Email has been sended';
}



const listOfUsers = [
    {email:'moza@gamil.com',dateOfBirth:'2022-04-21'},
    {email:'moza@gamil.com',dateOfBirth:'2022-05-24'},
    {email:'moza@gmail.com',dateOfBirth:'2022-07-08'}
]



const mainFunction = ()=>{

    listOfUsers.forEach(u =>{

    let d = new Date(u.dateOfBirth);

    let year = d.getUTCFullYear();
    let month = d.getUTCMonth() + 1; // month in js is starting from zero
    let day = d.getUTCDate();

    // schedule.scheduleJob(,)

    })

    // i want this function to run on given dates






}

