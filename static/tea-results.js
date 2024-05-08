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

        for (const tea_item of res) {
          const result = 
            `<div class="col">
            <div class="card">
              <img src="${tea_item.tea_img}" class="card-img-top tea-cards" alt="Image of tea">
              <div class="card-body">
                <h5 class="card-title">Tea Name: ${tea_item.tea_name}</h5>
                <p class="card-text">Origin: ${tea_item.tea_origin}</p>
                <a class="btn btn-outline-dark" href="/tea-profile/${tea_item.tea_id}">Spot Tea</a>
              </div>
            </div>
          </div>`;
          results_list += result;
        }

        teaResults.innerHTML = results_list;
    });

}

document.querySelector('#origin-search').addEventListener('submit', showTeaResults);