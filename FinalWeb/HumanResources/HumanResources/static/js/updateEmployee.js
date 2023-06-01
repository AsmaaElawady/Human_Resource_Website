console.log("problem unknown")
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if the cookie name matches the provided name
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function loadDoc() {
    console.log("the problem is ");
    var name = document.getElementById("new").innerHTML;
    var id = document.getElementById("newID").innerHTML;
    var mail = document.getElementById("mail").innerHTML;
    var phone = document.getElementById("num").innerHTML;
    var add = document.getElementById("a").innerHTML;
    var salary = document.getElementById("s").innerHTML;
    var vacdays = document.getElementById("vacdays").innerHTML;
    var appdays = document.getElementById("approved").innerHTML;

    var xhttp = new XMLHttpRequest();
    xhttp.open('POST','/updaterecord/',true);
    xhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhttp.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
    xhttp.onreadystatechange = function()
    {
        if(xhttp.status === 200 && xhttp.readyState === 4)
        {
            console.log("employee updated successfully");
            window.location.href='/editinfo.html';
        }
        else
        {
            console.error('error updating employee: ' + xhttp.status);

        }
        xhttp.send('new=' + encodeURIComponent(name) + '&newID='+ encodeURIComponent(id) 
        + '&num='+ encodeURIComponent(phone) + '&a='+ encodeURIComponent(add) 
        + '&s='+ encodeURIComponent(salary)  + '&mail='+ encodeURIComponent(mail) 
        + '&vacdays='+ encodeURIComponent(vacdays)  + '&approved='+ encodeURIComponent(appdays)
        );
    }

}
// function confirmDelete()
// {
//     var con = confirm("Are you sure you want to delete this Employee?");
//     return con;
// }

// function alertuserName()
// {
//     alert("userName is required");
// }

// function alertID()
// {
//     alert("ID is required");
// }

// function removefromstorage(idd)
// {
//     console.log(idd);
//     if (confirmDelete())
//     {
//         localStorage.removeItem(idd);
//         console.log(idd);
//     }
// }

// let nameInput = document.querySelector("[name = 'userName']")
// let idInput = document.querySelector("[name = 'ID']")


// document.forms[0].onsubmit = function(e){
//     let userValid = false;
//     let IdValid = false;
    
//     if(nameInput.value === "" || nameInput.value === null)
//     {
//         userValid = false;
//         alertuserName();
//     }
//     else if(idInput.value === "" || idInput.value === null)
//     {
//         IdValid = false;
//         alertID();
//     }
//     else
//     {
//         userValid = true;
//         IdValid = true;
//         if(!store())
//         {
//             e.preventDefault();
//         }
//     }
    
//     if(userValid === false || IdValid === false)
//     {
//         e.preventDefault();
//     }

//     else if( userValid === true && IdValid === true)
//     {
//         var idstr = document.getElementById("us1").value ;
//         const empfromstore = localStorage.getItem(idstr);
//         var parsedobj = JSON.parse(empfromstore);
//         var tempname = parsedobj["EmployeeName"];
//         console.log(parsedobj["EmployeeName"]);
//         console.log(tempname);
//         localStorage.setItem("currentupdate", tempname)

//     }
// }


// document.forms[1].onsubmit = function(e){
//     let userValid = false;
//     let IdValid = false;
    
//     if(nameInput.value === "" || nameInput.value === null)
//     {
//         userValid = false;
//         alertuserName();
//     }
//     else if(idInput.value === "" || idInput.value === null)
//     {
//         IdValid = false;
//         alertID();
//     }
//     else
//     {
//         userValid = true;
//         IdValid = true;
//         if(!store())
//         {
//             e.preventDefault();
//         }
//     }
//     if(userValid === false || IdValid === false)
//     {
//         e.preventDefault();
//     }
//     else if(userValid === true && IdValid === true)
//     {
//         const btn1 = document.getElementById('delete');
//         btn1.addEventListener("click", removefromstorage(idd));

//     }
// }

// function store()
// {
// idd = document.getElementById('us1').value;
// inputID = document.getElementById('id1').value;

// var test = localStorage.getItem(idd);

// if( test === null)
// {
//     document.getElementById("iderror").innerText = "sorry this employee doesn't exist";
//     return false;
// }
// else
// {
//     var tempobj  = JSON.parse(test);
//     var matchId = tempobj["EmployeeID"];
//     if(inputID === matchId)
//     {
//         return true;
//     }
//     else
//     {
//         document.getElementById("iderror").innerText = "sorry this employee doesn't exist";
//         return false;
//     }
// }

// }

