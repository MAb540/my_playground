
async function test(){
  let res = await fetch('http://localhost:8000/users');

  let data = await res.json();

  console.log(data)

}


test().then(r => console.log(r));








// get User function that returns a list of users
// function getUsers() {
//   return new Promise((resolve) => {
//     setTimeout(() => {
//       resolve(["user1", "user2", "user3"]);
//     }, 3000);
//   });
// }



// function mainFunc() {
//   getUsers().then((users) => console.log(users));
//   console.log("executed");
// }
// mainFunc();

// async function mainFunc2() {
//   let users = await getUsers();
//   console.log(users);
//   console.log("executed");
// }
// mainFunc2();













// function getUserDetails(name) {
//     return new Promise((resolve) => {
//       setTimeout(() => {
//         resolve(`This is ${name} details`);
//       }, 3000);
//     });
// }


// function mainFuncDetails() {
//   getUsers().then((users) => {
//     for (let user of users) {
//       getUserDetails(user)
//         .then((userDetails) => console.log(userDetails));
//     }
//   });
// }
// // mainFuncDetails();

// async function mainFuncDetails2(){
//     const users = await getUsers();
//     for(let user of users){
//         let userDetails = await getUserDetails(user);
//         console.log(userDetails);
//     }
// }
// // mainFuncDetails2();


// function sum(num1, num2){
//     return num1 + num2;
// }
// // console.log(sum(2,3));


// async function asyncSum(num1, num2){
//     return num1 + num2;
// }

// console.log(asyncSum(2,3));
// asyncSum(2,3).then(r => console.log(r));










