/**
 * fizzBuz - A function that determines if a given number is divisible by 3 and/or 5 and returns a corresponding string.
 *
 * @param {number} num - The number to be checked
 * @returns {string|number} - "Fizz" if the number is divisible by 3, "Buzz" if the number is divisible by 5, "FizzBuzz" if the number is divisible by both 3 and 5, and the number itself if it's not divisible by 3 or 5
 *
 * Usage:
 * fizzBuzz(4); //=> 4
 * fizzBuzz(6); //=> "Fizz"
 * fizzBuzz(10); //=> "Buzz"
 * fizzBuzz(15); //=> "FizzBuzz"
 */

function fizzBuzz(n) {
    if (n % 3 === 0 && n % 5 === 0){
        return "FizzBuzz"
    }

    else if (n % 3 === 0){
        return "Fizz"
    }

    else if (n % 5 === 0){
        return "Buzz"
    }
    else {
        return n
    }
}

module.exports = fizzBuzz
