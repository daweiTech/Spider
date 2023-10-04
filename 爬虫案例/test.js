const CryptoJS = require('crypto-js');
function encryptByAES(message, key){
	let CBCOptions = {
		iv: CryptoJS.enc.Utf8.parse(key),
		mode:CryptoJS.mode.CBC,
		padding: CryptoJS.pad.Pkcs7
	};
	let aeskey = CryptoJS.enc.Utf8.parse(key);
	let secretData = CryptoJS.enc.Utf8.parse(message);
	let encrypted = CryptoJS.AES.encrypt(
		secretData,
		aeskey,
		CBCOptions
	);
	return CryptoJS.enc.Base64.stringify(encrypted.ciphertext);
}
function decryptByAES(ciphertext, key) {
    let CBCOptions = {
        iv: CryptoJS.enc.Utf8.parse(key),
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    };
    let aeskey = CryptoJS.enc.Utf8.parse(key);
    let encryptedHexStr = CryptoJS.enc.Base64.parse(ciphertext);
    let encryptedBase64Str = CryptoJS.enc.Hex.stringify(encryptedHexStr);
    let decryptedData = CryptoJS.AES.decrypt(
        encryptedBase64Str,
        aeskey,
        CBCOptions
    );
    return decryptedData.toString(CryptoJS.enc.Utf8);
}
let ciphertext = encryptByAES("hello world", "mykey");
let plaintext = decryptByAES(ciphertext, "mykey");
console.log(plaintext);  // 输出：hello world
