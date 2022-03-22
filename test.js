// let t = document.getElementById('test_h1');
//console.log(t.textContent)

// const getApi = () => {
//     return new Promise((resolve) => {
//       setTimeout(() => {
//         resolve(["user1", "user2", "user3"]);
//       }, 5000);
//     });
//   };

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

// name = 'John snow';
// function test(name){
//     // this.name = name;
//     console.log(this.name);
// }
// test('useEffect Hook');

// name = 'John snow';
// const testing = (name)=>{
//     this.name = name;
//     console.log(this.name)
// }
// testing('michael jordan');

// const testObj = {
//     name : "Shoaib Akhtar",
//     getName:function(){
//         console.log(this.name);
//     }
// }

// testObj.getName(); //

// const obj = {ab:'cd'};
// obj.cd = 'some value';
// const ab = 'abd';

// function ab(a){
//     return function inner(b){
//         return a + b;
//     }
// }

// let sum = ab(5);
// sum(5);

function getNumberOfWeeks(year, month) {
  let firstOfMonth = new Date(year, month, 1);
  let lastOfMonth = new Date(year, month + 1, 0);
  let used = firstOfMonth.getDay() + lastOfMonth.getDate();
  return Math.ceil(used / 7);
}

let today = new Date();

let span = document.getElementById("todayDate");
let nextBtn = document.getElementById("next_btn");
let prevBtn = document.getElementById("prev_btn");

let theadRow = document.getElementById("label-thead-row");
let tbody = document.getElementById("label-tbody");

let currentDay = Number(today.getDate());
let currentMonth = Number(today.getMonth() + 1);
let currentYear = Number(today.getFullYear());
let td = getTotalDays(today.getFullYear(), today.getMonth());

span.textContent = `${currentYear}-${currentMonth}-${currentDay}`;
tableHead();
tableBody(td);

nextBtn.addEventListener("click", nextBtnHandler);
prevBtn.addEventListener("click", prevBtnHandler);

function tableHead() {
  const arr = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
  arr.forEach((day) => {
    let td = document.createElement("td");
    td.textContent = day;
    td.classList.add("td-style");
    theadRow.appendChild(td);
  });
}

function tableBody(totalNoOfDays) {
  let noOfCols = 7;
  let noOfRows = totalNoOfDays / 7;
  let start = 1;
  let end = noOfCols;

  tbody.textContent = "";
  for (let i = 0; i < noOfRows; i++) {
    let tr = document.createElement("tr");
    tr.classList.add("table-row");

    if (end > totalNoOfDays) {
      let diff = end - totalNoOfDays;
      while (diff > 0) {
        end -= 1;
        diff -= 1;
      }
    }
    for (let j = start; j <= end; j++) {
      let td = document.createElement("td");

      td.textContent = j;
      td.classList.add("td-style");
      tr.appendChild(td);
    }
    tbody.appendChild(tr);
    start = end + 1;
    end += noOfCols;
  }
}
function setTodayMonth(year, month) {
  span.textContent = `${year}-${month}-${currentDay}`;
}

function nextBtnHandler() {
  if (currentMonth < 12) {
    currentMonth += 1;
  } else {
    currentMonth = 1;
    currentYear += 1;
  }
  let td = getTotalDays(currentYear, currentMonth - 1, 1);
  console.log(td);
  tableBody(td);
  setTodayMonth(currentYear, currentMonth);
  setTodayMonth(currentYear, currentMonth);
}

function prevBtnHandler() {
  if (currentMonth > 1) {
    currentMonth -= 1;
  } else {
    currentMonth = 12;
    currentYear -= 1;
  }
  let td = getTotalDays(currentYear, currentMonth - 1, 1);
  tableBody(td);
  setTodayMonth(currentYear, currentMonth);
  setTodayMonth(currentYear, currentMonth);
}

function getTotalDays(year, month) {
  const dateTime = new Date(year, month, 1);
  let firstDay = dateTime.getDate();
  dateTime.setMonth(month + 1, 0);
  let lastDay = dateTime.getDate();
  let totalNoOfDays = 0;

  for (let i = firstDay; i <= lastDay; i++) {
    totalNoOfDays += 1;
  }
  return totalNoOfDays;
}
