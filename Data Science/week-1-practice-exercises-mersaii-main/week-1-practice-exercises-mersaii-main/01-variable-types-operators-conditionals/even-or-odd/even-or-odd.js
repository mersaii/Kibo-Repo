/**
 * evenOrOdd - A function that determines if a given number is even or odd.
 *
 * @param {number} num - The number to be checked
 * @returns {string} - "even" if the number is even, "odd" if the number is odd
 *
 * Usage:
 * const result = evenOrOdd(7);
 * // Output: "odd"
 */
function evenOrOdd(num) {
    if (num % 2 === 0){
        return "even"
    } else if (num % 2 !== 0){
        return "odd"
    }
}

module.exports = evenOrOdd;
