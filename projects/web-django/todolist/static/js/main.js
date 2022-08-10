const addTaskButton = document.querySelector(".btn-add-task");
const formDiv = document.querySelector(".task-form");
const taskStatus = document.querySelector(".task-status");
const updateOp = document.querySelector(".update-op");

// show task form
if (addTaskButton) {
  addTaskButton.addEventListener("click", () => {
    // use inline style to override css property.
    if (formDiv.style.display === "") {
      formDiv.style.display = "none";
    }
    formDiv.style.display =
      formDiv.style.display == "none" ? "flex" : "none";
  });
}
