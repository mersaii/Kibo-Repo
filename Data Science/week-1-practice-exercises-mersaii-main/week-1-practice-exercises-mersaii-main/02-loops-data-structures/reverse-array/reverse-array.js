/**
 * reverseArray - A function that reverses the elements in a given array without using Array.reverse.
 *
 * @param {Array} arr - The input array
 * @returns {Array} - A new array with the elements in reverse order
 *
 * Usage:
 * const result = reverseArray([1, 2, 3]);
 *  // Output: [3, 2, 1]
 */

function reverseArray(arr) {
    const rev_arr = []
    for (let i = arr.length-1; i >= 0; i--){
        // a = arr.pop()
        // console.log(a)
        rev_arr.push(arr[i])
    }
    return rev_arr
}

module.exports = reverseArray;
