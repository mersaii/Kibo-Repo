import './css/style.css'
import cipher from './js/cipher'

// console.log(document.getElementById('welcome').innerHTML)

// const encodedMessage = cipher.encode()

const encryptText = document.getElementById('encryptedMessage')
const encryptOffset = document.getElementById('encryptedOffset')
const encryptResult = document.getElementById('encryptedMessageResult')
const encrypt_button = document.getElementById('encryptButton')

encrypt_button.addEventListener('click', function() {
    let a = encryptText.value
    let b = encryptOffset.value
    let encode_result = cipher.encode(a,b)
    encryptResult.innerHTML = encode_result;
});


const decryptText = document.getElementById('decryptedMessage')
const decryptOffset = document.getElementById('decryptedOffset')
const decryptResult = document.getElementById('decryptedMessageResult')
const decrypt_button = document.getElementById('decryptButton')

decrypt_button.addEventListener('click', function() {
    let a = decryptText.value
    let b = decryptOffset.value
    let decode_result = cipher.decode(a,b)
    decryptResult.innerHTML = decode_result
});