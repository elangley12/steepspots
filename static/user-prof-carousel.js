'use strict';

//select all the carousle by the profilecarosel class

//queryselectorall - returns list of elements
const listOfFavTeas = document.querySelectorAll('.profile-carousel');
// console.log(listOfFavTeas)
if (listOfFavTeas.length > 0) {
    listOfFavTeas[0].classList.add('active');
}
    

//only add the active class to the first one in the list
// look at js dom lecture