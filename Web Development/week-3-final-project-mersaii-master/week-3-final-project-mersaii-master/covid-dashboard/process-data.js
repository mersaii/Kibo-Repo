export default function processData(covidData){
    // get total per country of cases, deaths, recovereies and time series
    let final_data = []
    covidData.forEach(countryData => {
        const eachCountry = countryData.country
        const country_totalCases = countryData.statistics.reduce((acc, curr) => acc + curr.cases, 0)
        const country_totalDeaths = countryData.statistics.reduce((acc, curr) => acc + curr.deaths, 0)
        const country_totalRecoveries = countryData.statistics.reduce((acc, curr) => acc + curr.recoveries, 0)
        // range of time series
        const country_timeRange = countryData.statistics[0].time + ' - ' + countryData.statistics[countryData.statistics.length - 1].time

        let all_data = {
            'country': eachCountry, 
            'statistics': {
            'cases': country_totalCases, 
            'deaths': country_totalDeaths,
            'recoveries': country_totalRecoveries,
            'time': country_timeRange
        }
        }

        // console.log('alldata',all_data)
        final_data.push(all_data)
    })
    // console.log('finaldata',final_data)
    return final_data
}

export function renderTable(data,id){
      const statsBody = document.getElementById(id);
      statsBody.innerHTML = '';
    //   console.log('render', data.length)
      
    
    if( data.length >1) {
        // console.log('i am here > 1')
    data.forEach(entry => {
        const country = entry.country
        let stat = entry.statistics
    // Iterate over the statistics of that country
        // Create a row for each statistic with the country information
        const statRow = document.createElement('tr');
        statRow.innerHTML = `<td>${country}</td>
                            <td>${stat.cases}</td>
                            <td>${stat.deaths}</td>
                            <td>${stat.recoveries}</td>
                            <td>${stat.time}</td>`;
        statsBody.appendChild(statRow);
    })
    // console.log(data)
    return data
}
    else if (data.length === 1) {
        // console.log('i am here = 1')
        const country = data[0];
        const stats = country.statistics
        // console.log('stats', stats)        
        // Iterate over the statistics of that country
        
        if (stats && country.statistics.length > 0){
        country.statistics.forEach(stat => {
            // Create a row for each statistic with the country information
            const statRow = document.createElement('tr');
            statRow.innerHTML = `<td>${country.country}</td>
                                <td>${stat.cases}</td>
                                <td>${stat.deaths}</td>
                                <td>${stat.recoveries}</td>
                                <td>${stat.time}</td>`;
            statsBody.appendChild(statRow);
        })
    // console.log(data)
    return data
    }

    else {
        // console.log('i am here')
        let stat = country.statistics
        const statRow = document.createElement('tr');
        statRow.innerHTML = `<td>${country.country}</td>
                            <td>${stat.cases}</td>
                            <td>${stat.deaths}</td>
                            <td>${stat.recoveries}</td>
                            <td>${stat.time}</td>`;
        statsBody.appendChild(statRow);

    }
    // console.log(data)
    return data
}}


export function filterData(data, countryInput, dateInput) {
    // console.log(countryInput, dateInput);
    if  (!countryInput && !dateInput) {
        alert('Enter country and/or date')
        return data;
    }
    else if (countryInput && !dateInput){
        // console.log('i am have country')
        const matchingEntry_country = data.find(entry => {
            const countryMatch = countryInput ? entry.country.toLowerCase().includes(countryInput) : true;

            // console.log(countryMatch);
            return countryMatch;
        });

        if (matchingEntry_country) {
            // console.log('entry', matchingEntry_country);
            return [matchingEntry_country];
        } else {
            // console.log('no entry found in data');
            return null; 
        }}

    else if (!countryInput && dateInput) {
        // console.log('i am have date')
        const matchingEntry_date = data.map(entry => {
            const countryDateMatch = entry.country
            const dateMatch = entry.statistics.find(stat => stat.time === dateInput);
            if (dateMatch){
                dateMatch['country'] = countryDateMatch
            // console.log(dateMatch);
        
                return {
                    'country': countryDateMatch,
                    'statistics': dateMatch};
            }
            // }else{
            //     let filterror = document.getElementById('filterError');
            //     filterror.append = 'Sorry, no data found for ${dateInput}. Data available is within 2021-07 to 2022-06';
            //     console.log('no entry found in data');
            //     setTimeout(function(){ filterror.innerHTML = ''; }, 3000);
            // }  
        });

        if (matchingEntry_date) {
            // console.log(matchingEntry_date.length);
            // console.log('entry', matchingEntry_date);
            
            return matchingEntry_date;
        } else {
            // console.log('no entry found in data');
            return null; 
        }}
        
    else if (countryInput && dateInput) {
        // console.log('i have both country and date');
        const matchingEntry_country = data.find(entry => {
            const countryMatch = countryInput ? entry.country.toLowerCase().includes(countryInput) : true;
            return countryMatch;
        })
        const matchingEntry_date = matchingEntry_country.statistics.find(stat => stat.time === dateInput);

        let filt = {
            'country': matchingEntry_country.country,
            'statistics': matchingEntry_date
        }

        if (matchingEntry_date) {
            // console.log('filt', filt);
            return [filt];
        }
    }
}

    // Milestone 4: Implement Sorting
    // Add clickable table headers that allow users to sort countries based on the number of cases, deaths, or recoveries.

export function sortData(data, sortBy, sortOrder) {
    // console.log('sort', sortBy, sortOrder);
    if (sortBy === 'cases') {
        console.log('sort by cases');
        const sortedData = data.sort((a, b) => {
            return sortOrder === 'asc' ? a.statistics.cases - b.statistics.cases : b.statistics.cases - a.statistics.cases;
        });
        return sortedData;
    }
    else if (sortBy === 'deaths') {
        console.log('sort by deaths');
        const sortedData = data.sort((a, b) => {
            return sortOrder === 'asc' ? a.statistics.deaths - b.statistics.deaths : b.statistics.deaths - a.statistics.deaths;
        }
        );
        // console.log('sortedData', sortedData)
        return sortedData;
    }
    else if (sortBy === 'recoveries') {
        // console.log('sort by recoveries');
        const sortedData = data.sort((a, b) => {
            return sortOrder === 'asc' ? a.statistics.recoveries - b.statistics.recoveries : b.statistics.recoveries - a.statistics.recoveries;
        }
        );
        return sortedData;
    }
    else if (sortBy === 'time') {
        // console.log('sort by time');
        const sortedData = data.sort((a, b) => {
            return sortOrder === 'asc' ? a.statistics.time - b.statistics.time : b.statistics.time - a.statistics.time;
        }
        );
        return sortedData;
    }
    else if (sortBy === 'country') {
        // console.log('sort by country');
        const sortedData = data.sort((a, b) => {
            const nameA = a.country.toLowerCase();
            const nameB = b.country.toLowerCase();
        
            return sortOrder === 'asc' ? nameA.localeCompare(nameB) : nameB.localeCompare(nameA);
        });
        // console.log('sortedData', sortedData)
        return sortedData;
    }
    else {
        // console.log('no sort');
        return data;
    }
}
