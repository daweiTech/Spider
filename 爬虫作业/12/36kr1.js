window = {}
var i = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCeiLxP4ZavN8qhI+x+whAiFpGWpY9y1AHSQC86qEMBVnmqC8vdZAfxxuQWeQaeMWG07lXhXegTjZ5wn9pHnjg15wbjRGSTfwuZxSFW6sS3GYlrg40ckqAagzIjkE+5OLPsdjVYQyhLfKxj/79oOfjl/lV3rQnk/SSczHW0PEyUbQIDAQAB"
var JSEncrypt = require('jsencrypt')
function xl(str){
    
  r = new JSEncrypt();
  r.setPublicKey(i);
  var a = r.encrypt(str);
  return a

}
var t = Date.now()
console.log(t)
console.log(xl('123456'))


function get_timestamp(){
  return t
}

function get_phone(){
  return xl('19859891007')
}
function get_pwd(){
  return xl('123456DW')
}

