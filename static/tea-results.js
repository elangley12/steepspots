'use strict';

function showTeaResults(evt) {
    evt.preventDefault();
  
    // Take user tea flavor selection, package it up like this
    const formInputs = {
      tea_flavor: document.querySelector('#tea-flavor-field').value,
    };

    // need to write route for this (see server.py for notes). put jsonified result from server here
  fetch('/order-melons.json', {
    method: 'POST',
    body: JSON.stringify(formInputs),
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then((response) => response.json())
    .then(updateMelons);
    // Need to make a function above that checks for existing children, 
    // erase them, display the new results using document.querySelector and 
    // insertAdjacent instead (see links from Trew!!)
}

document.querySelector('#flavor-search').addEventListener('submit', showTeaResults);