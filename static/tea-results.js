'use strict';


function showTeaResults(evt) {
    evt.preventDefault();
  
    // Take user tea flavor selection, package it up like this
    // TODO - change form inputs in html, grab those in js here
    const formInputs = {
      teaOrigin: document.querySelector('#tea-origin-field').value,
    };
    console.log(formInputs)
    
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

        const result_headers = 
          `<tr align='left'>
            <th>Tea Group</th>
            <th>Caffeine Range (mg)</th>
            <th>Tea Name</th>
            <th>Origin</th>
            <th>Add to Favorites</th>
          </tr>`
        results_list += result_headers

        for (const tea_item of res) {
          results_list += `<tr>`;
          const result = 
            `<td>${tea_item['tea_group']}</td>
            <td>${tea_item['caff_range_mg']}</td>
            <td>${tea_item['tea_name']}</td>
            <td>${tea_item['tea_origin']}</td>`;
          results_list += result;
          // make a variable that will store an html button or link
          const add_to_favorites = 
            `<td>
              <a href="/tea-profile/${tea_item['tea_id']}">Spot Tea</a>
            </td>`;
            // link would call to a Flask route to add to user favorites
          // concatenate the variable above to results_list
          results_list += add_to_favorites;
          results_list += `</tr>`;
        }

        teaResults.innerHTML = results_list;
    });

}

document.querySelector('#origin-search').addEventListener('submit', showTeaResults);