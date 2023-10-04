

function aes(val) {
    var k = CryptoJS.enc.Utf8.parse('1234567890abcDEF');
    var iv = CryptoJS.enc.Utf8.parse('1234567890abcDEF');
    enc = CryptoJS.AES.encrypt($.trim(val), k, {iv: iv, mode:CryptoJS.mode.CBC, padding: CryptoJS.pad.ZeroPadding}).toString();
    return enc;
}

a = aes('123456')
console.log(a)