const countryDriveLimit = {
    'ng': 16,
    'gh': 16,
    'ke': 16,
    'us': 21,
}

const countryVoteLimit = {
    'ng': 18,
    'gh': 18,
    'ke': 18,
    'us': 21,
}

/**
 * canIDriveAndVote - A function that checks if a person can legally drive and vote based on their age.
 * @param {Object} person - a person to check
 * @param {number} person.age - the person's age
 * @param {string} person.country - a string representing the country ('gh', 'ke', 'ng', or 'us')
 * @returns {Boolean} if person with a particular age at a particular country can drive and vote 
*/

function canIDriveAndVote(person) {
    if (person.country in countryDriveLimit && person.country in countryVoteLimit){
        if (person.age >= countryDriveLimit[person.country] && person.age >= countryVoteLimit[person.country]){
            return true
        }
        else {
            return false
        }
    }else {
        return false
    }
}

module.exports = canIDriveAndVote;
