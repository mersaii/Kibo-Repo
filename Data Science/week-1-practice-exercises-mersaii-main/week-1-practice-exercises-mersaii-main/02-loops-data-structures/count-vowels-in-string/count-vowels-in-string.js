/**
 * countVowelsInString - A function that counts the number of vowels in a given string.
 *
 * @param {string} str - The input string
 * @returns {number} - The number of vowels in the input string
 *
 * Usage:
 * const result = countVowelsInString("Hello, World!");
 * // Output: 3
 */

function countVowelsInString(str) {
    if (!str){
        return 0
    }
    const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    let i = 0
    // console.log(str)
    for(let char of str){
        if (vowels.includes(char)){
            // console.log(char,i)
            i++
        }
    }
    return i
}


module.exports = countVowelsInString;
