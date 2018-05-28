import 'whatwg-fetch'  
import 'es6-promise'  

function obj2params(obj) {  
    var result = '';  
    var item;  
    for(item in obj){  
        result += '&' + item + '=' +encodeURIComponent(obj[item]);  
    }  
  
    if(result) {  
        result = result.slice(1);  
    }  
    return result;  
}  
  
// 发送 post 请求（首先会发送 option）  
function post(url, paramsObj) {  
    var result = fetch(url, {  
        method: 'post',  
        mode:'cors',  
        headers: {  
            'Accept': 'application/json',  
            'Content-Type': 'application/x-www-form-urlencoded'  
        },  
        body: obj2params(paramsObj)  
    });  
  
    return result;  
}

function get(url) {  
    // var result = fetch('http://www.mockhttp.cn'+url, { // 打包 apk 时候使用  
    var result = fetch(''+url, {  
        credentails: 'include',  
        mode: "cors",  
        headers: {  
            'Accept': 'application/json, text/plain, */*',  
            'Content-Type': 'application/x-www-form-urlencoded'  
        }  
    });  
    return result;  
}

export {post, get}