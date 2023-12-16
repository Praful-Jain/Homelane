// `.dataset` property is used to access the data attributes associated with a particular element.
// The `dataset` property is an object that contains all the data attributes of the element.
document.addEventListener("DOMContentLoaded", function () {
    var start_index = document.getElementById('tableBody').dataset.startIndex;
    var indexCells = document.getElementsByClassName("index-cell");
    console.log("Start Index:", start_index);
    for (var i = 0; i < indexCells.length; i++) {
        indexCells[i].textContent = parseInt(start_index) + i;
    }
});

