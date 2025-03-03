import './style.css'
import covidData from './covid-data'
import processData from './process-data.js'
import {renderTable,filterData,sortData} from './process-data.js'

let allData = covidData

// Milestone 1: Display Total Statistics
let totalData = processData(covidData)
let tots = renderTable(totalData,'statsBody')
// console.log('tots',tots);
let filths;

// Milestone 2: Implement Country Filter
let apply_filterbtn = document.getElementById('applyFilterBtn')

apply_filterbtn.addEventListener('click', function() {
  let filterCountry = document.getElementById('countryInput').value.toLowerCase();
  let filterDate = document.getElementById('dateInput').value;

  // Call filterData with the input values
  let filters = filterData(allData, filterCountry, filterDate);
  filths = renderTable(filters,'statsBody')
});


// Milestone 4: Implement Sorting
let apply_Sortbtn = document.getElementById('applySortBtn')
apply_Sortbtn.addEventListener('click', function() {

  const categoryDropdown = document.getElementById("categoryDropdown");
  const orderDropdown = document.getElementById("orderDropdown");

  const selectedCategory = categoryDropdown.value.toLowerCase();
  const selectedOrder = orderDropdown.value.toLowerCase();

  if (tots && !filths){
    let atots = sortData(tots, selectedCategory, selectedOrder);
    renderTable(atots,'statsBody');

   }else if (tots && filths){
    let bfilths = sortData(filths, selectedCategory, selectedOrder);
    renderTable(bfilths,'statsBody')

  }

});