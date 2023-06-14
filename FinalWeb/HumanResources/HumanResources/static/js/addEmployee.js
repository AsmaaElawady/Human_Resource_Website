function validateForm() {
  let EmployeeName = document.getElementById("EmployeeName").value;
  let number = document.getElementById("Phonenumber").value;
  let email = document.getElementById("email").value;
  let id = document.getElementById("EmployeeID").value;
  var nameformat = /^[ a-zA-Z]+$/;

  var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  var phoneformt = /^\(?([0-9]{4})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;

  if (
    EmployeeName == null ||
    EmployeeName == "" ||
    !EmployeeName.match(nameformat)
  ) {
    alert("Employee Name isn't Valid");
    return false;
  } else if (!number.match(phoneformt) || number == "" || number == null) {
    alert("The PhoneNumber isn't Valid");
    return false;
  } else if (!email.match(mailformat) || email == "" || email == null) {
    alert("The Email isn't Valid");
    return false;
  } else if (id < 1 || id >= 100000000 || id == "" || id == null) {
    alert("The ID isn't Valid");
    return false;
  } else {
    return true;
  }
}

function addemployee()
{
    var Add=alert("Employee Added Successfully");
}

// function signup(e) {
//   event.preventDefault();
//   var EmployeeName = document.getElementById("EmployeeName").value;
//   var EmployeeID = document.getElementById("EmployeeID").value;
//   var email = document.getElementById("email").value;
//   var Phonenumber = document.getElementById("Phonenumber").value;
//   var Addres = document.getElementById("Addres").value;
//   var Salary = document.getElementById("Salary").value;
//   var NumberVacation = document.getElementById("a1").value;
//   var NumberApprovedVacation = document.getElementById("a2").value;
//   var Date = document.getElementById("Date").value;
//   var Gender = document.querySelector("input[name=gender]:checked").value;
//   var Status = document.querySelector("input[name=statue]:checked").value;
//   var MARITALSTATUE = document.querySelector(
//     "input[name=MaritalStatue]:checked"
//   ).value;


//   var user = {
//     EmployeeName: EmployeeName,
//     EmployeeID: EmployeeID,
//     email: email,
//     Phonenumber: Phonenumber,
//     Addres: Addres,
//     Salary: Salary,
//     a1: NumberVacation,
//     a2: NumberApprovedVacation,
//     Date: Date,
//     gender: Gender,
//     statue: Status,
//     MaritalStatue: MARITALSTATUE,

//   };

//   var json = JSON.stringify(user);
//   localStorage.setItem(EmployeeName, json);
//   console.log("user added");
// }
