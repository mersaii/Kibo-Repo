/**
 * countSpacesInString - A function that counts the number of spaces in a given string.
 *
 * @param {string} str - The input string
 * @returns {number} - The number of spaces in the input string
 *
 * Usage:
 * const result = countSpacesInString("Hello, World!");
 * // Output: 1
 */
function countSpacesInString(str) {
    let i = 0;
    for (let char of str){
        if (char == " "){
        i++
        }
    }
    return i
}

module.exports = countSpacesInString;
