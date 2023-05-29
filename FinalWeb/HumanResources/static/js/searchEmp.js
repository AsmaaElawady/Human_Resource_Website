
function validate(){
     let empName = document.getElementById('empName').value;

   if(!empName){
    alert("Enter name to search");
    return false
   }
   return true;
}
// searchButton.addEventListener('click', function(event) {
//
//    // Prevent the form from submitting
//    event.preventDefault();
//
//
//    // Get the value entered by the user
//
// });