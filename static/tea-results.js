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
        // console.log(res);

        const result_headers = `<tr><th>Group</th><th>Name</th></tr>`
        results_list += result_headers

        for (const tea_item of res) {
          results_list += `<tr>`;
          const result = `<td>${tea_item['tea_group']}</td> <td>${tea_item['tea_name']}</td>`;
          results_list += result;
          // make a variable that will store an html button or link
          const add_to_favorites = `<td><a href="/tea-profile/${tea_item['tea_id']}"></a></td>`
            // link would call to a Flask route to add to user favorites
          // concatenate the variable above to results_list
          results_list += `</tr>`;
        }

        teaResults.innerHTML = results_list;
    });

}

document.querySelector('#flavor-search').addEventListener('submit', showTeaResults);