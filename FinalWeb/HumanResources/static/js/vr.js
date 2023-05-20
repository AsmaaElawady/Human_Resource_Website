
// Create a table element
let table = document.createElement('table');
localStorage.removeItem("currentupdate");
localStorage.removeItem("currentName");

// Create a table head element
let thead = document.createElement('thead');
let headerRow = document.createElement('tr');
let headerCell1 = document.createElement('th');
let headerCell2 = document.createElement('th');
let headerCell3 = document.createElement('th');
//let headerCell4 = document.createElement('th');
//headerCell4.textContent = 'Status';
headerCell1.textContent = 'Name';
headerCell2.textContent = 'status ';
headerCell3.textContent='status';
headerRow.appendChild(headerCell1);
headerRow.appendChild(headerCell2);
headerRow.appendChild(headerCell3);
//headerRow.appendChild(headerCell4);

thead.appendChild(headerRow);
table.appendChild(thead);

for(var i =0; i < localStorage.length; i++){
  var k = localStorage.key(i);
  let empInfo =(localStorage.getItem(k));
  let employeeInfo = JSON.parse(empInfo);
  if(employeeInfo.hasOwnProperty('fromDate') && employeeInfo.status === "submitted" ){
    // Create a table row for each property in the employee object
    let row = document.createElement('tr');
    let cell1 = document.createElement('td');
    let cell2 = document.createElement('td');
    cell1.textContent = employeeInfo.EmployeeName;
    let cell3 = document.createElement('td');
    let cell4 = document.createElement('td');
    let anchor = document.createElement('a');
    //create a text node and assign it to the "link" variable.
    let textNode = document.createTextNode(cell1.textContent);
    let btninput = document.createElement('input');
    btninput.type = 'button';
    btninput.value = 'Approve'
    btninput.id = 'ap';
    let btninput2 = document.createElement('input');
    btninput2.type = 'button';
    btninput2.value = 'Reject';
    btninput2.id2 = 'ap';
    stat = "s"
    cell2.appendChild(btninput);
   // cell3.appendChild(btninput);
    cell2.appendChild(btninput2);
    cell3.appendChild(btninput2);
    // Append the textNode as a child to anchor.
    anchor.appendChild(textNode);
    anchor.href = "vacation_form.html";

    row.appendChild(anchor);
    row.appendChild(cell2);
    row.appendChild(cell3);
    //row.appendChild(cell4);
    table.appendChild(row);

    anchor.onclick = function(){
      localStorage.setItem('currentName', cell1.textContent);
    }
    btninput.onclick = function()
    {
      employeeInfo.status  = "Approved";
      let date1 = new Date(employeeInfo.toDate) ;
      let date2  = new Date(employeeInfo.fromDate) ;
      let difference = date1.getDate() - date2.getDate();
      if( difference>=0 && employeeInfo.a1>difference)
      {
        let tempnum=parseInt(employeeInfo.a1) - difference;
        employeeInfo.a1 = tempnum;
        let tempnum2 = parseInt(employeeInfo.a2)  +difference;
        employeeInfo.a2 = tempnum2;
        let tempn = employeeInfo.EmployeeName;
        emp = JSON.stringify(employeeInfo);
        localStorage.setItem(tempn , emp);
        console.log("you approved the request");
        table.removeChild(row);
      }
    }
    btninput2.onclick = function()
    { 
      employeeInfo.status  = "Rejected";

      console.log("you rejected the request");
      table.removeChild(row);
    }
    // Append the table to the search results container
    let searchResultsContainer = document.getElementById('searchResults');
    searchResultsContainer.innerHTML = '';
    searchResultsContainer.appendChild(table);
  }

}