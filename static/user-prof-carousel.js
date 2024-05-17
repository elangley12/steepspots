'use strict';


//select all the carousle by the profilecarosel class

//queryselectorall - returns list of elements
const listOfFavTeas = document.querySelectorAll('.profile-carousel');
// console.log(listOfFavTeas)
if (listOfFavTeas.length > 0) {
    listOfFavTeas[0].classList.add('active');
}
    

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))