'use strict';

function showTeaResults(evt) {
    evt.preventDefault();
  
    // Take user tea flavor selection, package it up like this
    const formInputs = {
      tea_flavor: document.querySelector('#tea-flavor-field').value,
    };
    console.log(formInputs)
    // need to write route for this (see server.py for notes). put jsonified result from server here
  fetch('/tea-results.json', {
    method: 'POST',
    body: JSON.stringify(formInputs),
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then((response) => response.json())
    .then((res) => { // this `res` is the jsonified `results` from the server
        let teaResults = document.querySelector('#tea-results');
        let results_list = "";
        console.log(res);

        const result_headers = `<tr><th>Group</th><th>Name</th></tr>`
        results_list += result_headers

        for (const tea_item of res) {
          const result = `<tr><td>${tea_item['tea_group']}</td> <td>${tea_item['tea_name']}</td></tr>`;
          results_list += result;
        }

        teaResults.innerHTML = results_list;
    });

}

document.querySelector('#flavor-search').addEventListener('submit', showTeaResults);