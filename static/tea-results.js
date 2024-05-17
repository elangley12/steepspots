'use strict';
// here's a good spot to add an alert for testing connections

let tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
let tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// lst1 = [1,2,3]
// lst2 = [4,5,6]
// lst2.append(7) => modify python lists freely

// in js, to modify things made with const, we have to make a copy

// [...tooltipTriggerList] => take a copy of every single item in this Array, in the same index order

// let sessionObj = {'key': 'value', 'currUser': 'user1'}
// sessionObj = { ... sessionObj, 'currUSer': None }
// sessionObj['currUser'] = None // this is still good syntax

// ... == "Spread Operator"

// tooltipTriggerList => Array() => [<tooltip>,<tooltip>,<tooltip>,</tooltip>]

// tooltipTriggerList.map => for item in array, do this
// iterate over the entire list and do this thing

// // [].map( iterable => what to do with that iterable )
// [...tooltipTriggerList].iterate(function callBack(tooltipTriggerEl) {
//     return new bootstrap.Tooltip(tooltipTriggerEl)
//   });


function showTeaResults(evt) {
    console.log(evt);
    evt.preventDefault();
    console.log("Show tea results function hit")
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
            data-bs-title="${tea_item.tea_flavor_notes}" 
            alt="Image of tea">
            <div class="card-body">
              <h5 class="card-title">${tea_item.tea_name} (${tea_item.tea_origin})</h5>
              <h6 class="card-subtitle mb-2 text-muted">${tea_item.tea_group} tea</h6>
              <h6 class="card-subtitle mb-2 text-muted">${tea_item.caff_level} caffeine (${ tea_item.caff_range_mg } per cup)</h6>
              <p class="card-text">${tea_item.tea_info}</p>
              <a class="btn btn-outline-dark" data-bs-toggle="tooltip" 
              data-bs-placement="bottom" data-bs-custom-class="spot-tea-tooltip"
              data-bs-title="click to save favorite" 
              href="/tea-profile/${tea_item.tea_id}">
                <img src=" ../static/images/spot-tea.svg" id="spot-tea-icon">
                spot
              </a>
              </div>
            </div>
          </div>`;
          results_list += result;
        }

        teaResults.innerHTML = results_list;
        tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
        tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
    });

}

document.querySelector('#origin-search').addEventListener('submit', showTeaResults);