/**
 * canIOrderItem - A function that checks if a specified dish is available in stock.
 *
 * @param {string} dishName - The name of the dish to be checked
 * @param {Array<{[dish: string]: number}>} stockArray - An array of objects, each object having a dish name as the key and the stock as the value
 * @returns {boolean} - True if there is stock available for the specified dish, false otherwise
 *
 * Usage:
 * const stockArray = [{ "Pizza": 5 }, { "Burger": 3 }];
 * const result = canIOrderItem("Pizza", stockArray);
 * Output: true
 */
function canIOrderItem(dishName, stockArray) {
    //  Loop through each item in stockArray
    // console.log(stockArray.length,stockArray[0])
    for (let i = 0; i < stockArray.length; i++) {
        const item = stockArray[i];

        // Check if the current item has the specified dishName
        if (item.hasOwnProperty(dishName)) {
            // If the dish is found and has stock greater than 0, return true
            if (item[dishName] > 0) {
                return true;
            } else {
                // If the dish is found but has no stock, return false
                return false;
            }
        }
    }
    // If the dish is not found in stockArray, return false
    return false;
}


module.exports = canIOrderItem;