const searchForm = document.querySelector("#searchForm")
      const searchResaultContainer = document.querySelector("#searchResults")

      //put event listener to see the sumbtion
      searchForm.addEventListener("submit", function (event) {
          event.preventDefault();

          const employeeName = document.getElementById('empName').value;



          $.post("/getEmployee/", { eName: employeeName }, (data) => {

              searchResaultContainer.innerHTML = data;


          });

      });

console.log("zeh2t");
