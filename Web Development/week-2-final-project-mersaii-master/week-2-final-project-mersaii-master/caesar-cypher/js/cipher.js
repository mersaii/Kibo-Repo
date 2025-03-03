export default {
    encode: (message, offset)=>{
        // console.log('hello')
        let result = ""
        const isValid = isOnlyLetters(message);
        if (isValid) {
            if (isValidOffset(offset)){
                offset = parseInt(offset, 10)
                message = message.toUpperCase();
                const stringList = message.split(' ')

                stringList.forEach(each => {
                    let char_result = ''
                    for (let i = 0; i < each.length; i++) {
                        let char = each[i];

                        const index = alphabet.indexOf(char);
                        const newIndex = (index + offset) % 26;
                        char = alphabet[newIndex];
                        char_result+=char;
                    }
                    result += " " + char_result
                });
                return result.trim();
            }else{
                alert('Offset must be numeric and between 1 and 26');
                return null;
            }
        }
        else{
            alert('Only english alphabets allowed');
            return null;
        }

    },

    decode: (message, offset)=>{
        let result = "";
        const isValid = isOnlyLetters(message);
        if (isValid)  {
            if (isValidOffset(offset)){
                offset = parseInt(offset, 10)
                message = message.toUpperCase();
                const stringList = message.split(' ');
                // console.log('string;ist: ', stringList)

                stringList.forEach(each => {
                    let char_result = '';
                    for (let i = 0; i < each.length; i++) {
                        let char = each[i];

                        const index = alphabet.indexOf(char);
                        const newIndex = (index - offset + 26) % 26;
                        char = alphabet[newIndex];
                        char_result += char;
                    }
                    result += " " + char_result;
                });
                return result.trim();
            }else{
                alert('Offset must be numeric and between 1 and 26');
                return null;
            }
        } else {
            alert('Only English alphabets allowed');
            return null;
        }
        }
}


const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

function isOnlyLetters(message) {
    // Regular expression to match only uppercase, lowercase letters and space
    const lettersRegex = /^[a-zA-Z\s]+$/;
  
    // Test if the message contains only letters
    return lettersRegex.test(message);
  }

function isValidOffset(offset) {
    // Check if offset is a numeric value
    if (!isNaN(offset)) {
        // Check if offset is within the range of 1 to +26
        if (offset >= 1 && offset <= 26) {
            return offset;
        } else {
            return false;
        }
    } else {
        return false;
    }
}
