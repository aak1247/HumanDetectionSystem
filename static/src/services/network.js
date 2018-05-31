import 'whatwg-fetch'
import 'es6-promise'

const server_url = "http://localhost:5000"

function obj2params(obj) {
    var result = '';
    var item;
    for (item in obj) {
        result += '&' + item + '=' + encodeURIComponent(obj[item]);
    }

    if (result) {
        result = result.slice(1);
    }
    return result;
}

// 发送 post 请求（首先会发送 option）  
function post(url, paramsObj) {
    var result = fetch(url, {
        method: 'post',
        mode: 'cors',
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
    var result = fetch('' + url, {
        credentails: 'include',
        mode: "cors",
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    });
    return result;
}


function login(user) {
    return fetch(server_url + "/user/signIn", {
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify(user),
        credentials: "include"
    })
}

function getUser() {
    return fetch(server_url + "/user", {
        method: 'GET',
        mode: 'cors',
        credentials: "include"
    })
}

function logout() {
    return fetch(server_url + "/user/signIn", {
        method: 'DELETE',
        mode: 'cors',
        body: JSON.stringify({}),
        credentials: "include"
    })
}

function register(user) {
    return fetch(server_url + "/user", {
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify(user),
        credentials: "include"
    })
}

function upload(formData) {
    return fetch(server_url + "/image", {
        method: "POST",
        mode: "cors",
        body: formData,
        credentials: "include"
    })
}

function detect(imageId) {
    console.log(imageId)
    return fetch(server_url + "/image/detect", {
        method: "POST",
        mode: "cors",
        body: JSON.stringify({
            "imageId": imageId
        }),
        credentials: "include"
    })
}

export { post, get, register, login, upload, detect, logout, getUser }