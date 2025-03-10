/**
 * bothNumbersAreEven - A function that checks if both input numbers are even.
 *
 * @param {number} a - The first number to be checked
 * @param {number} b - The second number to be checked
 * @returns {boolean} - True if both numbers are even, false otherwise
 *
 * Usage:
 * bothNumbersAreEven(4, 6);
 * Output: true
 */
function bothNumbersAreEven(a, b) {
    if (a%2 == 0 && b%2 == 0) {
        return true;
    }
    else {
        return false;
    }
}

module.exports = bothNumbersAreEven;
