var CryptoJS = require('crypto-js')
var navigator = {
    'appVersion':'5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
var e = 'nba';
var r = "" + (new Date).getTime();
var i = r + parseInt(10 * Math.random(), 10);

function get_sign(){
    var sign;
    var mid = "fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5";
    sign = CryptoJS.MD5(mid)
    return sign.toString()
}

function get_salt(){
    var salt;
    salt = i;
    return salt;
}

function get_ts(){
    var ts;
    ts = r;
    return ts;
}

function get_bv(){
    var bv;
    bv = CryptoJS.MD5(navigator.appVersion)
    return bv.toString()
}
console.log(get_sign())

