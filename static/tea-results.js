'use strict';
// here's a good spot to add an alert for testing connections

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

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
            <img src="${tea_item.tea_img}" class="card-img-top tea-cards" 
            data-bs-toggle="tooltip" data-bs-placement="top" 
            data-bs-custom-class="tea-img-tooltip"
            data-bs-title="${ tea_item.tea_flavor_notes }" 
            alt="Image of tea">
            <div class="card-body">
              <h5 class="card-title">${ tea_item.tea_name } (${tea_item.tea_origin})</h5>
              <h6 class="card-subtitle mb-2 text-muted">${ tea_item.tea_group } tea</h6>
              <h6 class="card-subtitle mb-2 text-muted">${ tea_item.caff_level } caffeine (${ tea_item.caff_range_mg } per cup)</h6>
              <p class="card-text">${ tea_item.tea_info }</p>
              <a class="btn btn-outline-dark" data-bs-toggle="tooltip" 
              data-bs-placement="bottom" data-bs-custom-class="spot-tea-tooltip"
              data-bs-title="click to save favorite" 
              href="/tea-profile/${ tea_item.tea_id }">Spot Tea</a>
              </div>
            </div>
          </div>`;
          results_list += result;
        }

        teaResults.innerHTML = results_list;
    });

}

document.querySelector('#origin-search').addEventListener('submit', showTeaResults);