/**
 * largestNumberInArray - A function that finds the largest number in a given array of numbers.
 *
 * @param {number[]} arr - The input array of numbers
 * @returns {number} - The largest number in the input array
 *
 * Usage:
 * const result = largestNumberInArray([1, 2, 3]);
 * // Output: 3
 */
function largestNumberInArray(arr) {
    largest = arr[0]
    for(let i=0; i < arr.length-1 ; i++){
        if (arr[i] > arr[i+1]){
            largest = arr[i]
        }else{
            largest = arr[i+1]
        }
    }return largest
}

module.exports = largestNumberInArray;
