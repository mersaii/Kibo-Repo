/**
 * countCharactersInString - A function that counts the number of characters in a given string without using the length method.
 *
 * @param {string} str - The input string
 * @returns {number} - The number of characters in the input string
 *
 * Usage:
 * const result = countCharactersInString("Hello, World!");
 * // Output: 13
 */
function isEmoji(character) {
    // Regular expression to match emoji characters
    const emojiRegex = /[\p{Emoji}]/u;
    
    return emojiRegex.test(character);
}

function countCharactersInString(str) {
    var i = 0
    if (!str){
        return 0
    }

    for (let char of str){
        console.log(char, i)
        if (isEmoji(char)){
            i += 2
        }
        else i++
        }
    
    return i
}

module.exports = countCharactersInString;
