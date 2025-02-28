/**
 * powerOfTwo - A function that calculates the power of two for a given number without using Math.pow.
 *
 * @param {number} exponent - The exponent to which 2 should be raised
 * @returns {number} - The result of 2 raised to the power of the given exponent
 *
 * Usage:
 * const result = powerOfTwo(3);
 * // Output: 8
 */

function powerOfTwo(exponent) {
    if (exponent < 0){
        return 1
    }
    let result = 1;
    for (i=0; i<exponent; i++){
        result *= 2
    }
    return result
}

module.exports = powerOfTwo;
