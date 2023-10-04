
//调库
var CryptoJS = require('crypto-js')

function MD5test(){
    var text = "I love python!"

    return CryptoJS.MD5(text).toString()
}

//console.log(MD5test())
function aes(val) {
    var k = CryptoJS.enc.Utf8.parse('1234567890abcDEF');
    var iv = CryptoJS.enc.Utf8.parse('1234567890abcDEF');
    enc = CryptoJS.AES.encrypt(val, k, {iv: iv, mode:CryptoJS.mode.CBC, padding: CryptoJS.pad.ZeroPadding}).toString();
    return enc;
}

a = aes('123456')
console.log(a)
b = aes('19236105524')
console.log(b)